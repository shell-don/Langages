!---------------------------- Auteur : Mathis Pigassou------------------------------!
!-  Exercice 4									   -!
!-  1. Ecrire un programme calculant l'aire et le volume d'un cercle de rayon r    -!
!-----------------------------------------------------------------------------------!


module ex4


	implicit none

	real, parameter :: pi = 3.14159265

contains

    	function aire_cercle(r) result(a)
        	
		real, intent(in) :: r
		real :: a
		a = pi*r*r

    	end function aire_cercle

	
	function volume_cercle(r) result(v)

		real, intent(in) :: r
		real :: v
	
		v = 4.0/3.0*pi*r**3

	end function volume_cercle


end module ex4

