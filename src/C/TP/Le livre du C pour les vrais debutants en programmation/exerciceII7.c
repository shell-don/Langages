#include <stdio.h>
#include <stdlib.h>

/* Quelles seront les valeurs attribuées à x et à y par : */

int main () {

  int n1, n2, x ; 
  float y ; 

  n1 = 15 ;
  n2 = 4 ;
  printf ("n1 = %d, n2 = %d\n", n1, n2) ; 

  x = n1 / n2 ;
  y = n1 / n2 + 0.5 ;

  printf ("n1 / n2 = %d, n1 / n2 + 0.5 = %f", x, y) ;
  /* même si x est rond c'est un float car défini comme cela, il peut être un int */
 
}