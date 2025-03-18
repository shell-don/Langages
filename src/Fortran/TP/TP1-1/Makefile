# Paramètres
COMPILE=gfortran


# Édition de lien
TP1-1 : TP1-1.o mod_ex1.o mod_ex2.o mod_ex3.o mod_ex4.o mod_ex5.o mod_ex6.o mod_ex7.o mod_ex8.o mod_ex9.o
	$(COMPILE) -fcheck=all -o TP1-1 TP1-1.o mod_ex1.o mod_ex2.o mod_ex3.o mod_ex4.o mod_ex5.o mod_ex6.o mod_ex7.o mod_ex8.o mod_ex9.o


# Compilation 
TP1-1.o : TP1-1.f90 mod_ex1.o mod_ex2.o mod_ex3.o mod_ex4.o mod_ex5.o mod_ex6.o mod_ex7.o mod_ex8.o mod_ex9.o
	$(COMPILE) -fcheck=all -c TP1-1.f90
mod_ex1.o : mod_ex1.f90
	$(COMPILE) -fcheck=all -c mod_ex1.f90
mod_ex2.o : mod_ex2.f90
	$(COMPILE) -fcheck=all -c mod_ex2.f90
mod_ex3.o : mod_ex3.f90
	$(COMPILE) -fcheck=all -c mod_ex3.f90
mod_ex4.o : mod_ex4.f90
	$(COMPILE) -fcheck=all -c mod_ex4.f90
mod_ex5.o : mod_ex5.f90
	$(COMPILE) -fcheck=all -c mod_ex5.f90
mod_ex6.o : mod_ex6.f90
	$(COMPILE) -fcheck=all -c mod_ex6.f90
mod_ex7.o : mod_ex7.f90
	$(COMPILE) -fcheck=all -c mod_ex7.f90
mod_ex8.o : mod_ex8.f90
	$(COMPILE) -fcheck=all -c mod_ex8.f90
mod_ex9.o : mod_ex9.f90
	$(COMPILE) -fcheck=all -c mod_ex9.f90

# Nettoyage
clean :
	rm -f *.o *.mod

