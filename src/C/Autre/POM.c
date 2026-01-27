#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#define BUFFER_SIZE 1024
#define ITERATION 64

void print_usage() {
    	
	printf("Usage : pom -e|-d -K <key_file_path> -k <key> -i <input_file> \n");
    	printf("Options :\n");
    	printf("     -e            Mode chiffrement \n") ;
    	printf("     -d            Mode déchiffrement \n") ;
    	printf("     -K            Spécifie le chemin du fichier clé \n") ;
   	printf("     -k            Spécifie la clé \n") ;
	printf("     -i            Fichier d'entrée \n") ;
}

unsigned char ROTR (unsigned char value, int n) {
    return (value >> n) | (value << (8 - n)) ;
}

unsigned char ROTL (unsigned char value, int n) {
    return (value << n) | (value >> (8 - n)) ;
}

void my_encrypt (char *input_file, char *key_file, char *key) {

	FILE *fin = fopen (input_file, "r+b") ;
	FILE *fkey = fopen (key_file, "rb") ;

	if (!fin) {
		perror("Erreur lors de l'ouverture du fichier d'entré") ;
		printf("Nom du fichier d'entrée : %s\n", input_file); 
		fclose (fkey) ; 
		exit(EXIT_FAILURE) ; 
	}
	
	if (!fkey) { 
		perror("Erreur lors de l'ouverture du fichier clé") ;  
		fclose (fin) ; 
		exit(EXIT_FAILURE) ; 
	}
	
	unsigned char buffer[BUFFER_SIZE] ;
	size_t fread_result, key_file_size, key_size ;
	unsigned long key_file_index = 0, key_index = 0 ;

	fseek (fkey, 0, SEEK_END) ;
	key_file_size = ftell (fkey) ;
	fseek (fkey, 0, SEEK_SET) ;
	key_size = strlen(key) ; 

	unsigned char *key_file2 = malloc(key_file_size) ;
    	if (!key) {
        	perror("Erreur d'allocation mémoire") ;
        	fclose(fkey) ;
		fclose(fin) ;
        	exit(EXIT_FAILURE) ;
    	}

    	fread(key_file2, 1, key_file_size, fkey) ;
   	fclose(fkey) ;

	while ( (fread_result = fread (buffer, 1, BUFFER_SIZE, fin)) > 0 ) {

		for (int iteration = 0 ; iteration < ITERATION ; iteration++) {               		key_file_index = 0 ;
            		key_index = 0 ;
			
			for (int i = 0 ; i < fread_result ; i++) {
			
				key[key_index] = ~(ROTR(key_file2[key_file_index], 4) ^ ~key_file2[key_file_index]) ^ ROTR(~ROTR(key[key_index], 3), 2) ^ ~(~key[key_index] ^ key_file2[key_file_index]) ^ ROTR(~key[key_index], 5) ; 
				key_file2[key_file_index] = ROTR(~(key_file2[key_file_index]), 4) ^ ~(~(key[key_index] ^ ROTL(~key[key_index], 2)) ^ ~ROTL(key_file2[key_file_index], 3) ^ ~(key_file2[key_file_index] ^ ROTR(key[key_index], 4))) ; 
				buffer[i] = ~(ROTR(key_file2[key_file_index], 3) ^ buffer[i]) ^ ROTL(key[key_index], 6) ;
				key_file_index = (key_file_index + 1) % key_file_size ;
				key_index = (key_index + 1) % key_size ;
		
			}
		}
		fseek (fin, -fread_result, SEEK_CUR) ;
		fwrite (buffer, 1, fread_result, fin) ;
	}
	
	fclose (fin) ; 
	fclose (fkey) ; 
	free (key_file2) ;
}
	
void my_decrypt (char *input_file, char *key_file, char *key) {

	FILE *fin = fopen (input_file, "r+b") ;
	FILE *fkey = fopen (key_file, "rb") ;

	if (!fin) {
		perror("Erreur lors de l'ouverture du fichier d'entré") ;
		printf("Nom du fichier d'entrée : %s\n", input_file); 
		fclose (fkey) ; 
		exit(EXIT_FAILURE) ; 
	}
	
	if (!fkey) { 
		perror("Erreur lors de l'ouverture du fichier clé") ;  
		fclose (fin) ; 
		exit(EXIT_FAILURE) ; 
	}
	
	unsigned char buffer[BUFFER_SIZE] ;
	size_t fread_result, key_file_size, key_size ;
	unsigned long key_file_index = 0, key_index = 0 ;

	fseek (fkey, 0, SEEK_END) ;
	key_file_size = ftell (fkey) ;
	fseek (fkey, 0, SEEK_SET) ;
	key_size = strlen(key) ; 

	unsigned char *key_file2 = malloc(key_file_size) ;
    	if (!key) {
        	perror("Erreur d'allocation mémoire") ;
        	fclose(fkey) ;
		fclose(fin) ;
        	exit(EXIT_FAILURE) ;
    	}

    	fread(key_file2, 1, key_file_size, fkey) ;
   	fclose(fkey) ;

	while ( (fread_result = fread (buffer, 1, BUFFER_SIZE, fin)) > 0 ) {

		for (int iteration = 0 ; iteration < ITERATION ; iteration++) {                				key_file_index = 0 ;
            		key_index = 0 ;

			for (int i = 0 ; i < fread_result ; i++) {
			
			 	key[key_index] = ~(ROTR(key_file2[key_file_index], 4) ^ ~key_file2[key_file_index]) ^ ROTR(~ROTR(key[key_index], 3), 2) ^ ~(~key[key_index] ^ key_file2[key_file_index]) ^ ROTR(~key[key_index], 5) ; 
				key_file2[key_file_index] = ROTR(~(key_file2[key_file_index]), 4) ^ ~(~(key[key_index] ^ ROTL(~key[key_index], 2)) ^ ~ROTL(key_file2[key_file_index], 3) ^ ~(key_file2[key_file_index] ^ ROTR(key[key_index], 4))) ;
				buffer[i] = ~(buffer[i]^ROTL(key[key_index], 6)) ^ ROTR(key_file2[key_file_index], 3) ;
				key_file_index = (key_file_index + 1) % key_file_size ;
				key_index = (key_index + 1) % key_size ;
			}
		}
		fseek (fin, -fread_result, SEEK_CUR) ;
		fwrite (buffer, 1, fread_result, fin) ;
	}
	
	fclose (fin) ; 
	fclose (fkey) ; 
	free (key_file2) ;
}


int main(int argc, char *argv[]) {
    
	int opt ;
   	int encrypt_mode = 0, decrypt_mode = 0 ;
    	char *key_file = NULL ;
    	char *key = NULL ;
	char *input_file = NULL ;
 
   	while ((opt = getopt(argc, argv, "edK:k:i:")) != -1) {
      	 	switch (opt) {
            	
		case 'e':
                	encrypt_mode = 1 ;
                	break ;
            	case 'd':
                	decrypt_mode = 1 ;
               		break ;
            	case 'K':
                	key_file = optarg ;
                	break ;
            	case 'k':
                	key = optarg ;
                	break ;
		case 'i' : 
			input_file = optarg ;
			break ;
            	default: /* '?' */
                	print_usage() ;
                	exit(EXIT_FAILURE) ;
        	}
    	}


    	if ((encrypt_mode && decrypt_mode) || (!encrypt_mode && !decrypt_mode)) {
        	print_usage() ;
        	exit(EXIT_FAILURE) ;
    	}
    	if (!input_file || !key_file || !key) {
        	fprintf(stderr, "Erreur : paramètres obligatoires manquants.\n") ;
        	print_usage() ;
        	exit(EXIT_FAILURE) ;
    	}

    	
    	if (encrypt_mode) {
        	my_encrypt(input_file, key_file, key) ;
    	} else if (decrypt_mode) {
        	my_decrypt(input_file, key_file, key) ;
    	}


    	return 0 ;
}