!---------------------------- Auteur : Mathis Pigassou------------------------------!
!-  Exercice 1									   -!
!-  1. Ecrire, compiler, et exécuter un programme qui aﬃche Hello Word !     	   -!
!-----------------------------------------------------------------------------------!


module ex1

	implicit none

contains

	subroutine Bonjour

		write(6,*)"Hello World !"

	end subroutine Bonjour

end module ex1

