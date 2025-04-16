reco_rules_intra = {
    ("Visiteur Léger", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Visiteur Léger", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Visiteur Léger", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Visiteur Léger", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Super Utilisateur", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Super Utilisateur", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Super Utilisateur", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Super Utilisateur", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Explorateur Minimaliste", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Explorateur Minimaliste", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Explorateur Minimaliste", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Explorateur Minimaliste", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Découverte Instantanée", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Découverte Instantanée", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Découverte Instantanée", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Découverte Instantanée", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Explorateur Actif", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Explorateur Actif", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Explorateur Actif", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Explorateur Actif", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Curieux Fidèle", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Curieux Fidèle", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Curieux Fidèle", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Curieux Fidèle", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Anonyme Répété", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Anonyme Répété", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Anonyme Répété", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Anonyme Répété", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Décrocheur Précipité", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Décrocheur Précipité", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Décrocheur Précipité", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Décrocheur Précipité", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Nouveau Prometteur", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Nouveau Prometteur", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Nouveau Prometteur", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Nouveau Prometteur", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Endormi Historique", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Endormi Historique", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Endormi Historique", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Endormi Historique", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Silencieux Stable", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Silencieux Stable", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Silencieux Stable", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Silencieux Stable", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges",

    ("Récemment Attiré", "Faible"): "Identifier blocages : proposer aide, simplifier interface",
    ("Récemment Attiré", "Moyen"): "Stimuler avec contenu pertinent ou personnalisé",
    ("Récemment Attiré", "Fort"): "Renforcer engagement avec feedback ou gamification",
    ("Récemment Attiré", "Très fort"): "Valoriser utilisateur : recommandation sociale, badges"
}



def get_recommendation(cluster_label, level):
    return reco_rules_intra.get((cluster_label, level), "Proposer un contenu personnalisé")
