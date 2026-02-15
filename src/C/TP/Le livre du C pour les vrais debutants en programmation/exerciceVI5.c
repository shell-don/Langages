#include <stdio.h>
#include <stdlib.h>

/*******
Écrivez un programme qui affiche une "diagonale" d'astérisques dont el nombre est fourni par l'utilisateur :
combien d'astérisques dans votre diagonale : 5 
*
 *
  *
   *
    *

*******/

int main ()
{
  int n_a, i, j ;
  char c = ' ' ;      /*défini l'espace*/

  printf ("combien d'astérisques dans votre diagonale : ") ;
  scanf ("%d", &n_a) ;

  for (i=0 ; i<n_a ; i++) 
   {
    for (j=0 ; j<i ; j++) 
    {
      printf ("%c", c) ; /*répète l'espace en fonction de i*/
    } 
    printf ("*\n") ; 
   }
 return 0 ;
}