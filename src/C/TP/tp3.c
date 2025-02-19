#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Exercice 6 : Racine Carré par la méthode de Newton (de 2)

int Newton () {

	double i = 2 ;
	printf("%.10f", sqrt(i)) ;
	return 0 ;
}

int Newton_iteratif () {

	double x = 1 ;
	double y = (x+2/x)/2 ;
	while(y>=x+1e-10 || y<=x-1e-10) {
		double tmp = y ;
		y = (y+2/y)/2 ;
		x = tmp ;
	}
	printf("%.10f\n",y) ;
	return 0 ;

}

int main () {

	Newton_iteratif () ;
	return 0 ;

}