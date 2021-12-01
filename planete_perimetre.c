
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
	double v_planete;
	double revolution;

};


double calc_demi_petit_axe (double demi_grand_axe, double excentricite) {
	double b = demi_grand_axe*sqrt(1 - pow(excentricite, 2));
	
	return b;
}

double calc_perimetre (double demi_grand_axe, double demi_petit_axe) {
	double h = pow((demi_grand_axe - demi_petit_axe),2)/pow((demi_grand_axe + demi_petit_axe), 2);
	double perimetre = M_PI*(demi_grand_axe + demi_petit_axe)*(1 + (3*h/(10 + sqrt( 4 - 3*h))));
	
	return perimetre;
}

double v_planete (double perimetre, double revolution) {
	double vitesse_planete = perimetre / revolution ;
	
	return vitesse_planete;
}

//v_planete (calc_perimetre(double demi_grand_axe, double demi_petit_axe), revolution)

// ne pas oublier de rajouter le int iterations si ca marche pas

void fichierCSV ( char* filename, double centre_x, double centre_y, double demi_grand_axe, double demi_petit_axe, double revolution) {
	FILE * file = fopen(filename, "w+");
	
	//int delta_t = 20; //jours
	//iterations = revolution / delta_t
	int iterations = 5000;
	/*
	if (iterations % 2 == 0) iterations += 1;
	else ;
	*/
    for (int i = 0; i < iterations; i++) {
		double coor_x = centre_x + demi_grand_axe*cos(M_PI*i/(iterations/2));
		double coor_y = centre_y + demi_petit_axe *sin(M_PI*i/(iterations/2));	
		        
        fprintf(file, "%0.6f,%0.6f", coor_x, coor_y );    
        fprintf(file, "\n");
    }
    // la speed de nos planetes *v_planete(calc_perimetre(demi_grand_axe, demi_petit_axe), revolution)/delta_t 
    // et )*v_planete(calc_perimetre(demi_grand_axe, demi_petit_axe), revolution)/delta_t

    fclose(file);
}

int main(int argc, char * argv[]) {
	
	struct Planete Mercure = {"Mercure", 56.625*pow(10,3), 0.2589, 0, 0, 87.96};
	Mercure.demi_petit_axe = calc_demi_petit_axe(Mercure.demi_grand_axe, Mercure.excentricite);
	Mercure.v_planete = v_planete(calc_perimetre(Mercure.demi_grand_axe, Mercure.demi_petit_axe), Mercure.revolution);
	
	struct Planete Venus = {"Venus", 105.615*pow(10,3), 0.0051, 0, 0, 224.70};
	Venus.demi_petit_axe = calc_demi_petit_axe(Venus.demi_grand_axe, Venus.excentricite);
	Venus.v_planete = v_planete(calc_perimetre(Venus.demi_grand_axe, Venus.demi_petit_axe), Venus.revolution);
	
	struct Planete Terre = {"Terre", 150.5*pow(10,3), 0.101, 0, 0, 365.25};
	Terre.demi_petit_axe = calc_demi_petit_axe(Terre.demi_grand_axe, Terre.excentricite);
	Terre.v_planete = v_planete(calc_perimetre(Terre.demi_grand_axe, Terre.demi_petit_axe), Terre.revolution);
	
	struct Planete Mars = {"Mars", 227.84*pow(10,3), 0.103, 0, 0, 686.98};
	Mars.demi_petit_axe = calc_demi_petit_axe(Mars.demi_grand_axe, Mars.excentricite);
	Mars.v_planete = v_planete(calc_perimetre(Mars.demi_grand_axe, Mars.demi_petit_axe), Mars.revolution);
	
	struct Planete Jupiter = {"Jupiter", 778.345*pow(10,3), 0.0507, 0, 0, 4332.59};
	Jupiter.demi_petit_axe = calc_demi_petit_axe(Jupiter.demi_grand_axe, Jupiter.excentricite);
	Jupiter.v_planete = v_planete(calc_perimetre(Jupiter.demi_grand_axe, Jupiter.demi_petit_axe), Jupiter.revolution);
	
	struct Planete Saturne = {"Saturne", 1427.18*pow(10,3), 0.0593, 0, 0, 10759.23};
	Saturne.demi_petit_axe = calc_demi_petit_axe(Saturne.demi_grand_axe, Saturne.excentricite);
	Saturne.v_planete = v_planete(calc_perimetre(Saturne.demi_grand_axe, Saturne.demi_petit_axe), Saturne.revolution);
	
	struct Planete Uranus = {"Uranus", 2870.83*pow(10,3), 0.0482, 0, 0, 30685.4};
	Uranus.demi_petit_axe = calc_demi_petit_axe(Uranus.demi_grand_axe, Uranus.excentricite);
	Uranus.v_planete = v_planete(calc_perimetre(Uranus.demi_grand_axe, Uranus.demi_petit_axe), Uranus.revolution);
	
	struct Planete Neptune = {"Neptune", 4496.974*pow(10,3), 0.0098, 0, 0, 60216.8};
	Neptune.demi_petit_axe = calc_demi_petit_axe(Neptune.demi_grand_axe, Neptune.excentricite);
	Neptune.v_planete = v_planete(calc_perimetre(Neptune.demi_grand_axe, Neptune.demi_petit_axe), Neptune.revolution);
	
	double centre_x = 5.0e+6;
	double centre_y = 5.0e+6;

	fichierCSV("planete_Mercure1.csv", centre_x, centre_y, Mercure.demi_grand_axe, Mercure.demi_petit_axe, Mercure.revolution);
	fichierCSV("planete_Venus1.csv", centre_x, centre_y, Venus.demi_grand_axe, Venus.demi_petit_axe, Venus.revolution);
	fichierCSV("planete_Terre1.csv", centre_x, centre_y, Terre.demi_grand_axe, Terre.demi_petit_axe, Terre.revolution);
	fichierCSV("planete_Mars1.csv", centre_x, centre_y, Mars.demi_grand_axe, Mars.demi_petit_axe, Mars.revolution);
	fichierCSV("planete_Jupiter1.csv", centre_x, centre_y, Jupiter.demi_grand_axe, Jupiter.demi_petit_axe, Jupiter.revolution);
	fichierCSV("planete_Saturne1.csv", centre_x, centre_y, Saturne.demi_grand_axe, Saturne.demi_petit_axe, Saturne.revolution);
	fichierCSV("planete_Uranus1.csv", centre_x, centre_y, Uranus.demi_grand_axe, Uranus.demi_petit_axe, Uranus.revolution);
	fichierCSV("planete_Neptune1.csv", centre_x, centre_y, Neptune.demi_grand_axe, Neptune.demi_petit_axe, Neptune.revolution);
	
	return 0; 
}
