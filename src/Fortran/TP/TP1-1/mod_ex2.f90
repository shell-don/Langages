!---------------------------- Auteur : Mathis Pigassou------------------------------!
!-  Exercice 2									   -!
!-  1. Ecrire un programme permettant de résoudre un systèeme                      -!
!-  de 2 équations à 2 inconnues.                                                  -!
!-----------------------------------------------------------------------------------!


module ex2


	implicit none

contains

    	subroutine resolv_systeme(a, b, c, d, e, f, x, y)
        	
		real, intent(in) :: a, b, c, d, e, f
        	real, intent(out) :: x, y
        	real :: det

        	det = a * e - b * d

        	if (det == 0.0) then
            		print *, "Système sans solution ou avec une infinité de solutions"
            		x = 0.0
            		y = 0.0
        	else
            		x = (c * e - b * f) / det
            		y = (a * f - c * d) / det
        	end if

    	end subroutine resolv_systeme


end module ex2
