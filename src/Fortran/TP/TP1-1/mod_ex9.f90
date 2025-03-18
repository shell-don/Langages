!---------------------------- Auteur : Mathis Pigassou------------------------------!
!-  Exercice 9									   -!
!-  1. choisit un nombre au hasard entre 0 et 100                                  -!
!-  2. permet à l’utilisateur de jouer à retrouver ce nombre                       -!
!-----------------------------------------------------------------------------------!


module ex9


	implicit none

contains

    	subroutine jeux
        	
		real :: random
		integer :: nb_a_trouver
        	integer :: nb_propose

        	call random_number(random)
		nb_a_trouver = int(random*100+1)

		write(6,*) "!----------------------- Auteur : Mathis Pigassou------------------------!"
		write(6,*) "!-  Proposer un nombre entre 1 et 100                                	 -!"
		partie : do
			read(5,*) nb_propose
			if (nb_propose == nb_a_trouver) then
				write(6,*) "!-  Félicitation c'était bien", nb_a_trouver, "le nombre à trouver !         -!"
				write(6,*) "!------------------------------------------------------------------------!"
				exit partie
			else if (nb_propose < nb_a_trouver) then
				write(6,*) "!-  C'est plus                                                      	 -!"
			else 
				write(6,*) "!-  C'est moins                                                      	 -!"
			end if
		end do partie

    	end subroutine jeux


end module ex9