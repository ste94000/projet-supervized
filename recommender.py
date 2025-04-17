reco_rules_intra = {
    ("Endormi à Fort Rebond", "Faible"): "Réduire le taux de rebond avec un accueil repensé et contextualisé",
    ("Endormi à Fort Rebond", "Moyen"): "Relancer l'intérêt avec des contenus mis à jour ou personnalisés",
    ("Endormi à Fort Rebond", "Fort"): "Réactiver l’intérêt via une campagne de relance ou nouveautés mises en avant",
    ("Endormi à Fort Rebond", "Très fort"): "Proposer une réintégration exclusive avec contenus ou fonctions VIP",

    ("Androidien Récurrent et Actif", "Faible"): "Faciliter la première accroche avec des contenus populaires Android",
    ("Androidien Récurrent et Actif", "Moyen"): "Personnaliser l'accueil en fonction de l'historique mobile",
    ("Androidien Récurrent et Actif", "Fort"): "Proposer des fonctions avancées pour utilisateurs réguliers sur mobile",
    ("Androidien Récurrent et Actif", "Très fort"): "Encourager à rejoindre une communauté active ou à noter du contenu",

    ("Curieux Mobile à Faible Ancienneté", "Faible"): "Simplifier l'expérience mobile dès l’entrée avec tutoriel ou suggestion rapide",
    ("Curieux Mobile à Faible Ancienneté", "Moyen"): "Renforcer l’intérêt avec des recommandations contextualisées",
    ("Curieux Mobile à Faible Ancienneté", "Fort"): "Proposer de suivre des thématiques ou de sauvegarder ses préférences",
    ("Curieux Mobile à Faible Ancienneté", "Très fort"): "Inviter à l'inscription avec avantages exclusifs sur mobile",

    ("Explorateur Récurrent Stable", "Faible"): "Dynamiser la page d’accueil avec un mix de contenu frais et familier",
    ("Explorateur Récurrent Stable", "Moyen"): "Mettre en avant les nouveautés sur ses sujets de prédilection",
    ("Explorateur Récurrent Stable", "Fort"): "Offrir des raccourcis vers les rubriques souvent visitées",
    ("Explorateur Récurrent Stable", "Très fort"): "Suggérer un espace personnalisé ou abonnement premium",

    ("Explorateur Régulier Modéré", "Faible"): "Proposer un chemin de navigation simplifié",
    ("Explorateur Régulier Modéré", "Moyen"): "Valoriser les sections déjà explorées pour approfondissement",
    ("Explorateur Régulier Modéré", "Fort"): "Inciter à enregistrer ses rubriques favorites",
    ("Explorateur Régulier Modéré", "Très fort"): "Proposer des badges de régularité ou challenges d’exploration",

    ("Linuxien Régulier et Stable", "Faible"): "Mettre en avant les sections techniques et documentées",
    ("Linuxien Régulier et Stable", "Moyen"): "Suggérer du contenu avancé ou des outils compatibles Linux",
    ("Linuxien Régulier et Stable", "Fort"): "Offrir des ressources personnalisées pour utilisateurs avertis",
    ("Linuxien Régulier et Stable", "Très fort"): "Proposer contribution communautaire ou feedback produit",

    ("Mobinaute Léger sur Réseau Local", "Faible"): "Optimiser la navigation locale mobile dès l’accueil",
    ("Mobinaute Léger sur Réseau Local", "Moyen"): "Suggérer les contenus locaux les plus vus récemment",
    ("Mobinaute Léger sur Réseau Local", "Fort"): "Proposer des alertes locales personnalisées",
    ("Mobinaute Léger sur Réseau Local", "Très fort"): "Inciter à rejoindre des groupes ou forums géolocalisés",

    ("Navigateur Occasionnel à Rebond Élevé", "Faible"): "Réduire le rebond par une accroche claire dès la landing page",
    ("Navigateur Occasionnel à Rebond Élevé", "Moyen"): "Proposer un carrousel de contenus populaires récents",
    ("Navigateur Occasionnel à Rebond Élevé", "Fort"): "Offrir un tableau de bord de suivi de lecture",
    ("Navigateur Occasionnel à Rebond Élevé", "Très fort"): "Inciter à créer un compte pour sauvegarder ses intérêts",

    ("Premier Contact Minimaliste", "Faible"): "Simplifier l'expérience et guider l’utilisateur avec un assistant de navigation",
    ("Premier Contact Minimaliste", "Moyen"): "Encourager la découverte de rubriques via recommandations automatisées",
    ("Premier Contact Minimaliste", "Fort"): "Proposer de s'abonner à un flux thématique",
    ("Premier Contact Minimaliste", "Très fort"): "Inciter à participer à la plateforme (commentaires, réactions)",

    ("Utilisateur Historique Extrême", "Faible"): "Identifier et comprendre l’évolution de ses centres d’intérêt",
    ("Utilisateur Historique Extrême", "Moyen"): "Réactiver ses thématiques passées via une sélection dynamique",
    ("Utilisateur Historique Extrême", "Fort"): "Proposer de partager son expertise dans les rubriques clés",
    ("Utilisateur Historique Extrême", "Très fort"): "Créer un programme ambassadeur ou de mentorat",

    ("Utilisateur Répétitif Confirmé", "Faible"): "Revaloriser son engagement par une mise en avant de ses interactions",
    ("Utilisateur Répétitif Confirmé", "Moyen"): "Automatiser l’accès à ses contenus favoris",
    ("Utilisateur Répétitif Confirmé", "Fort"): "Suggérer des contenus en série ou parcours avancé",
    ("Utilisateur Répétitif Confirmé", "Très fort"): "Proposer un rôle de modérateur ou d’expert communautaire",

    ("Utilisateur Volatile Desktop", "Faible"): "Analyser si le parcours utilisateur est trop long ou confus",
    ("Utilisateur Volatile Desktop", "Moyen"): "Tester des accroches contextuelles ou relances ciblées",
    ("Utilisateur Volatile Desktop", "Fort"): "Créer une page de suivi simplifiée",
    ("Utilisateur Volatile Desktop", "Très fort"): "Analyser les comportements anormaux ou non humains",

    ("Visiteur Unique à Passage Éclair", "Faible"): "Simplifier le premier point d’entrée pour capter rapidement l’attention",
    ("Visiteur Unique à Passage Éclair", "Moyen"): "Tester une mise en avant automatique de sujets d’actualité",
    ("Visiteur Unique à Passage Éclair", "Fort"): "Proposer un accès instantané à des fonctionnalités différenciantes",
    ("Visiteur Unique à Passage Éclair", "Très fort"): "Suggérer l’inscription via un call-to-action fort dès l’interaction",
}

def get_recommendation(cluster_label, level):
    return reco_rules_intra.get((cluster_label, level), "Proposer un contenu personnalisé")
