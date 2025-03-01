#############################
# TP2 : Analyses univariées #
#############################

####################
# On définit le dossier par défaut pour la session
setwd("~/Documents/Informatique/R/TP")
employes=read.table("employes.txt",header=TRUE)

# Pour accéder aux variables directement par leur nom
attach(employes)
####################

## 1 Préparation des données

# dans le data.frame toutes les variables sont de type "int" pour
# "integer" or les variables sexe, stat_pro et national sont
# qualitatives nominales dans R il faut qu'elles soient de 
# type "Factor"

# on transforme en Factor les variables qualitatives
employes$sexe=factor(employes$sexe,labels=c("F","M"))
employes$stat_pro=factor(employes$stat_pro,
                         labels=c("employé","agent de sécurité",
                                  "manager"))
employes$national=factor(employes$national,labels=c("américaine",
                                                    "autre"))

head(employes,10) # affiche les 10 premières lignes du jeu de données
tail(employes,10) # affiche les 10 dernières lignes du jeu de données

# par défaut head et tail affichent 6 lignes :
head(employes)

# descriptif du jeu de données
summary(employes)
 # donne les résumés numériques des variables quantitatives
 # et les effectifs des modalités pour les variables qualitatives

# manipulations sur le jeu de données
employes[1,] # affiche les valeurs du 1er individu à toutes les variables

employes[,1] # affiche les valeurs de tous les ind. à la 1e variable
employes$sexe # affiche les valeurs de tous les ind. à la variable sexe
 # on obtient donc la même chose que précédemment mais c'est plus simple
 # d'utiliser cette commande (on connaît le nom de la variables mais
 # pas forcément sa position)
 
employes$sexe[1:5] # affiche la valeur des 5 premiers ind. à la variable sexe
employes[1:5,]     # affiche la valeur des 5 premiers ind. à toutes les var.

employes[employes$age>=65,] # sous-échantillon des individus de 65 ans ou plus
which(employes$age>=65)     # numéro (position) des individus de 65 ans ou plus
length(which(employes$age>=65)) # nombre d'individus de 65 ans ou plus, il y en a 50
employes$age[employes$age>=65]  # âge des individus de 65 ans ou plus

sort(employes$age[employes$age>=65]) #idem en triant les valeurs par ordre croissant

employes$sexe # affiche les valeurs de tous les ind. à la variable sexe
# pour accéder à une variable on donne le nom du data.frame $ puis le nom de la variable



# 2 Description univariée d'une série de données
# 2.1 Variables qualitatives

# tableau de distribution
table(sexe)               # effectifs
prop.table(table(sexe))   # fréquences relatives
round(prop.table(table(sexe)),digits=3) # pour avoir les f_j avec seulement 3 décimales


# diagramme en colonnes
barplot(prop.table(table(stat_pro)))
barplot(prop.table(table(stat_pro)),
        main="Distribution du statut professionnel",
        ylab="Fréquence", xlab="Statut professionnel",
        ylim=c(0,1), col="darkseagreen2")

# Arguments utiles pour les graphiques
#   - main pour préciser le titre du graphique,
#   - ylab pour préciser le nom de l'axe des ordonnées,
#   - xlab pour préciser le nom de l'axe des abscisses,
#   - ylim pour choisir les bornes de l'axe des ordonnées
#      (xlim pour l'axe des abscisses)
#   - col pour changer la couleur du graphique
#   - \n pour revenir à la ligne lorsqu'un titre est trop long.

# diagramme en secteurs
pie(prop.table(table(stat_pro)),
    main="Distribution du statut professionnel")

# 2.2 Variables quantitatives
# A) Résumés numériques
summary(age)
# indicateurs de position
# minimum, 1er quartile, médiane, moyenne, 3e quartile, maximum

###### Q_1 Q_3 PAS INTERPRETES
###### var, sd, cv, quantiles
n <- length(age)
print(n)
var(age)*(n-1)/n

# écart type
sd(age)*sqrt((n-1)/n)
# CV
sd(age)/mean(age)
# Quantile
quantile(age,probs=seq(0.1,1,by=0.1))
quantile(age,probs=seq(0.1,1,by=0.01))

# Boite à moustache.
boxplot(age, horizontal=TRUE, col = "red", main="Boîte à moustaches de l'âge",
        xlab="Age (en années)")

summary(salaire)
# indicateurs de position
# minimum, 1er quartile, médiane, moyenne, 3e quartile, maximum

###### Q_1 Q_3 PAS INTERPRETES
###### var, sd, cv, quantiles
n <- length(salaire)
print(n)
var(salaire)*(n-1)/n

# écart type
sd(salaire)*sqrt((n-1)/n)
# CV
sd(salaire)/mean(salaire)
# Quantile
quantile(salaire,probs=seq(0.1,1,by=0.1))
quantile(salaire,probs=seq(0.1,1,by=0.01))

# Boite à moustache.
boxplot(salaire, horizontal=TRUE, col = "red", main="Boîte à moustaches sur les salaires",
        xlab="Salaires")

# Boite à moustache de la variable,
variable <- c(salembau)
summary(variable)
n <- length(variable)
print(n)
var(variable)*(n-1)/n
sd(variable)*sqrt((n-1)/n)
sd(variable)/mean(variable)
quantile(variale,probs=seq(0.1,1,by=0.1))
quantile(variable,probs=seq(0.1,1,by=0.01))
boxplot(variable, horizontal=TRUE, col = "red", main="Boîte à moustaches",
        xlab="variable")

Q_1sal <- quantile(variable, probs=0,25)


# B) Diagramme en bâtons

# pour une variable quantitative discrète, ici educ

# tableau de distribution
 # effectifs n_j
table(educ)
 # fréquences relatives f_j
round(prop.table(table(educ)),digits=3)
 # fréquences relatives cumulées Phi_j
cumsum(round(prop.table(table(educ)),digits=3))
# Phi_5=0.895
# 89,5% des employés de l'entreprise américaine
# ont au plus 16 années d'études après le 1st grade (CP)

# diagramme en bâtons
plot(prop.table(table(educ)),type="h",col="red",
     ylab="Fréquence",
     xlab="Nombre d'années d'études après le 1st grade",
     main="Distribution du nombre d'années d'études")

# C) Histogramme pour une variable quantitative continue
hist(age,freq=FALSE,xlab="Age",ylab="Densité de proportion",
     main="Histogramme de la variable age")
# argument freq=FALSE pour représenter les densités de proportion en ordonnées

# avec des classes personnalisées
hist(age,freq=FALSE,breaks=c(30,33,36,38,40,45,50,55,60,65,75),
xlab="Age",ylab="Densité de proportion",
main="Histogramme de la variable age,\n classes personnalisées")


# 2.3 Application

## Etude univariée du sexe
table(sexe)
round(prop.table(table(sexe)),digits=3)
barplot(prop.table(table(sexe)),main="Distribution du sexe",ylim=c(0,0.6),
        xlab="Sexe", ylab="Fréquences relatives", col="darkcyan")

## Etude univariée du statut professionnel
table(stat_pro)
round(prop.table(table(stat_pro)),digits=3)
barplot(prop.table(table(stat_pro)),main="Distribution du statut professionnel",
        ylim=c(0,1),xlab="Statut professionnel",
        ylab="Fréquences relatives", col="darkblue")

## Etude univariée de la nationalité
table(national)
round(prop.table(table(national)),digits=3)
pie(table(national),main="Distribution de la nationalité")

## Etude univariée du salaire
summary(salaire)
hist(salaire, freq=FALSE,xlab="Salaire annuel (en $)",
     breaks=c(15000,20000,25000,30000,40000,50000,70000,100000,140000),
     ylab="Densité de proportion",main="Histogramme du salaire annuel",
     col="goldenrod1")

## Etude univariée de l'expérience passée
summary(exppasse)
hist(exppasse, freq=FALSE,xlab="Expérience passée (en mois)",
     col="darkseagreen4",ylab="Densité de proportion",
     main="Histogramme de l'expérience passée")




############
# Exercice #
############

936+43 # 979
522+39 # 561
733+662 # 1395
492+496 # 988
inact=c(rep(1,979),rep(2,561),rep(3,1395),rep(4,988))
inact=factor(inact,labels=c("raisons familiales","au foyer",
                            "raisons de santé","inactivité transitoire"))
table(inact)             
round(prop.table(table(inact)),2)
