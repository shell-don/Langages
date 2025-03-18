!---------------------------- Auteur : Mathis Pigassou------------------------------!
!-  1. Exercices de base du TP1. 	         				   -!
!-----------------------------------------------------------------------------------!


program TP1


	!- Noms des modules
	use ex1
	use ex2
	use ex3
	use ex4
	use ex5
	use ex6
	use ex7
	use ex8
	use ex9

	implicit none

	real :: x, y, r
	integer :: z
	real, dimension(1:3, 1:2) :: A
	real, dimension(1:2, 1:3) :: B
	real, dimension(1:3, 1:3) :: C
	real, dimension(5) :: tableau

	!- Exercice 1
	write(6,*)
	call Bonjour()
	write(6,*)

	!- Exerice 2 
	call resolv_systeme(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, x, y)
	write(6,*) "La solutions au système :"
	write(6,*) "	 x + 2y = 3"
	write(6,*) "	4x + 5y = 6"
	write(6,*) "est ... "
	write(6,*) "x =", x, "y =", y
	write(6,*)

	!- Exercice 3
	z = 5
	write(6,*) "Les", z, "premiers termes de la suite un+1 = 2un + 3 avec u0 = 1 sont :"
	call suite(n)
	write(6,*) "Les", z, "premiers termes de la suite de Fibonacci sont :"
	call fibonacci(z)
	write(6,*)

	!- Exercice 4
	r = 6.789
	write(6,*) "L'aire d'un cercle de rayon", r, "est :", aire_cercle(r)
	write(6,*) "Le volume d'un cercle de rayon", r, "est :", volume_cercle(r)
	write(6,*)

	!- Exercice 5
	write(6,*) "f(", x, ") =", f(x)
	write(6,*) "f(", y, ") =", f(y)
	write(6,*)

	!- Exercice 6
	!- call produit_matriciel(A, B, C)
	
	!- Exercice 7
	!- call inverse

	!- Exercice 8
	tableau = (/3.,5.,1.,2.,9./)
	call tri_bulle(tableau)

	!- Exercice 9
	call jeux

end program TP1

