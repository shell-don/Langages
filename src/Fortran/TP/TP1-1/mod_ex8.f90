!---------------------------- Auteur : Mathis Pigassou------------------------------!
!-  Exercice 8									   -!
!-  1. Tri Bulle d'une liste de nombres réel.                                           -!
!-----------------------------------------------------------------------------------!


module ex8


	implicit none

contains

    	subroutine tri_bulle(tableau)
        	
		real, dimension(:), intent(inout) :: tableau
		integer :: i, tmp
		logical :: aucune_interversion
        	
		write(6,*) "Tableau avant le tri :"
		write(6,*) tableau

		bulle : do 
			aucune_interversion = .true.
        		do i=1,size(tableau)-1
				if (tableau(i) >= tableau(i+1)) then
					tmp = tableau(i)
					tableau(i) = tableau(i+1)
					tableau(i+1) = tmp
					aucune_interversion = .false.
				end if
			end do
			if (aucune_interversion) then
				exit bulle
			end if
		end do bulle
		
		write(6,*) "Tableau après le tri :"
		write(6,*) tableau

    	end subroutine tri_bulle


end module ex8