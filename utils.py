def get_engagement_level(score):
    if score < 25:
        return "Faible"
    elif score < 50:
        return "Moyen"
    elif score < 75:
        return "Fort"
    else:
        return "Très fort"

def cluster_summary(df):
    return df.groupby(['cluster_label', 'engagement_level']).agg({
        'id_visitor': 'count',
        'score_engagement_final': 'mean'
    }).rename(columns={'id_visitor': 'Nb Utilisateurs', 'score_engagement_final': 'Score moyen'}).reset_index()

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def plot_distributions(df):
    # Histogramme du score d'engagement
    fig1 = px.histogram(
        df,
        x="score_engagement_final",
        nbins=30,
        title="Distribution des scores d'engagement",
        color_discrete_sequence=["#636EFA"]
    )
    fig1.update_layout(xaxis_title="Score", yaxis_title="Nombre d'utilisateurs")
    st.plotly_chart(fig1, use_container_width=True)

    # Répartition par cluster
    cluster_order = df['cluster_label'].value_counts().index.tolist()
    df["cluster_label"] = pd.Categorical(df["cluster_label"], categories=cluster_order, ordered=True)
    fig2 = px.histogram(
        df,
        x="cluster_label",
        title="Répartition par cluster",
        color_discrete_sequence=["#EF553B"]
    )
    fig2.update_layout(xaxis_title="Cluster", yaxis_title="Nombre d'utilisateurs")
    st.plotly_chart(fig2, use_container_width=True)

def show_user_profile(user):
    st.subheader("📌 Détails utilisateur")

    st.write("🆔 ID:", user["id_visitor"])
    st.write("⭐ Score engagement:", user["score_engagement_final"])
    st.write("📦 Cluster:", user["cluster_label"])
    st.write("📊 Niveau:", user["engagement_level"])

    # Graphe radar Plotly
    fig = go.Figure()

    categories = ["num_pageviews", "num_comments", "is_bounce"]
    values = [user[col] for col in categories]

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=["Pages vues", "Commentaires", "Bounce"],
        fill='toself',
        name='Profil'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=False,
        title="Profil utilisateur : comportement"
    )

    st.plotly_chart(fig, use_container_width=True)
