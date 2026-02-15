#include <stdio.h>
#include <stdlib.h>

/* Soit trois variables a, b et c (supposées de type entier). Ecrivez les instructions permutant leurs valeurs, de sorte que la valeur de a passe dans b, celle de b dans c et celle de c dans a. On utilisera une (et une seule) variable supplémentaire nommée d (de type entier). */

int main() {
  int a, b, c, d ;
  
  /* initialisation */
  a = 1 ; 
  b = 2 ; 
  c = 3 ;
  printf ("Initialisation : a = %d, b = %d, c = %d\n", a, b, c) ;

  /* changement */
  d = c ;
  c = a ;
  a = d ; 
  d = c ; 
  c = b ;
  b = d ;

  printf ("Après permutation : a = %d, b = %d, c = %d", a, b, c) ;
}

  