!---------------------------- Auteur : Mathis Pigassou------------------------------!
!-  Exercice 5									   -!
!-  1. Ecrire un programme qui lit une valeur réelle x                             -!
!-  calcule et écrit la valeur x/(1+x). Le cas x =−1 devra produire                -!
!-  un message d’erreur.                                                           -!
!-----------------------------------------------------------------------------------!


module ex5


	implicit none

contains

    	function f(x) result(f_x)
        	
		real, intent(in) :: x
        	real :: f_x 

        	if (x == -1.0) then
            		f_x = -1.
        	else
            		f_x = x/(1.+x)
        	end if

    	end function f


end module ex5

