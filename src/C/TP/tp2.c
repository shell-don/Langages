#include <stdio.h>
#include <stdlib.h>

// Exercice 1 : création 

// L’objectif de ce TP est de se familiariser avec les tableaux et les pointeurs au travers de la manipulation de matrices.
// Utilisation Chatgpt : questions de compréhension pour création_dynamique, gestion de la mémoire à l'exercice 3 

int creation_statique () {

	int tab[2][2] ;

	for (int l = 0 ; l < 2 ; l++) {
		
		for (int c = 0 ; c < 2 ; c++) {
			printf("[%d][%d] = ", l, c) ;
			scanf("%d", &tab[l][c]) ;
		}
	
	}

	printf("\nLa matrice est : \n\n") ;

	for (int l = 0 ; l < 2 ; l++) {
		
		for (int c = 0 ; c < 2 ; c++) {
			printf("%d ", tab[l][c]) ;
		}
	
		printf("\n") ;
	}

	return 0 ;
	
}

int creation_dynamique () {

	// Les éléments sont stockés dans le heap de manière contiguë
	// Une case mémoire est "coupé" en 4, ici une case vaut 16 octets 
	// tab[0] = tab[0][0], tab[1] = tab[0][1], tab[2] = tab[1][0], tab[3] = tab[1][1]
	
	int *tab = malloc(2*2*sizeof(int)) ;

	for (int l = 0 ; l < 2 ; l++) {
		
		for (int c = 0 ; c < 2 ; c++) {
			printf("[%d][%d] = ", l, c) ;
			scanf("%d", &tab[(l*2)+c]) ;
		}
	
	}

	printf("\n") ;

	for (int l = 0 ; l < 2 ; l++) {
		
		for (int c = 0 ; c < 2 ; c++) {
			printf("%d ", tab[(l*2)+c] ) ;
		}
	
		printf("\n") ;
	}

	// Libération de La case mémoire
	free(tab) ;

	return 0 ;
	
}

int creation_dynamique2 () {

	// Les éléments sont stockés dans le heap de manière non contiguë
	// Ici **tab est un poiteur vers deux pointeurs
	// Ou, en représentation, tab est un Tableau contenant deux tableaux Indépendant 
	// tab[0] est l'adresse du premier tableau, tab[1] l'adresse du deuxième
	// tab[0][j] représente l'élément j du premier tableau
	
	int **tab = malloc(2*sizeof(int *)) ;
	for (int i = 0 ; i < 2 ; i++) {
		tab[i] = malloc(2*sizeof(int)) ;
	}

	for (int l = 0 ; l < 2 ; l++) {
		
		for (int c = 0 ; c < 2 ; c++) {
			printf("[%d][%d] = ", l, c) ;
			scanf("%d", &tab[l][c]) ;
		}
	
	}

	printf("\n") ;

	for (int l = 0 ; l < 2 ; l++) {
		
		for (int c = 0 ; c < 2 ; c++) {
			printf("%d ", tab[l][c] ) ;
		}
	
		printf("\n") ;
	}

	// Libération des deux pointeurs/Tableaux/Lignes
	for (int i = 0; i < 2; i++) {
       		free(tab[i]) ; 
    	}

	return 0 ;
	
}

// Exercice 2 : passage de paramètres 

int determinant_statique (int tab[2][2]) {
    return (tab[0][0] * tab[1][1] - tab[0][1] * tab[1][0]) ;
}

void transpose_statique (int tab[2][2]) {
	
	for (int l = 0 ; l < 2 ; l++) {
		for (int c = 0 ; c < 2 ; c++) {
			printf("%d ", tab[c][l]) ;
		}
	printf("\n") ; 
	}
}


int determinant_dynamique (int **tab) {
    return (tab[0][0] * tab[1][1] - tab[0][1] * tab[1][0]) ;
}

void transpose_dynamique (int **tab) {
	
	for (int l = 0 ; l < 2 ; l++) {
		for (int c = 0 ; c < 2 ; c++) {
			printf("%d ", tab[c][l]) ;
		}
	printf("\n") ; 
	}
}

// Exercice 3 : tableaux de structures 

typedef struct {
	char *nom ;
	char *filière ;
} ETUDIANT ;

int etudiant () {

	ETUDIANT **tab = malloc(2*sizeof(ETUDIANT *)) ;
	for (int i = 0 ; i < 2 ; i++) {
		tab[i] = malloc(2*sizeof(ETUDIANT)) ;
		for (int y = 0 ; y < 2 ; y++) {
			tab[i][y].nom = malloc(100 * sizeof(char)) ;
			tab[i][y].filière = malloc(100 * sizeof(char)) ;
		}
	}

	for (int l = 0 ; l < 2 ; l++) {
		
		for (int c = 0 ; c < 2 ; c++) {
			printf("quel est le nom de l'étudiant en [%d][%d] = ", l, c) ;
			// tab[l][c].nom est un pointeur donc & est inutile
			scanf("%s", tab[l][c].nom) ;
		}
	}  

	for (int l = 0 ; l < 2 ; l++) {
		
		for (int c = 0 ; c < 2 ; c++) {
			printf("quel est la filière de l'étudiant en [%d][%d] = ", l, c) ;
			// tab[l][c].filière est un pointeur donc & est inutile
			scanf("%s", tab[l][c].filière) ;
		}
	}

	printf("\nLa matrice est : \n\n") ;

	// affichage
	for (int l = 0 ; l < 2 ; l++) {
		for (int c = 0 ; c < 2 ; c++) {
			printf("%s:%s ", tab[l][c].nom, tab[l][c].filière) ;
		}
	
		printf("\n") ;
	}
	
	for (int l = 0; l < 2; l++) {
        	for (int c = 0; c < 2; c++) {
            		free(tab[l][c].nom) ;  
            		free(tab[l][c].filière) ;  
        	}
        	free(tab[l]);  
	}
    	free(tab) ;

	return 0 ;

}

void transpose_etudiant (ETUDIANT **tab) {
	
	for (int l = 0 ; l < 2 ; l++) {
		for (int c = 0 ; c < 2 ; c++) {
			printf("%s:%s ", tab[c][l].nom, tab[c][l].filière) ;
		}
	printf("\n") ; 
	}
}


int main () {
/*
	
	// Exercice 2 : allocation statique
	int tab[2][2] ;

	for (int l = 0 ; l < 2 ; l++) {
		
		for (int c = 0 ; c < 2 ; c++) {
			printf("[%d][%d] = ", l, c) ;
			scanf("%d", &tab[l][c]) ;
		}
	
	}  	
	printf("\nDeterminant : %d \nMatrice transposée : \n\n", determinant_statique (tab) ) ;
	transpose_statique (tab) ;

*/
/*

	// Exercice 2 : allocation dynamique
	int **tab = malloc(2*sizeof(int *)) ;
	for (int i = 0 ; i < 2 ; i++) {
		tab[i] = malloc(2*sizeof(int)) ;
	}

	for (int l = 0 ; l < 2 ; l++) {
		
		for (int c = 0 ; c < 2 ; c++) {
			printf("[%d][%d] = ", l, c) ;
			scanf("%d", &tab[l][c]) ;
		}
	
	}

	printf("\nDeterminant : %d \nMatrice transposée : \n\n", determinant_dynamique (tab) ) ;
	transpose_dynamique (tab) ;

	for (int i = 0; i < 2; i++) {
       		free(tab[i]) ; 
    	}

*/

	etudiant () ;

	return 0 ;
}