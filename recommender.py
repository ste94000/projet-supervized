reco_rules = {
    ("Légendaire", "Faible"): "Relancer avec contenu nostalgique",
    ("Visiteur Express", "Moyen"): "Inciter à créer un compte",
    ("Contributeur", "Très fort"): "Proposer du contenu expert / badges",
    ("Fantôme", "Faible"): "À exclure du ciblage",
    ("Fidèle Silencieux", "Fort"): "Stimuler par quiz ou participation",
}

def get_recommendation(cluster_label, level):
    return reco_rules.get((cluster_label, level), "Proposer un contenu personnalisé")
