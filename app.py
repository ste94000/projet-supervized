import streamlit as st
import pandas as pd
from data_loader import load_data, load_data_engagement
from model import load_model, predict_engagement
from recommender import get_recommendation
from utils import get_engagement_level, plot_distributions, show_user_profile, cluster_summary
from config import cluster_labels, level_labels
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Moteur de recommandation engagement utilisateur", layout="wide")

st.sidebar.title("🔎 Filtres")
cluster_filter = st.sidebar.selectbox("Choisir un cluster", ["Tous"] + list(cluster_labels.keys()))
level_filter = st.sidebar.select_slider("Niveau d'engagement", options=["Tous"] + level_labels)

df = load_data()
model = load_model()

# Ajouter colonnes labellisées
cluster_labels_map = {v: k for k, v in cluster_labels.items()}
df['cluster_label'] = df['cluster'].map(cluster_labels_map)
df['engagement_level'] = df['score_engagement_final'].apply(get_engagement_level)

# Appliquer filtre cluster dès le départ
filtered_df = df.copy()
if cluster_filter != "Tous":
    filtered_df = filtered_df[filtered_df['cluster_label'] == cluster_filter]
if level_filter != "Tous":
    filtered_df = filtered_df[filtered_df['engagement_level'] == level_filter]

tab1, tab2 = st.tabs(["📊 Dashboard", "🔍 Exploration des clusters"])

with tab1:
    st.title("📊 Dashboard Engagement Utilisateurs")


    # KPI globaux du segment
    st.subheader("📌 KPIs")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Utilisateurs", len(filtered_df))
    kpi2.metric("Score d'engagement moyen", round(filtered_df['score_engagement_final'].mean(), 2))
    kpi3.metric("Pages vues moyennes", round(filtered_df['num_pageviews'].mean(), 2))
    kpi4.metric("Sessions moyennes", round(filtered_df['num_prior_sessions'].mean(), 2))

    kpi5, kpi6, kpi7 = st.columns(3)
    kpi5.metric("Taux de rebond moyen", f"{round(filtered_df['is_bounce'].mean() * 100, 2)}%")
    kpi6.metric("Ancienneté moyenne (jours depuis 1ère session)", round(filtered_df['days_since_first_session'].mean(), 2))
    kpi7.metric("Délai moyen depuis dernière session (jours)", round(filtered_df['days_since_prior_session'].mean(), 2))

    # OS dominant
    os_cols = [col for col in df.columns if col.startswith("os_")]
    os_dominant = filtered_df[os_cols].mean().idxmax().replace("os_", "")
    country_cols = [col for col in df.columns if col.startswith("country_")]
    country_dominant = filtered_df[country_cols].mean().idxmax().replace("country_", "")

    st.info(f"🖥️ OS dominant : {os_dominant} | 🌍 Pays dominant : {country_dominant}")

    # Vue analytique
    st.subheader("📈 Vue analytique")
    plot_distributions(filtered_df)

    # Recommandations stratégiques
    st.subheader("🧠 Recommandations")
    col1, col2 = st.columns(2)
    with col1:
        selected_cluster = st.selectbox("Cluster", list(cluster_labels.keys()), index=0)
    with col2:
        selected_level = st.selectbox("Niveau d'engagement", level_labels, index=0)
    rec = get_recommendation(selected_cluster, selected_level)
    st.success(f"🎯 Recommandation : {rec}")

    # Importance des variables (Random Forest)
    st.subheader("📌 Top variables influençant le désengagement")

    weights = {
        'mean_num_pageviews < 2': 0.25,
        'num_comments == 0': 0.20,
        'mean_num_prior_sessions <= 3': 0.15,
        'is_repeat_visitor == 0': 0.05,
        'no_username': 0.15,
        'is_bounce': -0.10,  # impact négatif
        'mean_time_sinse_priorsession': -0.05,
        'days_since_first_session < 3': 0.05
    }

    # On prend les valeurs absolues pour représenter l'importance (peu importe le signe)
    importance_df = pd.DataFrame({
        "Variable": list(weights.keys()),
        "Importance": [abs(v) for v in weights.values()]
    }).sort_values(by="Importance", ascending=False)

    # Créer un faux camembert
    fig = go.Figure(data=[go.Pie(
        labels=importance_df["Variable"],
        values=importance_df["Importance"],
        hole=0.4,
        textinfo='label+percent',
        textposition='outside'
    )])

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🔮 Prédiction de désengagement")

    with st.form("prediction_form"):
        st.markdown("**Saisir les caractéristiques de l'utilisateur :**")

        num_pageviews = st.slider("Nombre de pages vues", 0, 100, 5)
        num_comments = st.slider("Nombre de commentaires", 0, 20, 0)
        num_prior_sessions = st.slider("Nombre de sessions précédentes", 0, 50, 2)
        is_repeat_visitor = st.slider("Visiteur récurrent ?", 0.0, 1.0, 0.5)
        has_username = st.selectbox("A un nom d'utilisateur ?", [0, 1])
        is_bounce = st.slider("Quel est son taux de rebond moyen ?", 0.0, 1.0, 0.5)
        time_sinse_priorsession = st.slider("Temps depuis la session précédente (secondes)", 0, 300000)
        days_since_first_session = st.slider("Jours depuis la première session", 0, 1000, 10)

        submitted = st.form_submit_button("Prédire le désengagement")

        if submitted:
            # Variables que l'utilisateur a remplies
            user_inputs = {
                'num_pageviews': num_pageviews,
                'num_comments': num_comments,
                'num_prior_sessions': num_prior_sessions,
                'is_repeat_visitor': is_repeat_visitor,
                'has_username': has_username,
                'is_bounce': is_bounce,
                'days_since_prior_session': time_sinse_priorsession,
                'days_since_first_session': days_since_first_session
            }

            # Créer un dictionnaire complet avec toutes les variables nécessaires au modèle
            model_features = df.drop(columns=[
                'score_engagement_final',
                'score_engagement_intra_cluster',
                'cluster_label',
                'engagement_level',
                'id_visitor',
                "Unnamed: 0.2"
            ]).columns

            complete_input = {}
            for col in model_features:
                if col in user_inputs:
                    complete_input[col] = user_inputs[col]
                else:
                    # Remplir avec la moyenne du dataset
                    complete_input[col] = df[col].mean()

            # Construire le DataFrame d'entrée
            input_data = pd.DataFrame([complete_input])

            # Faire la prédiction
            prediction = predict_engagement(model, input_data)

            if hasattr(prediction, "values"):
                prediction = prediction[0]

            if is_repeat_visitor > 0.8 or num_pageviews > 10 or num_comments > 6 or is_bounce < 0.1:
                st.success("✅ L'utilisateur semble engagé.")
            elif prediction == 0:
                st.error("⚠️ L'utilisateur est à risque de désengagement.")
            else:
                st.success("✅ L'utilisateur semble engagé.")

with tab2:
    # Onglet Exploration des clusters
    # Inverser le mapping cluster → nom
    df_engagement = load_data_engagement()
    cluster_names = {v: k for k, v in cluster_labels.items()}
    df_engagement["cluster_name"] = df_engagement["cluster"].map(cluster_names)

    st.subheader("🔍 Recherche utilisateur par cluster et nom")

    # 📌 Sélection du cluster
    selected_cluster_name = st.selectbox("Sélectionner un cluster", sorted(df_engagement["cluster_name"].unique()))

    # 📌 Filtrage du DataFrame sur le cluster
    cluster_df = df_engagement[df_engagement["cluster_name"] == selected_cluster_name]

    # 📌 Liste des utilisateurs avec noms uniques
    usernames = cluster_df["user_name"].dropna().unique()
    selected_username = st.selectbox("Rechercher un nom d'utilisateur (si disponible)", sorted(usernames))

    # 📌 Filtrage sur l'utilisateur sélectionné
    # Recherche de l'utilisateur dans le nouveau dataset (cluster_df)
    user_data = cluster_df[cluster_df["user_name"] == selected_username]

    if not user_data.empty:
        # 🔑 Récupération de l'ID utilisateur depuis le cluster_df
        user_id = user_data["id_visitor"].values[0]

        # 📊 Récupération des infos KPI depuis le dataset principal (df_kpi)
        user = df[df["id_visitor"] == user_id].iloc[0]

        st.markdown(f"### 👤 Profil de **{selected_username}**")

        # 🔍 Détection dynamique des variables catégorielles
        language_cols = [col for col in df.columns if col.startswith("language_")]
        os_cols = [col for col in df.columns if col.startswith("os_")]
        medium_cols = [col for col in df.columns if col.startswith("medium_")]

        language_val = next((col.replace("language_", "") for col in language_cols if user.get(col, 0) == 1), "Non précisée")
        os_val = next((col.replace("os_", "") for col in os_cols if user.get(col, 0) == 1), "Inconnu")
        medium_val = next((col.replace("medium_", "") for col in medium_cols if user.get(col, 0) == 1), "Non précisé")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Langue :** {language_val}")
            st.markdown(f"**Appareil :** {os_val}")
            st.markdown(f"**Canal :** {medium_val}")
            st.markdown(f"**Temps depuis dernière session :** {int(user.get('days_since_prior_session', 0))} jours")
            st.markdown(f"**Ancienneté :** {int(user.get('days_since_first_session', 0))} jours")
        with col2:
            st.markdown(f"**Pages vues :** {user['num_pageviews']:.1f}")
            st.markdown(f"**Sessions :** {user['num_prior_sessions']:.1f}")
            st.markdown(f"**Commentaires :** {int(user.get('num_comments', 0))}")
            st.markdown(f"**Taux de rebond :** {user['is_bounce'] * 100:.1f} %")

        score = user["score_engagement_final"]
        niveau = "élevé" if score > 10 else "modéré" if score > 0 else "faible"
        st.markdown(f"### 📈 Score d'engagement : **{niveau}** ({round(score, 2)})")

        comportement = [
            "🔁 Revient souvent" if user["is_repeat_visitor"] else "🚶 Visiteur occasionnel",
            "💬 Commente fréquemment" if user["num_comments"] > 0 else "😶 Peu actif en commentaires",
            "👤 A un compte" if user["has_username"] else "🙈 Utilisateur anonyme"
        ]

        recommandations = [
            "📚 Articles adaptés à ses intérêts",
            "🤖 Suggestions IA ciblées",
            "💌 Offres premium et newsletters"
        ]

        st.markdown("### 🔍 Comportement :")
        st.markdown(" - " + "\n - ".join(comportement))

        st.markdown("### 🧠 Recommandations :")
        st.markdown(" - " + "\n - ".join(recommandations))

    else:
        st.info("Aucun utilisateur trouvé avec ce nom dans ce cluster.")
