#include <stdio.h>

// Commande de conversion d'un fichier .ps en .pdf avec ghostscript
// gs -sDEVICE=pdfwrite -o fichier_converti.pdf fichier.ps


// Exercice 1 : Affichage

void ligne (char c, int n) {

	for (int i = 0; i<n ; i++) {
		printf("%c", c) ;
	}
	
}

void boite (int l, int h, int e) {

	for (int i = 0 ; i<e ; i++) {
		ligne('#', l+e+e) ;
		printf("\n") ;
	} 
	for (int i = 0 ; i < h ; i++) {
		ligne('#', e) ;
		ligne(' ', l) ;
		ligne('#', e) ;
		printf("\n") ;
	}
	for (int i = 0 ; i<e ; i++) {
		ligne('#', l+e+e) ;
		printf("\n") ;
	} 

}

// Exercice 2 : exponentielle

void puissance (double x, int n) {

	if (n == 0) {
		printf("1 \n") ;
	} else {
		if (n % 2 == 0) {
			double y = 1 ;
			for (int i = 0 ; i < n/2 ; i++) {
				y *= x ;
			} 
			y *= y ; 
			printf("%e \n", y) ;
		} else {
			double y = 1 ;
			for (int i = 0 ; i < n/2 ; i++) {
				y *= x ;
			} 
			y = (y*y)*x ; 
			printf("%e \n", y) ;
		}
	}
}

// Exercice 3 : Instrumentation de l'exponentielle

int compteur_global ;

double mul (double x, double y) {

	compteur_global++ ; 
	return x*y ;
}

void puissance_compteur (double x, int n) {

	if (n == 0) {
		printf("1 \n") ;
	} else {
		if (n % 2 == 0) {
			double y = 1 ;
			for (int i = 0 ; i < n/2 ; i++) {
				y *= x ;
			} 
			y = mul(y, y) ; 
			printf("%e \n", y) ;
		} else {
			double y = 1 ;
			for (int i = 0 ; i < n/2 ; i++) {
				y *= x ;
			} 
			y = mul(mul(y,y), x) ; 
			printf("%e \n", y) ;
		}
	}
}

// Exercice 4 : Fibonacci récursif

int fibo (int n) {

	int x = 1, y = 1, z = 0 ;

	if (n == 0) {
		return 1 ;
	} else if (n == 1) {
		return 1 ;
	} else {
		for (int i = 0 ; i < n ; i++) {
			z = y + x ; 
			x = y ; 
			y = z ;
		}
		return z ;  
	}
}

// Exercice 6 : Tortue Logo

double x = 297, y = 419 ; /* milieu de la page */
int dir ; 

void avance (double pas) {

	printf("%f %f moveto ", x, y) ;
	if (dir == 0) {
		// printf("1 0 0 setrgbcolor ") ; 
		y = y + pas ; 
	} else if (dir == 1) {
		// printf("0 0 1 setrgbcolor ") ;
		x = x + pas ;
	} else if (dir == 2) {
		// printf("1 0 1 setrgbcolor ") ;
		y = y - pas ; 
	} else if (dir == 3) {
		// printf("0 1 0 setrgbcolor ") ;
		x = x - pas ;
	} 
	printf("%f %f lineto stroke\n", x, y) ;
}

void tourne_droite () {
	dir = (dir + 1) % 4 ;
}

void tourne_gauche () {
	dir = (dir + 3) % 4 ;
}

void courbe (int n) {

	if (n <= 0) {
		avance (3) ;
	} else {
		tourne_droite () ;
		courbe(n-1) ;
		tourne_gauche() ;
		courbe(n-1) ;
	}
} 

int main () {

	printf("%%!postscript\n") ;
	courbe(16) ;
	printf("showpage") ;

	return 0 ;

}