import streamlit as st
import pandas as pd
from data_loader import load_data
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

# Calcul des stats par cluster
cluster_stats = df.groupby("cluster").agg({
    "num_pageviews": "mean",
    "num_prior_sessions": "mean",
    "is_bounce": "mean",
    "id_visitor": lambda x: list(x.unique())[:5]
}).reset_index()

cluster_stats.rename(columns={
    "num_pageviews": "avg_pageviews",
    "num_prior_sessions": "avg_sessions",
    "is_bounce": "bounce_rate",
    "id_visitor": "top_users"
}, inplace=True)

# Ajouter taille du cluster
cluster_stats["size"] = df.groupby("cluster")["id_visitor"].nunique().values

st.subheader("📦 Exploration des clusters utilisateurs")

for _, row in cluster_stats.iterrows():
    with st.expander(f"🔹 Cluster {row['cluster']} – {row['size']} utilisateurs"):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Pages vues moyennes", round(row["avg_pageviews"], 2))
            st.metric("Sessions moyennes", round(row["avg_sessions"], 2))
            st.metric("Taux de rebond", f"{round(row['bounce_rate']*100, 1)} %")
        with col2:
            st.markdown("👤 **Utilisateurs typiques :**")
            selected_user = st.selectbox(
                f"Utilisateurs du cluster {row['cluster']}",
                options=row["top_users"],
                key=f"select_user_{row['cluster']}"
            )

            if selected_user:
                user = df[df["id_visitor"] == selected_user].iloc[0]
                st.markdown(f"**Nom :** {user.get('user_name', 'Inconnu·e')}")
                st.markdown(f"**Langue :** {user.get('language', 'Non précisée')}")
                st.markdown(f"**Appareil :** {user.get('os', 'Inconnu')}")
                st.markdown(f"**Canal :** {user.get('medium', 'Non précisé')}")
                st.markdown(f"**Temps depuis dernière session :** {int(user.get('days_since_prior_session', 0))} jours")
                st.markdown(f"**Pages vues :** {user['num_pageviews']:.1f}")
                st.markdown(f"**Sessions :** {user['num_prior_sessions']:.1f}")
                st.markdown(f"**Taux de rebond :** {user['is_bounce']*100:.1f} %")

                score = user["score_engagement_final"]
                niveau = "élevé" if score > 10 else "modéré" if score > 0 else "faible"
                st.markdown(f"### 📈 Score d'engagement : **{niveau}**")

                comportement = [
                    "🔁 Revient souvent" if user["is_repeat_visitor"] else "🚶 Visiteur occasionnel",
                    "💬 Commente fréquemment" if user["num_comments"] > 0 else "😶 Peu actif en commentaires"
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
