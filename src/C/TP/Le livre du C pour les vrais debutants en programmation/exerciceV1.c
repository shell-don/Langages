#include <stdio.h>
#include <stdlib.h>

/* Ecrivez un programme qui demande à l'utilisateur de lui 
fournir un nombre entier positif 
et inférieur à 10 et ceci jusqu'à ce que la réponse soit satisfaisante */

int main ()
{
  int entier ;

  do
  {
    printf ("donnez un entier positif inférieur à 100 : ") ;
    scanf ("%d", &entier) ;
  }
  while (!(entier > 0 && entier <= 100)) ; /* jusqu'à ce que la condition soit vraie */
  printf ("merci pour le nombre : %d", entier) ;
}
