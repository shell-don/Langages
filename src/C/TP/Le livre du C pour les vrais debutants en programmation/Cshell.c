/* accès au commande shell en C : system */

#include <stdio.h>
#include <stdlib.h>

int main () {
  system( "echo Hello World" ) ;
  return 0 ;
}

/* guillement obligatoire */
/* inconvénient : commande valable que sur les shell visé */