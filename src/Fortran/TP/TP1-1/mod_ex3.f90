!---------------------------- Auteur : Mathis Pigassou------------------------------!
!-  Exercice 3									   -!
!-  1. Ecrire un programme qui lit une valeur entière n, puis calcule              -!
!-  et écrit les n premiers termes de la suite un+1 = 2un + 3, sachant que u0 = 1  -!
!-  2. Même question pour la suite de Fibonacci.                                   -!
!-----------------------------------------------------------------------------------!


module ex3


	implicit none

contains


	subroutine suite(n)

		integer, intent(in) :: n
		integer :: r, i
        	
		r = 1
		i = 1
		write(6,*) r
		do while (i <= n-1)
			r = 2*r + 3
			write(6,*) r
			i = i + 1
		end do

    	end subroutine suite


	subroutine fibonacci(n)

		integer, intent(in) :: n
		integer :: r0, r1, r2, i 

		r0 = 1
		r1 = 1
		i = 1
		write(6,*) r0
		write(6,*) r1
		do while (i <= n-2)	
			r2 = r1 + r0
			r0 = r1
			r1 = r2			
			i = i+1
			write(6,*) r2
		end do

	end subroutine fibonacci


end module ex3

