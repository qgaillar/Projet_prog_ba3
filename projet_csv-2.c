#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>


double calc_demi_petit_axe (double demi_grand_axe, double excentricite) {
	double b = demi_grand_axe*sqrt(1 - pow(excentricite, 2));
	return b;
}

void fichierCSV ( char* filename, int centre_x, int centre_y, double demi_grand_axe, double demi_petit_axe) {
	FILE * file = fopen(filename, "w+");
    for (int i = 0; i < 101; i++) {
			
		double coor_x = centre_x + demi_grand_axe*cos(M_PI*i/50);
		double coor_y = centre_y + demi_petit_axe *sin(M_PI*i/50);
                     
        fprintf(file, "%0.6f,%0.6f", coor_x, coor_y );    
        fprintf(file, "\n");
    }

    fclose(file);

}

int main(int argc, char * argv[]) {
	double demi_petit_axe_Mercure = calc_demi_petit_axe(451.5, 0.);
	double demi_petit_axe_Venus = calc_demi_petit_axe(451.5, 0.101);
	double demi_petit_axe_Terre = calc_demi_petit_axe(451.5, 0.101);
	double demi_petit_axe_Mars = calc_demi_petit_axe(227.84, 0.103 );
	double demi_petit_axe_Jupiter = calc_demi_petit_axe(451.5, 0.101);
	double demi_petit_axe_Saturne = calc_demi_petit_axe(451.5, 0.101);
	double demi_petit_axe_Uranus = calc_demi_petit_axe(451.5, 0.101);
	double demi_petit_axe_Neptune = calc_demi_petit_axe(451.5, 0.101);
	fichierCSV("planete_Mercure.csv", 5000, 5000, 451.5, demi_petit_axe_Mercure);
	fichierCSV("planete_Venus.csv", 5000, 5000, 451.5, demi_petit_axe_Venus);
	fichierCSV("planete_Terre.csv", 5000, 5000, 451.5, demi_petit_axe_Terre);
	fichierCSV("planete_Mars.csv", 5000, 5000, 227.84, demi_petit_axe_Mars);
	fichierCSV("planete_Jupiter.csv", 5000, 5000, 451.5, demi_petit_axe_Jupiter);
	fichierCSV("planete_Saturne.csv", 5000, 5000, 451.5, demi_petit_axe_Saturne);
	fichierCSV("planete_Uranus.csv", 5000, 5000, 451.5, demi_petit_axe_Uranus);
	fichierCSV("planete_Neptune.csv", 5000, 5000, 451.5, demi_petit_axe_Neptune);
	return 0; 

}
