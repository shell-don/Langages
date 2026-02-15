#include <stdio.h>
#include <stdlib.h>

/* Soit c1 et c2, deux variables de type char. Écrivez les instructions permettant de permuter les contenus de ces deux variables. */

int main () {

  char c1, c2, c3 ;

  /* guillement seul pour les caactères */
  c1 = 's' ;  
  c2 = 'd' ;
  printf ("c1 = %c, c2 = %c\n", c1, c2) ;

  c3 = c2 ;
  c2 = c1 ;
  c1 = c3 ;
  printf ("c1 = %c, c2 = %c", c1, c2) ;

}