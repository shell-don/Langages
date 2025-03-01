#########################################################################
####             TP1 : Prise en main du logiciel RStudio             ####
#########################################################################


# pour définir le dossier par défaut
# à faire à chaque début de session
setwd("~/Documents/Informatique/R/TP")
# pensez à personnaliser ce dossier si vous reprenez un de mes scripts !

### 1.1 Environnement de travail
## D) Ouvrir un script
2+2
4/2
x=c(2,5,9)      # crée le vecteur x (on le voit dans la fenêtre Environment)


###  1.2 Opérations élémentaires
## A) Logique par objet de R

# vecteur
x = c(2,1,1,3,2) # crée le vecteur x (on le voit dans la fenêtre Environment)
                 # il remplace le précédent vecteur x
x            # affiche le vecteur x dans la console
y <- c(1:5)  # crée le vecteur y
y            # affiche le vecteur y dans la console

length(x)    # longueur du vecteur x
y[3]         # on affiche le 3e élément de y
y[-3]        # on affiche y sans spn 3e élément


# data.frame
F <- data.frame(x=rep(1,4),y=1:4,z=c(1,5,2,6))
 # on crée le data.frame F avec 3 variables x (valeur 1 répliquée 4 fois),
 # y (entiers de 1 à 4) et z
F            # on affiche F dans la console

F$x          # affiche la variable x du data.frame F
x            # affiche le vecteur x (qui est dans Values et non la variable x de F)

names(F)     # noms des colonnes (variables)    
names(F) <- c("A","B","C") # on les remplace par A, B et C
F

row.names(F) # noms des lignes (individus)

head(F,3)    # 3 premières lignes de F
tail(F,3)    # 3 dernières lignes de F

F[2,]        # valeurs prises par le 2e ind pour toutes les variables
F[2:4,]      # valeurs prises par les individus 2 à 4 pour toutes les variables
F[c(2,4),]   # valeurs prises par les individus 2 et 4 pour toutes les variables
F$B[2]       # valeur prise par le 2e individu à la variable B


## B) Instructions logiques
x<2   # compare chaque élément de x à 2 : TRUE s'il est <2
x==2  # TRUE si l'élément est égal à 2      
x!=2  # TRUE si l'élément est différent de 2  
x!=2 | y<=3  # TRUE si l'élt de x est différent de 2 OU l'élt de y est <=3
x==1 & y>2   # TRUE si l'élt de x = 1 ET l'élt de y est >2
which(x!=2)  # position/numéro des individus qui remplissent la condition (x différent de 2)
x[x!=2]      # valeur de x pour les ind.qui remplissent la condition (x différent de 2)

F[F$B==2 & F$C==2,] # aucun individu n'a pour valeur 2 à B et à C
F[F$B==2 | F$C==2,] #on affiche F pour les ind. qui remplissent la condition : B=2 ou C=2 
 # individus 2 et 3


## C) Opérations sur un vecteur numérique

x+y
x-y
x*10
x/5
x^2      # élève chaque élément de x au carré
sqrt(x)  # racine carrée
log(x)   # ln
sort(c(2,4,1))  # tri par ordre croissant

# données manquantes
x[3]=NA;x     # on affecte une donnée manquante au 3e individu de x
is.na(x)      # renvoie pour chaque élément TRUE si c'est une donnée manquante
any(is.na(x)) # renvoie TRUE s'il y a au moins une donnée manquante
which(is.na(x)) # renvoie la position des individus dont les données sont manquantes
all(is.na(x)) # renvoie TRUE si toutes les valeurs sont manquantes


##### Remarques sur la gestion des objets dans le workspace (fenêtre Environment)

rm(y)  # pour supprimer le vecteur y (séparer les noms par des virgules s'il y en a plusieurs)
# icône balai de la fenêtre Environment pour supprimer tous les objets


### 2 Importer et exporter des données
### 2.1 Importer des données

employes=read.table("employes.txt",header=TRUE)
