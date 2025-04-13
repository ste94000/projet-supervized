import streamlit as st
import pandas as pd
from data_loader import load_data
from model import load_model, predict_engagement
from recommender import get_recommendation
from utils import get_engagement_level, plot_distributions, show_user_profile, cluster_summary
from config import cluster_labels, level_labels

st.set_page_config(page_title="Engagement Segmentation App", layout="wide")

st.sidebar.title("🔎 Filtres")
cluster_filter = st.sidebar.selectbox("Choisir un cluster", ["Tous"] + list(cluster_labels.keys()))
level_filter = st.sidebar.select_slider("Niveau d'engagement", options=["Tous"] + level_labels)
user_id = st.sidebar.text_input("🔍 Rechercher un utilisateur")

df = load_data()
model = load_model()

# Ajouter colonnes labellisées
df['cluster_label'] = df['cluster'].map({v: k for k, v in cluster_labels.items()})
df['engagement_level'] = df['score_engagement_final'].apply(get_engagement_level)

st.title("📊 Dashboard Engagement Utilisateurs")

# Filtrage dynamique
filtered_df = df.copy()
if cluster_filter != "Tous":
    filtered_df = filtered_df[filtered_df['cluster_label'] == cluster_filter]
if level_filter != "Tous":
    filtered_df = filtered_df[filtered_df['engagement_level'] == level_filter]
if user_id:
    filtered_df = filtered_df[filtered_df['id_visitor'].astype(str).str.contains(user_id)]

# Résumé segment
st.subheader("🔎 Résumé du segment")
st.write(f"Nombre d'utilisateurs : {len(filtered_df)}")
st.dataframe(cluster_summary(filtered_df))

# Matrice
st.subheader("🧭 Matrice Engagement × Cluster")
matrix = pd.crosstab(df['cluster_label'], df['engagement_level'])
st.dataframe(matrix)

# Recommandations stratégiques
st.subheader("🧠 Recommandation contextuelle")
col1, col2 = st.columns(2)
with col1:
    selected_cluster = st.selectbox("Cluster", list(cluster_labels.keys()))
with col2:
    selected_level = st.selectbox("Niveau d'engagement", level_labels)
rec = get_recommendation(selected_cluster, selected_level)
st.write(f"🎯 **Recommandation :** {rec}")

# Liste des utilisateurs filtrés
st.subheader("👥 Utilisateurs correspondants")
st.dataframe(filtered_df[['id_visitor', 'cluster_label', 'engagement_level', 'score_engagement_final']])

# Profil détaillé utilisateur
if user_id and not filtered_df.empty:
    st.subheader("📌 Profil utilisateur")
    show_user_profile(filtered_df.iloc[0])

# Vue analytique
st.subheader("📈 Vue analytique")
plot_distributions(df)

# Prédiction (exemple d'utilisation du modèle)
st.subheader("🔮 Prédire le score pour un nouvel utilisateur")
if st.checkbox("Activer prédiction manuelle"):
    example = df.drop(columns=['score_engagement_final', 'score_engagement_intra_cluster', 'cluster', 'cluster_label', 'engagement_level']).iloc[0]
    input_data = {}
    for col in example.index:
        input_data[col] = st.number_input(col, value=float(example[col]))
    score_pred = predict_engagement(model, pd.DataFrame([input_data]))
    st.write(f"🔢 Score prédit : {score_pred:.2f}")
