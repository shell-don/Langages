#include <stdio.h>
#include <stdlib.h>

/* 
Écrivez un programme complet qui calcule le prix TTC d'un nombre donné d'articles de prix unitaire donné, compte tenu d'un taux de T.V.A. de 19,6%. On initialisera les variables voulues au moment de leur déclaration. Les résultats devront se présenter ainsi :
nombre d articles : 5
prix HT : 42.15 
prix TTC : 252,06 */

int main () { 
  float tva, prixHT, prixTTC  ; 
  int nbarticles ;

  nbarticles = 5 ;
  prixHT = 42.15 ;  
  tva = 19.6 ; 
  prixTTC = prixHT*0.196 ;

  printf ("nombre d articles : %d\nprix HT : %f\nprix TTC : %f", nbarticles, prixHT, prixTTC) ;
}