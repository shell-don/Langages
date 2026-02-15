#include <stdio.h>
#include <stdlib.h>

/*******
Écrivez un programme qui affiche un nombre donné n d'entiers consécutifs, à partir d'une valeur donnée p, les valeurs notées ici n et p étant lues en données :
valeur initiale et nombre de valeurs : 48 4 48
49
50
51
********/

int main ()
{
  int n, p, i ;

  printf ("valeur initiale et nombre de valeurs : ") ;
  scanf ("%d%d", &n, &p) ;

  for (i=0 ; i < p ; i++)
  { printf ("%d\n" ,n) ; 
    n = n+1 ; }
} 