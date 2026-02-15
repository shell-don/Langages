#include <stdio.h>
#include <stdlib.h>

int main (void) {
  int i, k, tt, v_i, j, max, h, Position, P_possible_du_max ;
  int *ptr_i ;  
  
  /* taille et création du tableau à une dimension */ 
  printf ("Quelle est la taille du tableau (dimension 1) ? ") ; 
  scanf ("%d", &tt) ;
  if (tt == 0) {printf ("erreur : le tableau doit avvoir au minimum une taille de 1") ; return 1 ; }
    else { 
    int Tableau[tt] ; 
    printf ("Entrez %d nombres entiers\n", tt) ;
    
    /* construction du tableau */
    for (i=0 ; i<tt ; i++) {
      printf ("Entrez la valeur %d, en position %d,%d : ", i+1, 1, i+1) ;
      scanf ("%d", &v_i) ;
      Tableau[i] = v_i ; 
      
      /* affiche le tableau */
      for (j=0 ; j<=i ; j++) printf ("%d ", Tableau[j]) ; }
    
    max = Tableau[0] ;
    Position = 0 ;
    for (h=0 ; h<tt ; h++) {
      Position = Position + 1 ;
      if (Tableau[h] < max) {max = Tableau[h] ; P_possible_du_max = Position ; } 
      if (P_possible_du_max >= Position) P_possible_du_max = Position ; }
    printf ("\nle maximum du tableau est : %d \nSa position est : %d ", max, P_possible_du_max) ;
    }  
}

