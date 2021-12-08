
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
	int iterations;
	double vitesse_planete;
	int multiple;
	double rayon_collision;

};


double calc_demi_petit_axe (double demi_grand_axe, double excentricite) {
	double b = demi_grand_axe*sqrt(1 - pow(excentricite, 2));
	
	return b;
}

double calc_perimetre (double demi_grand_axe, double demi_petit_axe) {
	double h = pow((demi_grand_axe - demi_petit_axe),2)/pow((demi_grand_axe + demi_petit_axe), 2);
	double perimetre = M_PI*(demi_grand_axe + demi_petit_axe)*(1 + (3*h/(10 + sqrt( 4 - 3*h))));
	
	// il s'agit d'une formule pour approximer le périmetre ce qui explique que nous n'avons pas les distances réelles car 
	// elle a un écart-type de + ou - 0.01 par rapport à la vraie valeur
	
	return perimetre;
}	

double calc_nb_iterations_selon_planete (double perimetre, double v_planete) {
	int t_revolution = (perimetre / v_planete)/24; 
	
	// pour avoir des jours (qui eux aussi ne sont pas les vrais temps de révolution à cause de l'approximation du périmètre 
	// et du fait qu'il nous faut un nombre entier pour faire des itérations par rapport à 2*pi)
	
	return t_revolution;
}


void fichierCSV ( char* filename, double centre_x, double centre_y, double demi_grand_axe, double demi_petit_axe, int iterations, int multiple) {
	FILE * file = fopen(filename, "w+");
	
	if (iterations % 2 != 0) iterations += 1;
	else ;
	for (int j = 0; j < multiple; j++) {
		for (int i = 0; i < iterations; i++) {
			double coor_x = centre_x + demi_grand_axe*cos(M_PI*i/(iterations/2));
			double coor_y = centre_y + demi_petit_axe *sin(M_PI*i/(iterations/2));	
					
			fprintf(file, "%0.6f,%0.6f", coor_x, coor_y );    
			fprintf(file, "\n");
		}
	}

    fclose(file);
}

double calc_rayon_collision(double perimetre, int iteration) {
	double rayon_collision = perimetre / (double) (iteration * 2);

	return rayon_collision;
}

int main(int argc, char * argv[]) {
	
	/* nous avons décidés de compter en milliers de kilomètres c est pourquoi toutes nos valeurs de demi grand axe et la vistesse sont divisées par 1000
	 par rapport aux vraies valeurs, sinon notre plot aurait eu une taille de 10^10, ce qui n'aurait pas pu être possible étant donné que les int 
	 vont jusqu'à 2^31.  
	
	   pour les structures, nous avons initialisés les demis petits axes et les itérations à 0 car nous les calculons juste après avec les valeurs que 
	  nous avons implémentées.
	*/
	
	struct Planete Mercure = {"Mercure", 56.625*pow(10,3), 0.2589, 0, 0, 175.936, 732};
	Mercure.demi_petit_axe = calc_demi_petit_axe(Mercure.demi_grand_axe, Mercure.excentricite);
	Mercure.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Mercure.demi_grand_axe, Mercure.demi_petit_axe), Mercure.vitesse_planete);
	Mercure.rayon_collision = calc_rayon_collision(calc_perimetre(Mercure.demi_grand_axe, Mercure.demi_petit_axe), Mercure.iterations);
	printf("%f\n", calc_perimetre(Mercure.demi_grand_axe, Mercure.demi_petit_axe));
	printf("%f\n", Mercure.rayon_collision);
	// le perimetre de Mercure étant calculé à l'aide du demi-grand axe et du demi-petit axe, nous avons un périmètre assez éloigné de la valeur réelle
	
	struct Planete Venus = {"Venus", 105.615*pow(10,3), 0.0051, 0, 0, 126.062, 274};
	Venus.demi_petit_axe = calc_demi_petit_axe(Venus.demi_grand_axe, Venus.excentricite);
	Venus.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Venus.demi_grand_axe, Venus.demi_petit_axe), Venus.vitesse_planete);
	
	struct Planete Terre = {"Terre", 150.5*pow(10,3), 0.101, 0, 0, 107.243, 164};
	Terre.demi_petit_axe = calc_demi_petit_axe(Terre.demi_grand_axe, Terre.excentricite);
	Terre.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Terre.demi_grand_axe, Terre.demi_petit_axe), Terre.vitesse_planete);
	
	struct Planete Mars = {"Mars", 227.84*pow(10,3), 0.103, 0, 0, 87.226, 88};
	Mars.demi_petit_axe = calc_demi_petit_axe(Mars.demi_grand_axe, Mars.excentricite);
	Mars.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Mars.demi_grand_axe, Mars.demi_petit_axe), Mars.vitesse_planete);
	
	struct Planete Jupiter = {"Jupiter", 778.345*pow(10,3), 0.0507, 0, 0, 47.196, 14};
	Jupiter.demi_petit_axe = calc_demi_petit_axe(Jupiter.demi_grand_axe, Jupiter.excentricite);
	Jupiter.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Jupiter.demi_grand_axe, Jupiter.demi_petit_axe), Jupiter.vitesse_planete);
	
	struct Planete Saturne = {"Saturne", 1427.18*pow(10,3), 0.0593, 0, 0, 34.962, 6};
	Saturne.demi_petit_axe = calc_demi_petit_axe(Saturne.demi_grand_axe, Saturne.excentricite);
	Saturne.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Saturne.demi_grand_axe, Saturne.demi_petit_axe), Saturne.vitesse_planete);
	
	struct Planete Uranus = {"Uranus", 2870.83*pow(10,3), 0.0482, 0, 0, 24.459, 2};
	Uranus.demi_petit_axe = calc_demi_petit_axe(Uranus.demi_grand_axe, Uranus.excentricite);
	Uranus.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Uranus.demi_grand_axe, Uranus.demi_petit_axe), Uranus.vitesse_planete);
	
	struct Planete Neptune = {"Neptune", 4496.975*pow(10,3), 0.0098, 0, 0, 19.566, 1};
	Neptune.demi_petit_axe = calc_demi_petit_axe(Neptune.demi_grand_axe, Neptune.excentricite);
	Neptune.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Neptune.demi_grand_axe, Neptune.demi_petit_axe), Neptune.vitesse_planete);
	
	double centre_x = 5.0e+6;
	double centre_y = 5.0e+6;

	fichierCSV("planete_Mercure.csv", centre_x, centre_y, Mercure.demi_grand_axe, Mercure.demi_petit_axe, Mercure.iterations, Mercure.multiple);
	fichierCSV("planete_Venus.csv", centre_x, centre_y, Venus.demi_grand_axe, Venus.demi_petit_axe, Venus.iterations, Venus.multiple);
	fichierCSV("planete_Terre.csv", centre_x, centre_y, Terre.demi_grand_axe, Terre.demi_petit_axe, Terre.iterations, Terre.multiple);
	fichierCSV("planete_Mars.csv", centre_x, centre_y, Mars.demi_grand_axe, Mars.demi_petit_axe, Mars.iterations, Mars.multiple);
	fichierCSV("planete_Jupiter.csv", centre_x, centre_y, Jupiter.demi_grand_axe, Jupiter.demi_petit_axe, Jupiter.iterations, Jupiter.multiple);
	fichierCSV("planete_Saturne.csv", centre_x, centre_y, Saturne.demi_grand_axe, Saturne.demi_petit_axe, Saturne.iterations, Saturne.multiple);
	fichierCSV("planete_Uranus.csv", centre_x, centre_y, Uranus.demi_grand_axe, Uranus.demi_petit_axe, Uranus.iterations, Uranus.multiple);
	fichierCSV("planete_Neptune.csv", centre_x, centre_y, Neptune.demi_grand_axe, Neptune.demi_petit_axe, Neptune.iterations, Neptune.multiple);
	
	
	return 0; 
}
