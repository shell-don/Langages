#include <stdlib.h>
#include <stdio.h>

/* Voici le programme correspondant (rappelons que l'opérateur / correspond à la division entière et que l'opérateur %correspond à l'opération "modulo"). Utilisation de l'algorithme d'Euclide */

int main ()
{ 
  int a, b, r ;

  printf ("donnez deux entiers positifs : ") ;
  scanf ("%d%d", &a, &b) ;

  while (r != 0)
  { 
    r = a % b ;
    a = b ;
    b = r ;
   }
  printf ("leurs PGCD est : %d", a) ; 
  return 0 ;
}