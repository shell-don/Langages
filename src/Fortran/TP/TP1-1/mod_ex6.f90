!---------------------------- Auteur : Mathis Pigassou------------------------------!
!-  Exercice 6									   -!
!-  1. Ecrire un programme permettant d’eﬀectuer le produit                	   -!
!-  de 2 matrices Aet B dont les dimensions sont stockées dans des constantes.     -!
!-----------------------------------------------------------------------------------!


module ex6


	implicit none

	integer, parameter :: m=3, n=2, o=2, p=3

contains

    	subroutine produit_matriciel(A, B, C)
        	
		real, dimension(1:m, 1:n), intent(inout) :: A
		real, dimension(1:o, 1:p), intent(inout) :: B
        	real, dimension(1:m, 1:p), intent(out) :: C
	
		integer :: i, j, k
		real :: coeff

        	print *, "rentrez les coefficients de A"
		do i=1,m
			do j=1,n
				print *, "A(",i,",",j,")="
				read *, A(i, j)
			end do
		end do

		print *, "rentrez les coefficients de B"
		do i=1,o
			do j=1,p
				print *, "B(",i,",",j,")="
				read *, B(i, j)
			end do
		end do

		C = 0.0

		do i=1,m
			do j=1,p
				!- calcul de C(i,j) = somme sur k des A(i,k)*B(k,j)
				coeff=0.0
				do k=1,n
					coeff=coeff+A(i, k)*B(k, j)
				end do
			C(i, j)=coeff
			end do
		end do

		print *, "Matrice C = A * B :"
		do i=1,m
			print *, C(i, :)
		end do

    	end subroutine produit_matriciel


end module ex6
