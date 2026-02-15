#include <stdio.h>
#include <stdlib.h>

/* Àpartir du tableau tprécédent, écrivez les instructions permettant de déterminer al posi- tion de son plus grand élément, c'est-à-dire la valeur de l'indice correspondant. */

int main () {
  int T[200], i, max, position ;
  max = T[0] ;
  for (i=1 ; i<200 ; i=i+1)
    if (T[i] > max) {max = T[i] ; position = T[i] ; }
  printf ("le max est : %d\nSa position est : %d", max, position) ;
}

