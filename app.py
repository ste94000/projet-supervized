import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_loader import load_data
from model import load_model, predict_engagement
from recommender import get_recommendation
from utils import get_engagement_level, plot_distributions
from config import cluster_labels, level_labels

# Configuration
st.set_page_config(page_title="Moteur de Recommandation Engagement", layout="wide")
st.title("📊 Moteur de Recommandation - Management & Datascience")

# Chargement
with st.spinner("Chargement des données et modèles..."):
    df = load_data()
    model = load_model()

# Préparation des labels
cluster_labels_map = {v: k for k, v in cluster_labels.items()}
df['cluster_label'] = df['cluster'].map(cluster_labels_map)
df['engagement_level'] = df['score_engagement_final'].apply(get_engagement_level)

# Filtres
st.sidebar.title("🔎 Filtres de segmentation")
cluster_filter = st.sidebar.selectbox("Choisir un cluster", ["Tous"] + list(cluster_labels.keys()))
level_filter = st.sidebar.selectbox("Niveau d'engagement", ["Tous"] + level_labels)

filtered_df = df.copy()
if cluster_filter != "Tous":
    filtered_df = filtered_df[filtered_df['cluster_label'] == cluster_filter]
if level_filter != "Tous":
    filtered_df = filtered_df[filtered_df['engagement_level'] == level_filter]

# KPIs
st.subheader("📌 Indicateurs du segment")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Utilisateurs", len(filtered_df))
kpi2.metric("Score moyen", round(filtered_df['score_engagement_final'].mean(), 2))
kpi3.metric("Pages vues", round(filtered_df['num_pageviews'].mean(), 2))
kpi4.metric("Sessions moyennes", round(filtered_df['num_prior_sessions'].mean(), 2))

kpi5, kpi6, kpi7 = st.columns(3)
kpi5.metric("Rebond moyen", f"{round(filtered_df['is_bounce'].mean() * 100, 2)}%")
kpi6.metric("Ancienneté (jours)", round(filtered_df['days_since_first_session'].mean(), 2))
kpi7.metric("Dernière session (jours)", round(filtered_df['days_since_prior_session'].mean(), 2))

# OS et Pays dominants
os_cols = [col for col in df.columns if col.startswith("os_")]
os_dominant = filtered_df[os_cols].mean().idxmax().replace("os_", "")
country_cols = [col for col in df.columns if col.startswith("country_")]
country_dominant = filtered_df[country_cols].mean().idxmax().replace("country_", "")
st.info(f"🖥️ OS dominant : {os_dominant} | 🌍 Pays dominant : {country_dominant}")

# Visualisation des distributions
st.subheader("📈 Analyse des segment")
plot_distributions(filtered_df)

# Importance des variables
st.subheader("📌 Top 5 variables influençant le score")
if hasattr(model, "feature_importances_"):
    importances = model.feature_importances_
    features = df.drop(columns=['score_engagement_final', 'score_engagement_intra_cluster', 'cluster', 'cluster_label', 'engagement_level']).columns
    importance_df = pd.DataFrame({"Variable": features, "Importance": importances})
    top5 = importance_df.sort_values(by="Importance", ascending=False).head(5)

    fig = go.Figure(data=[go.Pie(
        labels=top5["Variable"],
        values=top5["Importance"],
        hole=0.4,
        textinfo='label+percent'
    )])
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Modèle incompatible pour afficher l'importance des variables.")

# Recommandation stratégique
st.subheader("🎯 Recommandation pour un segment ciblé")
col1, col2 = st.columns(2)
with col1:
    selected_cluster = st.selectbox("Cluster ciblé", list(cluster_labels.keys()))
with col2:
    selected_level = st.selectbox("Niveau d'engagement", level_labels)
rec = get_recommendation(selected_cluster, selected_level)
st.success(f"💡 Action recommandée : {rec}")

# Prédiction manuelle
st.subheader("🔮 Prédiction manuelle du score d'engagement")
if st.checkbox("Activer la prédiction manuelle"):
    example = df.drop(columns=['score_engagement_final', 'score_engagement_intra_cluster', 'cluster', 'cluster_label', 'engagement_level']).iloc[0]
    input_data = {}
    for col in example.index:
        input_data[col] = st.number_input(col, value=float(example[col]))
    score_pred = predict_engagement(model, pd.DataFrame([input_data]))
    st.write(f"🔢 Score prédit : {score_pred:.2f}")
