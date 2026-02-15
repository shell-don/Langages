#include <stdio.h>
#include <stdlib.h>

int main () {
  system( "echo 'Quel est le chemin du fichier ?'" ) ;
  system( "read CHEMIN_FICHIER" ) ;
  system( "CHEMIN_ORIGINE=$CHEMIN_FICHIER" ) ;
  system( "echo 'Combien de fois voulez-vous le chiffrer ?'" ) ;
  system( "read n" ) ;
  system( "echo $n" ) ; 
}

/* la dernière commande ne renvoie rien car à chaque appel de system un nouveaux processus est commencé, comme si un nouveaux terminal était lancé */