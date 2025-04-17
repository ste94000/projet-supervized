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
st.subheader("📌 KPIs du segment sélectionné")
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
st.subheader("📈 Vue analytique du segment")
plot_distributions(filtered_df)

# Recommandations stratégiques
st.subheader("🧠 Recommandation contextuelle")
col1, col2 = st.columns(2)
with col1:
    selected_cluster = st.selectbox("Cluster", list(cluster_labels.keys()), index=0)
with col2:
    selected_level = st.selectbox("Niveau d'engagement", level_labels, index=0)
rec = get_recommendation(selected_cluster, selected_level)
st.success(f"🎯 Recommandation : {rec}")

# Importance des variables (Random Forest)
st.subheader("📌 Importance des variables dans le modèle d'engagement")

if hasattr(model, "feature_importances_"):
    importances = model.feature_importances_
    features = df.drop(columns=['score_engagement_final', 'score_engagement_intra_cluster', 'cluster', 'cluster_label', 'engagement_level']).columns
    importance_df = pd.DataFrame({
        "Feature": features,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False).head(20)

    fig = px.bar(importance_df, x="Importance", y="Feature", orientation="h", title="Top 20 Variables les Plus Importantes")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Le modèle chargé ne permet pas d’afficher l’importance des variables.")
