#include <stdio.h>
#include <stdlib.h>

/* En supposant que les variables n, pet q sont de type int et qu'elles contiennent respectivement les valeurs 8, 13 et 29, quelles sont les valeurs des expressions suivantes : */

int main () {
  int n, p, q, result ;

  n = 8 ;
  p = 13 ; 
  q = 29 ;
  printf ("n = %d, p = %d, q = %d\n", n, p, q) ; 
 
  result = n + p / q ;
  printf ("résultat de n + p / q = %d\n", result) ;

  result = n + q / p ;
  printf ("résultat de n + q / p = %d\n", result) ;

  result = (n + q) / p ;
  printf ("résultat de (n + q) / p = %d\n", result) ;

  result = n + p % q ;
  printf ("résultat de n + p modulo q = %d\n", result) ;

  result = n + q % p ;
  printf ("résultat de n + q modulo p = %d\n", result) ;

  result = (n + q) % p ;
  printf ("résultat de (n + q) modulo p = %d\n", result) ;

  result = n + p / n + p ;
  printf ("résultat de n + p / n + p = %d\n", result) ;

  result = (n + p) / (n + p) ;
  printf ("résultat de (n + p) / (n + p) = %d\n", result) ;
}
