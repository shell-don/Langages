!---------------------------- Auteur : Mathis Pigassou------------------------------!
!-  Exercice 7									   -!
!-  1. Ecrire un programme qui :                                                   -!
!-  d´eclare un tableau de 100 entiers            	                           -!
!-  aﬀecte aux éléements le valeurs 1,2,3,...,100                       	   -!
!-  lit deux valeurs entières comprises entre 1 et 100                             -!
!-  inverse l’ordre des éléments du tableau qui sont compris dans cet intervalle.  -!
!-----------------------------------------------------------------------------------!


module ex7


	implicit none

contains

    	subroutine inverse
        	
		integer :: i, m, n, milieu, taille_tableau
        	integer :: tmp
        	integer, dimension(100) :: tableau

		taille_tableau = 100
        	tableau = (/(i, i=1,taille_tableau)/)

		write(6,*) "Entrer m et n : inversera les éléments du tableau de m à n"
		read(5,*) m, n
	
		milieu = (m+n)/2
		!-     = (n+m)/2 si n+m pair, = (n+m-1)/2 sinon

		do i=m, milieu
			tmp = tableau(i)
			tableau(i) = tableau(n+m-i)
			tableau(n+m-i) = tmp
		end do

		write(6,*) tableau
		
    	end subroutine inverse


end module ex7

