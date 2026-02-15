#include <stdio.h>
#include <stdlib.h>

/* Ecrivez un programme qui demande à l'utilisateur de lui 
fournir un nombre entier positif 
et inférieur à 10 et ceci jusqu'à ce que la réponse soit satisfaisante

donnez un entier positif inférieur à 100 : 452 
SVP positif inférieur à 100 : 0
SVP positif inférieur à 100 : 28
merci pour le nombre 28          */
/* jusqu'à ce que la condition entre parenthèse soit vraie sinon repart du début */
/* pas de ; sinon le if sera terminé */

int main ()
{
  int entier, i = 0 ;

  do
  {
    if (i == 0)            
     {
      printf ("donnez un entier positif inférieur à 100 : ") ;
      scanf ("%d", &entier) ;
      i = i+1 ;
     }
    else
     {
      printf ("SVP positif inférieur à 100 : ") ;
      scanf ("%d", &entier) ;  
     }
  }
  while (!(entier > 0 && entier <= 100)) ;
  printf ("merci pour le nombre : %d", entier) ;
}
