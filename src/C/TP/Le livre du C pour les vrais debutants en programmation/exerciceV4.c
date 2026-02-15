#include <stdio.h>
#include <stdlib.h>

/*******
Modifiez el programme de doublement de capital du paragraphe 13., de manière qu'il affiche, outre le capital obtenu chaque année, un numéro d'année, comme suit :

capital, à l'année 1 : 11200.00
capital, à l'année 2 : 12544.00
capital, à l'année 3 : 14049.28
capital, à l'année 4 : 15735.19
capital, à l'année 5 : 17623.42
capital, à l'année 6 : 19738.23
capital, à l'année 7 : 22106.82

int main ()
{
  float cap_ini, cap, taux ;
  printf ("donnez le capital à placer et le taux : ") ;
  scanf ("%e%e", &cap_ini, &taux) ;
  cap = cap_ini ;
  do {
    cap = cap*(1+taux) ;
    printf ("capital un an plus tard : %12.2F\n", cap) ; }
  while (cap <= 2*cap_ini) ;
}

********/

int main ()
{
  float cap_ini, cap, taux ;
  int i = 1 ;
  
  printf ("donnez le capital à placer et le taux : ") ;
  scanf ("%e%e", &cap_ini, &taux) ;
  cap = cap_ini ;
 
  while (cap <= 2*cap_ini) {
    cap = cap*(1+taux) ;
    printf ("capital, à l'année %d : %12.2F\n", i, cap) ;
    i++ ; }
}



