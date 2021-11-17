#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>


struct Planete {
	char* nom;
	double demi_grand_axe;
	double excentricite;
	double demi_petit_axe;
	double rayon;

};



double calc_demi_petit_axe (double demi_grand_axe, double excentricite) {
	double b = demi_grand_axe*sqrt(1 - pow(excentricite, 2));
	return b;
}

double calc_perimetre (double demi_grand_axe, double demi_petit_axe) {
	
	double h = pow((demi_grand_axe - demi_petit_axe),2)/pow((demi_grand_axe + demi_petit_axe), 2);
	double perimetre = M_PI*(demi_grand_axe + demi_petit_axe)*(1 + (3*h/(10 + sqrt( 4 - 3*h))));
	printf("%f\n", perimetre);
	return perimetre;
}

double calc_nb_iterations_selon_planete (double perimetre, double taille_planete) {
	int i = perimetre / taille_planete ;
	printf("%d\n", i);
	return i;
}


void fichierCSV ( char* filename, int centre_x, int centre_y, double demi_grand_axe, double demi_petit_axe) {
	FILE * file = fopen(filename, "w+");
    for (int i = 0; i < 401; i++) {
		
			
		double coor_x = centre_x + demi_grand_axe*cos(M_PI*i/200);
		double coor_y = centre_y + demi_petit_axe *sin(M_PI*i/200);
                     
        fprintf(file, "%0.6f,%0.6f", coor_x, coor_y );    
        fprintf(file, "\n");
    }

    fclose(file);

}

int main(int argc, char * argv[]) {
	
	struct Planete Mercure = {"Mercure", 56.625, 0.2589, 0};
	Mercure.demi_petit_axe = calc_demi_petit_axe(Mercure.demi_grand_axe, Mercure.excentricite);
	
	struct Planete Venus = {"Venus", 128.115, 0.0051, 0};
	Venus.demi_petit_axe = calc_demi_petit_axe(Venus.demi_grand_axe, Venus.excentricite);
	
	struct Planete Terre = {"Terre", 150.5, 0.101, 0};
	Terre.demi_petit_axe = calc_demi_petit_axe(Terre.demi_grand_axe, Terre.excentricite);
	
	struct Planete Mars = {"Mars", 227.84, 0.103, 0};
	Mars.demi_petit_axe = calc_demi_petit_axe(Mars.demi_grand_axe, Mars.excentricite);
	
	struct Planete Jupiter = {"Jupiter", 778.345, 0.0507, 0};
	Jupiter.demi_petit_axe = calc_demi_petit_axe(Jupiter.demi_grand_axe, Jupiter.excentricite);
	
	struct Planete Saturne = {"Saturne", 1427.18, 0.0593, 0};
	Saturne.demi_petit_axe = calc_demi_petit_axe(Saturne.demi_grand_axe, Saturne.excentricite);
	
	struct Planete Uranus = {"Uranus", 2870.83, 0.0482, 0};
	Uranus.demi_petit_axe = calc_demi_petit_axe(Uranus.demi_grand_axe, Uranus.excentricite);
	
	struct Planete Neptune = {"Neptune", 4496.975, 0.0098, 0};
	Neptune.demi_petit_axe = calc_demi_petit_axe(Neptune.demi_grand_axe, Neptune.excentricite);
	
	int centre_x = 5000;
	int centre_y = 5000;

	fichierCSV("planete_Mercure.csv", centre_x, centre_y, Mercure.demi_grand_axe, Mercure.demi_petit_axe);
	fichierCSV("planete_Venus.csv", centre_x, centre_y, Venus.demi_grand_axe, Venus.demi_petit_axe);
	fichierCSV("planete_Terre.csv", centre_x, centre_y, Terre.demi_grand_axe, Terre.demi_petit_axe);
	fichierCSV("planete_Mars.csv", centre_x, centre_y, Mars.demi_grand_axe, Mars.demi_petit_axe);
	fichierCSV("planete_Jupiter.csv", centre_x, centre_y, Jupiter.demi_grand_axe, Jupiter.demi_petit_axe);
	fichierCSV("planete_Saturne.csv", centre_x, centre_y, Saturne.demi_grand_axe, Saturne.demi_petit_axe);
	fichierCSV("planete_Uranus.csv", centre_x, centre_y, Uranus.demi_grand_axe, Uranus.demi_petit_axe);
	fichierCSV("planete_Neptune.csv", centre_x, centre_y, Neptune.demi_grand_axe, Neptune.demi_petit_axe);
	
	//int a = calc_nb_iterations_selon_planete(calc_perimetre(150.5, calc_demi_petit_axe(150.5, 0.101)), 3);
	

	return 0; 
}
