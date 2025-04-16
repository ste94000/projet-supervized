reco_rules = {
    ("Super Utilisateur", "Faible"): "Comprendre désengagement soudain, proposer exclusivité",
    ("Super Utilisateur", "Moyen"): "Stimuler avec contenus premium ou nouveautés",
    ("Super Utilisateur", "Fort"): "Stimuler avec contenus premium ou nouveautés",
    ("Super Utilisateur", "Très fort"): "Récompenser la fidélité, créer programme ambassadeur",

    ("Visiteur Régulier", "Faible"): "Analyser points de friction, suggérer navigation guidée",
    ("Visiteur Régulier", "Moyen"): "Offrir contenus populaires pour approfondir l’engagement",
    ("Visiteur Régulier", "Fort"): "Offrir contenus populaires pour approfondir l’engagement",
    ("Visiteur Régulier", "Très fort"): "Proposer création de compte pour plus de personnalisation",

    ("Décrocheur Curieux", "Faible"): "Relancer avec mail teaser ou quiz simple",
    ("Décrocheur Curieux", "Moyen"): "Renforcer lien avec notifications personnalisées",
    ("Décrocheur Curieux", "Fort"): "Renforcer lien avec notifications personnalisées",
    ("Décrocheur Curieux", "Très fort"): "Renforcer lien avec notifications personnalisées",

    ("Nouveau ou Unique", "Faible"): "Inciter à revenir via pop-up ou rappel email",
    ("Nouveau ou Unique", "Moyen"): "Transformer visite en habitude avec call-to-action clair",
    ("Nouveau ou Unique", "Fort"): "Transformer visite en habitude avec call-to-action clair",
    ("Nouveau ou Unique", "Très fort"): "Transformer visite en habitude avec call-to-action clair",

    ("Explorateur Léger", "Faible"): "Suggérer sections populaires dès la landing",
    ("Explorateur Léger", "Moyen"): "Rediriger vers contenus connexes et en profondeur",
    ("Explorateur Léger", "Fort"): "Rediriger vers contenus connexes et en profondeur",
    ("Explorateur Léger", "Très fort"): "Rediriger vers contenus connexes et en profondeur",

    ("Fidèle Modéré", "Faible"): "Sonder désintérêt, proposer changement de rythme",
    ("Fidèle Modéré", "Moyen"): "Créer routine, newsletter adaptée au profil",
    ("Fidèle Modéré", "Fort"): "Créer routine, newsletter adaptée au profil",
    ("Fidèle Modéré", "Très fort"): "Créer routine, newsletter adaptée au profil",

    ("Actif Silencieux", "Faible"): "Stimuler l’interaction (commentaire, quiz, badge)",
    ("Actif Silencieux", "Moyen"): "Mettre en avant contenus collaboratifs ou forums",
    ("Actif Silencieux", "Fort"): "Mettre en avant contenus collaboratifs ou forums",
    ("Actif Silencieux", "Très fort"): "Mettre en avant contenus collaboratifs ou forums",

    ("Fantôme Passif", "Faible"): "Exclure des campagnes, segment de veille",
    ("Fantôme Passif", "Moyen"): "Exclure des campagnes, segment de veille",
    ("Fantôme Passif", "Fort"): "Exclure des campagnes, segment de veille",
    ("Fantôme Passif", "Très fort"): "Exclure des campagnes, segment de veille",

    ("Rebond Unique", "Faible"): "Optimiser la page d’atterrissage, simplifier l’entrée",
    ("Rebond Unique", "Moyen"): "Optimiser la page d’atterrissage, simplifier l’entrée",
    ("Rebond Unique", "Fort"): "Optimiser la page d’atterrissage, simplifier l’entrée",
    ("Rebond Unique", "Très fort"): "Optimiser la page d’atterrissage, simplifier l’entrée",

    ("Fidèle Silencieux", "Faible"): "Stimuler discrètement via contenu ludique (quiz)",
    ("Fidèle Silencieux", "Moyen"): "Inciter à interagir : badges, top lecteurs",
    ("Fidèle Silencieux", "Fort"): "Inciter à interagir : badges, top lecteurs",
    ("Fidèle Silencieux", "Très fort"): "Inciter à interagir : badges, top lecteurs",

    ("Éclaireur", "Faible"): "Retenir avec navigation fluide ou tuto rapide",
    ("Éclaireur", "Moyen"): "Proposer exploration guidée (série, parcours utilisateur)",
    ("Éclaireur", "Fort"): "Proposer exploration guidée (série, parcours utilisateur)",
    ("Éclaireur", "Très fort"): "Proposer exploration guidée (série, parcours utilisateur)",

    ("Visiteur Express", "Faible"): "Pop-up d’accroche ou incitation à revenir",
    ("Visiteur Express", "Moyen"): "Proposer création de compte, enregistrement contenu",
    ("Visiteur Express", "Fort"): "Proposer création de compte, enregistrement contenu",
    ("Visiteur Express", "Très fort"): "Proposer création de compte, enregistrement contenu",
}


def get_recommendation(cluster_label, level):
    return reco_rules.get((cluster_label, level), "Proposer un contenu personnalisé")
