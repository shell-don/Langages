#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// exe > .ps
// Commande de conversion d'un fichier .ps en .pdf avec ghostscript
// gs -sDEVICE=pdfwrite -o fichier_converti.pdf fichier.ps

// Turtle

double x = 5000, y = 5000 ; /* milieu de la page */
float dir ; 

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

void tourne_droite(float angle) {
    	dir = fmod(dir + angle, 4.0) ;
    	if (dir < 0) {
        	dir += 4.0 ;
    	}
}

void tourne_gauche(float angle) {
    	dir = fmod(dir + angle + 2.0, 4.0) ;
    	if (dir < 0) {
        	dir += 4.0 ;
    	}
}


// L-Systèmes

void trace_lsysteme(char *mot, float angle, int pas) {

	int longueur_mot = strlen(mot) ;

	for (int i = 0 ; i < longueur_mot ; i++) {
		if (mot[i] == 'A' || mot[i] == 'B') {
			avance (pas) ;
		} else if (mot[i] == 'g') {
			tourne_gauche(angle) ;
		} else if (mot[i] == 'd') {
			tourne_droite(angle) ;
		}
	}
} 

char *remplace_lettre(char *mot, char lettre, char *regle) {
    
	int longueur_mot = strlen(mot) ;
    	int longueur_regle = strlen(regle) ;

    	// Calcul de la taille nécessaire pour le nouveau mot
    	int nouvelle_taille = 0 ;
    	for (int i = 0 ; i < longueur_mot ; i++) {
        	if (mot[i] == lettre) {
            		nouvelle_taille += longueur_regle ; 
        	} else {
            	nouvelle_taille += 1 ; 
        	}
    	}

    	// Allocation dynamique pour le nouveau mot
    	char *nouveau_mot = malloc((nouvelle_taille + 1) * sizeof(char)) ;
    	if (nouveau_mot == NULL) {
        	perror("Erreur d'allocation mémoire") ;
        	exit(EXIT_FAILURE) ;
    	}

    	// Remplacement des lettres
    	int index = 0 ;
    	for (int i = 0 ; i < longueur_mot ; i++) {
        	if (mot[i] == lettre) {
            		strcpy(&nouveau_mot[index], regle) ;
            		index += longueur_regle ;
        	} else {
            		nouveau_mot[index] = mot[i] ;
            	index++ ;
        	}
    	}

 	nouveau_mot[index] = '\0' ;

    	return nouveau_mot ;
}

char *iter_remplace(char *mot, char lettre, char *regle, int n) {

	for (int i = 0 ; i < n ; i++) {
		mot = remplace_lettre(mot, lettre, regle) ;
	}

	return mot ;
}

int main () {

	printf("%%!postscript\n") ;
	printf("<< /PageSize [10000 10000] >> setpagedevice\n") ;
	trace_lsysteme(iter_remplace("AdAdAdA", 'A', "AgAAdAAdAdAgAgAAdAdAgAgAAgAAdA", 5), 1.0, 1) ;
	printf("showpage") ;

	return 0 ;

}