reco_rules = {
    ("Visiteur Léger", "Faible"): "Simplifier page d’accueil, capter l’attention dès les premières secondes",
    ("Visiteur Léger", "Moyen"): "Inciter à l’inscription avec bonus ou contenus exclusifs",
    ("Visiteur Léger", "Fort"): "Inciter à l’inscription avec bonus ou contenus exclusifs",
    ("Visiteur Léger", "Très fort"): "Inciter à l’inscription avec bonus ou contenus exclusifs",

    ("Ultra Power User", "Faible"): "Relancer via contenu exclusif ou statut VIP pour éviter le churn",
    ("Ultra Power User", "Moyen"): "Proposer fonctionnalités avancées ou expériences premium",
    ("Ultra Power User", "Fort"): "Proposer fonctionnalités avancées ou expériences premium",
    ("Ultra Power User", "Très fort"): "Créer rôle ambassadeur, offrir avant-premières et badges",

    ("Inactif Curieux", "Faible"): "Relancer par email ou notification avec du contenu ciblé et accrocheur",
    ("Inactif Curieux", "Moyen"): "Relancer par email ou notification avec du contenu ciblé et accrocheur",
    ("Inactif Curieux", "Fort"): "Relancer par email ou notification avec du contenu ciblé et accrocheur",
    ("Inactif Curieux", "Très fort"): "Relancer par email ou notification avec du contenu ciblé et accrocheur",

    ("Découverte Unique", "Faible"): "Optimiser onboarding, proposer retour avec une invitation simple",
    ("Découverte Unique", "Moyen"): "Optimiser onboarding, proposer retour avec une invitation simple",
    ("Découverte Unique", "Fort"): "Optimiser onboarding, proposer retour avec une invitation simple",
    ("Découverte Unique", "Très fort"): "Optimiser onboarding, proposer retour avec une invitation simple",

    ("Explorateur Occasionnel", "Faible"): "Suggérer contenus populaires, personnalisation rapide",
    ("Explorateur Occasionnel", "Moyen"): "Rediriger vers thématiques similaires ou newsletters ciblées",
    ("Explorateur Occasionnel", "Fort"): "Rediriger vers thématiques similaires ou newsletters ciblées",
    ("Explorateur Occasionnel", "Très fort"): "Rediriger vers thématiques similaires ou newsletters ciblées",

    ("Régulier Stable", "Faible"): "Réactiver via rappel de contenu suivi ou recommandation",
    ("Régulier Stable", "Moyen"): "Maintenir l’engagement avec badges ou contenus à débloquer",
    ("Régulier Stable", "Fort"): "Maintenir l’engagement avec badges ou contenus à débloquer",
    ("Régulier Stable", "Très fort"): "Maintenir l’engagement avec badges ou contenus à débloquer",

    ("Ancien Perdu", "Faible"): "Envoyer une campagne de re-séduction ou nostalgie (retour d'expérience)",
    ("Ancien Perdu", "Moyen"): "Envoyer une campagne de re-séduction ou nostalgie (retour d'expérience)",
    ("Ancien Perdu", "Fort"): "Envoyer une campagne de re-séduction ou nostalgie (retour d'expérience)",
    ("Ancien Perdu", "Très fort"): "Envoyer une campagne de re-séduction ou nostalgie (retour d'expérience)",

    ("Explorateur Actif", "Faible"): "Mettre en avant l’engagement via contributions ou favoris",
    ("Explorateur Actif", "Moyen"): "Mettre en avant l’engagement via contributions ou favoris",
    ("Explorateur Actif", "Fort"): "Mettre en avant l’engagement via contributions ou favoris",
    ("Explorateur Actif", "Très fort"): "Proposer challenges, quiz ou contenus collaboratifs",

    ("Nouveau Curieux", "Faible"): "Guider dans la découverte avec un parcours interactif ou contenus thématiques",
    ("Nouveau Curieux", "Moyen"): "Guider dans la découverte avec un parcours interactif ou contenus thématiques",
    ("Nouveau Curieux", "Fort"): "Guider dans la découverte avec un parcours interactif ou contenus thématiques",
    ("Nouveau Curieux", "Très fort"): "Guider dans la découverte avec un parcours interactif ou contenus thématiques",

    ("Endormi Récent", "Faible"): "Analyser friction, relancer avec nouveauté pertinente",
    ("Endormi Récent", "Moyen"): "Analyser friction, relancer avec nouveauté pertinente",
    ("Endormi Récent", "Fort"): "Analyser friction, relancer avec nouveauté pertinente",
    ("Endormi Récent", "Très fort"): "Analyser friction, relancer avec nouveauté pertinente",

    ("Silencieux Régulier", "Faible"): "Inciter à interagir : quiz, vote ou commentaire léger",
    ("Silencieux Régulier", "Moyen"): "Valoriser discrètement avec récap ou top lecteur",
    ("Silencieux Régulier", "Fort"): "Valoriser discrètement avec récap ou top lecteur",
    ("Silencieux Régulier", "Très fort"): "Valoriser discrètement avec récap ou top lecteur",

    ("Curieux Récent", "Faible"): "Encourager à approfondir la découverte avec un call-to-action simple",
    ("Curieux Récent", "Moyen"): "Encourager à approfondir la découverte avec un call-to-action simple",
    ("Curieux Récent", "Fort"): "Encourager à approfondir la découverte avec un call-to-action simple",
    ("Curieux Récent", "Très fort"): "Encourager à approfondir la découverte avec un call-to-action simple"
}



def get_recommendation(cluster_label, level):
    return reco_rules.get((cluster_label, level), "Proposer un contenu personnalisé")
