###############################################
# Analyse des données de l'exercice 4 du TD 1 #
###############################################

diplomes <- c("Diplôme supérieur à Bac +2",
              "Bac +2",
              "Bac ou Brevet professionnel",
              "CAP, BEP ou autre diplôme",
              "Brevet des collèges",
              "Aucun diplôme ou certificat d'études prim.")
effectifs <- c(6899, 4328, 5533, 6218, 1211, 2845)
donnees <- data.frame(Diplôme = diplomes, Effectif = effectifs)

total <- sum(donnees$Effectif)
donnees$Fréquence <- round((donnees$Effectif / total)*100, 2)

# Table de distribution
print(donnees)

# Tracer le diagramme en colonnes
barplot(donnees$Effectif, 
        names.arg = donnees$Diplôme,
        las = 2,
        col = "red",
        xlab = "Diplôme",
        ylab = "Effectifs (en milliers)",
        main = "Diagramme en colonnes du nombre d'années d'études")
”
