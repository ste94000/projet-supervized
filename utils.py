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
import streamlit as st

def plot_distributions(df):
    fig, ax = plt.subplots()
    sns.histplot(df['score_engagement_final'], bins=30, ax=ax)
    ax.set_title("Distribution des scores d'engagement")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.countplot(x='cluster_label', data=df, order=df['cluster_label'].value_counts().index, ax=ax)
    ax.set_title("Répartition par cluster")
    st.pyplot(fig)

def show_user_profile(user):
    st.write("ID:", user['id_visitor'])
    st.write("Score engagement:", user['score_engagement_final'])
    st.write("Cluster:", user['cluster_label'])
    st.write("Niveau:", user['engagement_level'])
    st.write("Pages vues:", user['num_pageviews'])
    st.write("Commentaires:", user['num_comments'])
    st.write("Bounce:", user['is_bounce'])
