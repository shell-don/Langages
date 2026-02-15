#include <stdio.h>
#include <stdlib.h>

/* demande au périphérique (clavier) un int */

int main ()
{
  float carre, cube, valeur ;
  int ent ;

  printf ("donnez un nombre réel : ") ;
  scanf ("%e", &valeur) ;
  carre = valeur * valeur ;
  cube = carre * valeur ;
  printf ("la valeur %f a pour carré %f et pour cube %f \n" , valeur, carre, cube) ;
  ent = cube ;
  printf ("la valeur entière de son cube est : %d", ent) ;
  
}
