import streamlit as st
import pandas as pd
from data_loader import load_data
from model import load_model, predict_engagement
from recommender import get_recommendation
from utils import get_engagement_level, plot_distributions, show_user_profile, cluster_summary
from config import cluster_labels, level_labels
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Engagement Segmentation App", layout="wide")

st.sidebar.title("🔎 Filtres")
cluster_filter = st.sidebar.selectbox("Choisir un cluster", ["Tous"] + list(cluster_labels.keys()))
level_filter = st.sidebar.select_slider("Niveau d'engagement", options=["Tous"] + level_labels)
user_id = st.sidebar.text_input("🔍 Rechercher un utilisateur")

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
if user_id:
    filtered_df = filtered_df[filtered_df['id_visitor'].astype(str).str.contains(user_id)]

st.title("📊 Dashboard Engagement Utilisateurs")

# KPI globaux du segment
st.subheader("📌 KPIs du segment sélectionné")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Utilisateurs", len(filtered_df))
kpi2.metric("Score d'engagement moyen", round(filtered_df['score_engagement_final'].mean(), 2))
kpi3.metric("Pages vues moyennes", round(filtered_df['num_pageviews'].mean(), 2))

kpi4, kpi5, kpi6 = st.columns(3)
kpi4.metric("Sessions moyennes", round(filtered_df['num_prior_sessions'].mean(), 2))
kpi5.metric("Commentaires moyens", round(filtered_df['num_comments'].mean(), 2))
kpi6.metric("Taux de rebond moyen", f"{round(filtered_df['is_bounce'].mean() * 100, 2)}%")

kpi7, kpi8, kpi9 = st.columns(3)
kpi7.metric("Ancienneté moyenne (jours depuis 1ère session)", round(filtered_df['days_since_first_session'].mean(), 2))
kpi8.metric("Délai moyen depuis dernière session", round(filtered_df['days_since_prior_session'].mean(), 2))
kpi9.metric("Nombre moyen de pays (1-hot)", round(filtered_df[[col for col in df.columns if col.startswith('country_')]].sum(axis=1).mean(), 2))

# OS dominant
os_cols = [col for col in df.columns if col.startswith("os_")]
os_dominant = filtered_df[os_cols].mean().idxmax().replace("os_", "")
country_cols = [col for col in df.columns if col.startswith("country_")]
country_dominant = filtered_df[country_cols].mean().idxmax().replace("country_", "")

st.info(f"🖥️ OS dominant : {os_dominant} | 🌍 Pays dominant : {country_dominant}")

# Matrice Engagement × Cluster
st.subheader("🧭 Matrice Engagement × Cluster")
matrix = pd.crosstab(filtered_df['cluster_label'], filtered_df['engagement_level'])
fig_matrix = px.imshow(matrix, text_auto=True, aspect="auto", title="Engagement × Cluster")
st.plotly_chart(fig_matrix, use_container_width=True)

# Recommandations stratégiques
st.subheader("🧠 Recommandation contextuelle")
col1, col2 = st.columns(2)
with col1:
    selected_cluster = st.selectbox("Cluster", list(cluster_labels.keys()), index=0)
with col2:
    selected_level = st.selectbox("Niveau d'engagement", level_labels, index=0)
rec = get_recommendation(selected_cluster, selected_level)
st.success(f"🎯 Recommandation : {rec}")

# Liste des utilisateurs (affichage résumés)
st.subheader("👥 Profils d'utilisateurs")
if not filtered_df.empty:
    for idx, row in filtered_df.head(5).iterrows():
        st.markdown(f"**ID :** {row['id_visitor']} | **Score d'engagement:** {row['score_engagement_final']:.1f} | **Niveau :** {row['engagement_level']} | **Cluster :** {row['cluster_label']}")
        st.progress(min(int(row['score_engagement_final']), 100))
else:
    st.info("Aucun utilisateur correspondant.")

# Profil utilisateur sélectionné
if user_id and not filtered_df.empty:
    st.subheader("🔍 Profil détaillé utilisateur")
    show_user_profile(filtered_df.iloc[0])

# Vue analytique
st.subheader("📈 Vue analytique du segment")
plot_distributions(filtered_df)

# Prédiction (exemple d'utilisation du modèle)
st.subheader("🔮 Prédire le score pour un nouvel utilisateur")
if st.checkbox("Activer prédiction manuelle"):
    example = df.drop(columns=['score_engagement_final', 'score_engagement_intra_cluster', 'cluster', 'cluster_label', 'engagement_level']).iloc[0]
    input_data = {}
    for col in example.index:
        input_data[col] = st.number_input(col, value=float(example[col]))
    score_pred = predict_engagement(model, pd.DataFrame([input_data]))
    st.write(f"🔢 Score prédit : {score_pred:.2f}")
