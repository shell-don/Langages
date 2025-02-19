#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Utilisation chatGPT : verification de l'entré utilisateur + boucle à flag (concept) + débugage

// Exercice 1 : Premier programme

int HelloWorld () {

	fprintf(stdout, "Hello World \n") ;
	return 0 ;

}

// Exercice 2 : Conditionnelles

int Q1() {
    
	int x = 0 ;

    	printf("Entrez un entier : ") ;
    	if (scanf("%d", &x) != 1) {
        	fprintf(stderr, "Erreur de saisie \n");
        	return 1 ;
    	}
	getchar() ; 
	
    	if (x == 42) {
        	printf("Gagné ! \n") ;
        	return 0 ;
    	} else {
        	printf("Perdu ! \n") ;
        	return 1 ;
    	}
}

int Q2 () {

	int x = 0 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &x) != 1) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;
	
	if (x == 1) {printf("Un \n") ; return 0 ; }
	if (x == 2) {printf("Deux \n") ; return 0 ; }
	printf("Autre \n") ;
	return 1 ;

}

int Q3 () {

	int x = 0 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &x) != 1) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;

	if (x >= 0) {
		if (x > 100) {
			printf("Supérieur à 100 \n") ;
			return 0 ;
		} else {
			printf ("Entre 0 et 100 \n") ;
			return 0 ;
		}
	} else {
		printf("Négatif \n") ; 
		return 0 ;
	}		

}

// Exercice 3 : Boucles Simples

int Q4 () {

	int n = 0 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &n) != 1) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;

	do
	{
		printf ("*") ; 
		n-- ;
	}
	while (n != 0) ;
	printf ("\n") ;	
	
	return 0 ;
}

int Q5 () {

	int n = 0 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &n) != 1) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;

	while (n != 0) {
	
		printf ("* \n") ; 
		n-- ;
	}
	printf ("\n") ;	

	return 0 ;
}

int Q6 () {

	int n = 0 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &n) != 1) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;

	for (int i = 1 ; i <= n ; i++) {
		printf("%d ", i*i) ; 
	}

	return 0 ;
}

// Exercice 4 : Boucles avec flag

int Q7 () {

	int n = 0 ;
	int flag = 1 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &n) != 1 || n < 0) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;
	
	while (flag) {
		for (int i = 1 ; i <= n ; i++) {
			if (i == 6) {
				printf("6 se trouve dans [0 : %d]", n) ;
				flag = 0 ;
				return 0 ;
			} 
			
		}
	printf("6 ne se trouve pas dans [0 : %d]", n) ;
	return 0 ;	
	}

	return 0 ;
}

// Exercice 5 : Boucles avec accumulation

int somme_des_cubes () {

	int n = 0 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &n) != 1 || n < 0) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;

	int ri = 0 ;
	int r = 0 ;
	for (int i = 1 ; i <= n ; i++) {
		ri = i*i*i ;
		r = r + ri ;
	}

	printf("%d \n", r) ;
	return 0 ; 
}

int factorielle () {

	int n = 0 ;
	int r = 1 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &n) != 1 || n < 0) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;
	
	if ( n == 0 ) {
		printf("1 \n") ;
		return 0 ;
	} else {
		for (int i = 1 ; i <= n ; i++) {
			r = r*i ;
		}
	}
	

	printf("%d \n", r) ;
	return 0 ;
}

int factorielle_variante () {

	int n = 0 ;
	int r = 1 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &n) != 1 || n < 0) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;
	
	if ( n == 0 ) {
		printf("1 \n") ;
		return 0 ;
	} else {
		for (int i = 1 ; i <= n ; i++) {
			r = r*i ;
			printf("%d! = %d \n", i, r) ; 
		}
	}
	
	return 0 ;
}

// Exercice 6 : Tirage de nombres aléatoire

int lignes () {

	int r = 0x0 ;

	for (int i = 0x0 ; i < 0xA ; i++) {
		r = rand() % 7 ;
		while (r == 0x0)  { r = rand() % 0x7 ;}
		printf("%d ", r) ;
	}
	printf("\n") ;

	return 0x0 ;
}

int lignes_colonnes () {

	int r = 0x0 ;

	for (int y = 0x0 ; y < 0xA ; y++) {
		for (int i = 0x0 ; i < 0xA ; i++) {
			r = rand() % 0x7 ;
			while (r == 0x0)  { r = rand() % 0x7 ;}
			printf("%d ", r) ;
		}
		printf("\n") ;
	}
	return 0x0 ;
}

int combien_de_6 () {

	int r = 0x0 ;
	int nb_six = 0x0 ;

	for (int y = 0x0 ; y < 0xA ; y++) {
		for (int i = 0x0 ; i < 0xA ; i++) {
			r = rand() % 0x7 ;
			while (r == 0x0)  { r = rand() % 0x7 ;}
			if (r == 0x6) nb_six += 1 ;
			printf("%d ", r) ;
		}
		printf("\n") ;
	}
	printf("\n") ;
	printf("le chiffre 6 apparait %d fois \n", nb_six) ;
	

	return 0x0 ;
}

// Exercice 7 : Suite de Fibonnaci (itérative)

int fibonnaci () {

	int n = 0 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &n) != 1 || n < 0) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;

	if (n == 0) {
		printf("0 \n") ;
		return 0 ;
	} else if (n == 1) {
		printf("1 \n") ;
		return 0 ;
	} else {
		int c0 = 0, c1 = 1, f = 0 ;
		for (int i = 0 ; i < n ; i++) {
			f = c0 + c1 ;
			c1 = c0 ;
			c0 = f ; 
		}
		printf ("\n%d", f) ; 
	 	return 0 ;
	} 
	
	return 0 ;

}

int bonus () {

	int n = 0 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &n) != 1 || n < 0) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;

	if (n == 0) {
		printf("0 \n") ;
		return 0 ;
	} else if (n == 1) {
		printf("1 \n") ;
		return 0 ;
	} else if (n == 2) {
		printf("1 \n") ;
		return 0 ;
	} else {
		int c0 = 0, c1 = 1, c2 = 1, f = 0 ;
		for (int i = 3 ; i <= n ; i++) {
			f = c0 + c1 + c2 ;
			c0 = c1 ;
			c1 = c2 ;
			c2 = f ; 
		}
		printf ("%d", f) ; 
	 	return 0 ;
	} 
	
	return 0 ;

}

// Exercice 8 : Boucles, flags, boucles imbriquées
	
int premier () {

	int n = 0 ;
	int premier = 1 ;

	printf("Entrez un entier : ") ;	
	if (scanf("%d", &n) != 1 || n < 0) {
		fprintf(stderr, "Erreur de saisie \n");
		return 1 ;
	} 
	getchar() ;


	while (premier) {
		if (n >= 2) {
			for (int i = 2 ; i <= n-1 ; i++) {
				if (n % i != 0) {
					premier = 0 ;
				} else {	
					printf("%d n'est pas premier", n) ;
					return 0 ;
				}
			}
		} else {	
			printf("%d n'est pas premier", n) ;
			return 0 ;
		}
	}
	
	printf("%d est premier", n) ;
	return 0 ;

}

int 100_premier () {

	

	for (int n = 1 ; n <= 100 ; n++) {
		
		int premier = 1 ;
	
		if (n >= 2) {
			for (int i = 2 ; i <= n-1 ; i++) {
				if (n % i == 0) {
					premier = 0 ; 
				} 
			}
		} 
		
		if (premier) {
			printf("%d, ", n) ; 
		}
	
	}
		
	return 0 ;

}


int main () {

	// Pour l'exercice 6 
	// srand(time(NULL)) ;	

	100_premier () ; 
	return 0 ;

}