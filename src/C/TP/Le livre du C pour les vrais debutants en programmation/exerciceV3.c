#include <stdio.h>
#include <stdlib.h>

/******
Écrivez le programme exemple du paragraphe 1.1, en utilisant l'instruction while au lieu de l'instruction do. while.

int main ()
{
  int n ;
  do 
  {
    printf ("donnez un nombre entier : ") ;
    scanf ("%d", &n) ;
    printf ("voici son carré : %d\n", n*n) ;
  }
  while (n != 0) ;
  printf ("fin du programme - au revoir") ;
} 

******/

int main ()
{
  int n ;
  while (n != 0) {
    printf ("donnez un nombre entier : ") ;
    scanf ("%d", &n) ;
    printf ("voici son carré : %d\n", n*n) ; }
  printf ("fin du programme - au revoir") ;
}
    