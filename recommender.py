reco_rules_intra = {
    ("Navigateur Occasionnel", "Faible"): "Proposer une visite guidée ou landing engageante",
    ("Navigateur Occasionnel", "Moyen"): "Recommander contenu populaire simple d'accès",
    ("Navigateur Occasionnel", "Fort"): "Suggérer création de compte ou favoris",
    ("Navigateur Occasionnel", "Très fort"): "Mettre en avant forum ou interactions",

    ("Utilisateur Historique Extrême", "Faible"): "Réactiver avec contenu historique ou premium",
    ("Utilisateur Historique Extrême", "Moyen"): "Inciter à partager expérience ou feedback",
    ("Utilisateur Historique Extrême", "Fort"): "Valoriser par statut ou privilèges",
    ("Utilisateur Historique Extrême", "Très fort"): "Transformer en ambassadeur utilisateur",

    ("Premier Contact Minimaliste", "Faible"): "Améliorer première impression, simplifier page d’entrée",
    ("Premier Contact Minimaliste", "Moyen"): "Proposer test ou découverte rapide",
    ("Premier Contact Minimaliste", "Fort"): "Encourager à explorer d'autres sections",
    ("Premier Contact Minimaliste", "Très fort"): "Inciter à créer un compte dès l’accueil",

    ("Visiteur Unique Rapide", "Faible"): "Retargeting ou relance email immédiate",
    ("Visiteur Unique Rapide", "Moyen"): "Pop-up d'incitation au retour",
    ("Visiteur Unique Rapide", "Fort"): "Suggestion de contenu lié à la visite précédente",
    ("Visiteur Unique Rapide", "Très fort"): "Offre flash ou bonus de fidélité au retour",

    ("Explorateur Régulier", "Faible"): "Renforcer la régularité avec contenu hebdo",
    ("Explorateur Régulier", "Moyen"): "Mettre en avant espace personnel ou favoris",
    ("Explorateur Régulier", "Fort"): "Introduire notifications personnalisées",
    ("Explorateur Régulier", "Très fort"): "Offrir contenus exclusifs ou premium",

    ("Mobinaute Côte d’Ivoire", "Faible"): "Optimiser performance mobile, navigation plus fluide",
    ("Mobinaute Côte d’Ivoire", "Moyen"): "Mettre en avant l'app si existante",
    ("Mobinaute Côte d’Ivoire", "Fort"): "Push mobile ou WhatsApp personnalisé",
    ("Mobinaute Côte d’Ivoire", "Très fort"): "Offres ciblées via canal mobile préféré",

    ("Explorateur Marocain", "Faible"): "Curation de contenu localisé",
    ("Explorateur Marocain", "Moyen"): "Encourager à enregistrer ou suivre contenus",
    ("Explorateur Marocain", "Fort"): "Mise en avant de contenu interactif",
    ("Explorateur Marocain", "Très fort"): "Créer espace communautaire local",

    ("Volatile US Desktop", "Faible"): "Identifier points de sortie, A/B test",
    ("Volatile US Desktop", "Moyen"): "Pop-up sortie ou sondage",
    ("Volatile US Desktop", "Fort"): "Recommandations personnalisées desktop",
    ("Volatile US Desktop", "Très fort"): "Bêta features pour utilisateurs experts",

    ("Curieux Mobile Afrique", "Faible"): "Interface allégée, mode faible débit",
    ("Curieux Mobile Afrique", "Moyen"): "Contenu snackable adapté mobile",
    ("Curieux Mobile Afrique", "Fort"): "Favoris + suggestions localisées",
    ("Curieux Mobile Afrique", "Très fort"): "Badge ou progression à débloquer",

    ("Endormi Ancien Suisse", "Faible"): "Relancer avec contenu nostalgique",
    ("Endormi Ancien Suisse", "Moyen"): "Email de retour personnalisé",
    ("Endormi Ancien Suisse", "Fort"): "Rappel du contenu consulté précédemment",
    ("Endormi Ancien Suisse", "Très fort"): "Offre de bienvenue ou retour",

    ("Linuxien Régulier Belgique", "Faible"): "Proposer fonctionnalités techniques avancées",
    ("Linuxien Régulier Belgique", "Moyen"): "Outils personnalisés open source",
    ("Linuxien Régulier Belgique", "Fort"): "Espace contribution ou suggestion",
    ("Linuxien Régulier Belgique", "Très fort"): "Beta testeur / contributeur communauté",

    ("Androidien Tunisien Récurrent", "Faible"): "Réduire friction sur mobile Android",
    ("Androidien Tunisien Récurrent", "Moyen"): "Parcours mobile guidé",
    ("Androidien Tunisien Récurrent", "Fort"): "Notifications push ciblées",
    ("Androidien Tunisien Récurrent", "Très fort"): "Accès rapide à l’app ou récompenses"
}


def get_recommendation(cluster_label, level):
    return reco_rules_intra.get((cluster_label, level), "Proposer un contenu personnalisé")
