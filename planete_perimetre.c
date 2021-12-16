
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>
#define TRUE 1
#define FALSE 0

struct Planete {
	char* nom;
	double demi_grand_axe;
	double excentricite;
	double demi_petit_axe;
	double perimetre;
	double masse;
	int iterations;
	double vitesse_planete;
	int multiple;
	double rayon_collision;
	double * coord_x;
	double * coord_y;
	double cos_planete;
	double sin_planete;
};

struct Asteroids {
	char* nom;
	double masse;
	double rayon;
	double v_x;  //vitesse initiale de notre asteroid
	double v_y; 
	double x_init;
	double y_init;
	double coord_x;
	double coord_y;
	double jours;
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

void coordonnees_planetes_x (double * coor_planete_x,  double centre_x, double demi_grand_axe, double demi_petit_axe, int iterations, int multiple) {
	
	if (iterations % 2 != 0) iterations += 1;
	else ;
	for (int j = 0; j < multiple; j++) {
		for (int i = 0; i < iterations; i++) {
			coor_planete_x[i] = centre_x + demi_grand_axe*cos(M_PI*i/(iterations/2));	
					
		}
	}
}

void coordonnees_planetes_y (double * coor_planete_y, double centre_y, double demi_grand_axe, double demi_petit_axe, int iterations, int multiple) {
	
	if (iterations % 2 != 0) iterations += 1;
	else ;
	for (int j = 0; j < multiple; j++) {
		for (int i = 0; i < iterations; i++) {
			coor_planete_y[i] = centre_y + demi_petit_axe *sin(M_PI*i/(iterations/2));	
					
		}
	}

}

void fichierCSV ( char* filename, double * coor_x_planete, double * coor_y_planete, int iterations, int multiple) {
	FILE * file = fopen(filename, "w+");
	
	
	for (int j = 0; j < multiple; j++) {
		for (int i = 0; i < iterations; i++) {
					
			fprintf(file, "%0.6f,%0.6f", coor_x_planete[i], coor_y_planete[i] );    
			fprintf(file, "\n");
		}
	}

    fclose(file);
}

double calc_rayon_collision(double perimetre, int iteration) {
	double rayon_collision = perimetre / (double) (iteration * 2);
	
	return rayon_collision;
}

void fichierCSV_Rayon_Collision( char* filename, struct Planete *Planetes) {
	FILE * file = fopen(filename, "w+");

	for (int i = 0; i < 8; i++) {
	
		fprintf(file, "%0.6f", Planetes[i].rayon_collision);    
		fprintf(file, "\n");
	}

    fclose(file);
}

double coor_ast(char* coordonnee) {

    double n; 
    
	printf("Entrer une coordonnee %s entre 0 et 10^7:", coordonnee);     
    scanf(" %lf", &n);

    return n;
}

double calcul_V_0(char* coordonnee) {
	double n;
	 
	printf("Entrer une vitesse %s comprise entre -5 et 5 :", coordonnee);     
    scanf(" %lf", &n);

    return n;
}

double j_ast_pause () {
	
	double n; 
    
	printf("Entrer un nombre de jours avant le lancement de l'asteroide :");     
    scanf(" %lf", &n);

    return n;
}

void CSV_valeur_demandees (char * filename, double x_i, double y_i, double theta_i,double v_i, double jours) {
	FILE * file = fopen(filename, "w+");
	
	fprintf(file, "%0.6f, %0.6f, %0.6f, %0.6f, %0.6f", x_i, y_i, theta_i, v_i, jours);    

    fclose(file);
	
}
	 
void fichierCSV_Asteroid ( char* filename, struct Asteroids Asteroide, double coord_x_Asteroid[], double coord_y_Asteroid[], int j) {
	FILE * file = fopen(filename, "w+");

	for (int i = 0; i < j; i++) {
	
		fprintf(file, "%0.6f,%0.6f", coord_x_Asteroid[i], coord_y_Asteroid[i] );    
		fprintf(file, "\n");
	}

    fclose(file);
}



int main(int argc, char * argv[]) {
	
	/* nous avons décidés de compter en milliers de kilomètres c est pourquoi toutes nos valeurs de demi grand axe et la vistesse sont divisées par 1000
	 par rapport aux vraies valeurs, sinon notre plot aurait eu une taille de 10^10, ce qui n'aurait pas pu être possible étant donné que les int 
	 vont jusqu'à 2^31.  
	
	   pour les structures, nous avons initialisés les demis petits axes et les itérations à 0 car nous les calculons juste après avec les valeurs que 
	  nous avons implémentées.
	*/
	
	double centre_x = 5.0*pow(10,6);
	double centre_y = 5.0*pow(10,6);

	struct Planete Planetes[8];

	Planetes[0].nom = "Mercure";
	Planetes[0].demi_grand_axe = 56.625*pow(10,3);
	Planetes[0].excentricite = 0.2589;
	Planetes[0].demi_petit_axe = calc_demi_petit_axe(Planetes[0].demi_grand_axe, Planetes[0].excentricite);
	Planetes[0].perimetre = calc_perimetre(Planetes[0].demi_grand_axe, Planetes[0].demi_petit_axe);
	Planetes[0].masse = 33*pow(10,22);
	Planetes[0].vitesse_planete = 175.936;
	Planetes[0].iterations = calc_nb_iterations_selon_planete(Planetes[0].perimetre, Planetes[0].vitesse_planete);
	Planetes[0].multiple = 732.0;
	Planetes[0].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[0].demi_grand_axe, Planetes[0].demi_petit_axe), Planetes[0].iterations)/10;
	Planetes[0].coord_x = calloc(Planetes[0].iterations * Planetes[0].multiple, sizeof (double));;
	Planetes[0].coord_y = calloc(Planetes[0].iterations * Planetes[0].multiple, sizeof (double));;
	Planetes[0].cos_planete = 0;
	Planetes[0].sin_planete = 0;

	Planetes[1].nom = "Venus";
	Planetes[1].demi_grand_axe = 105.615*pow(10,3);
	Planetes[1].excentricite = 0.0051;
	Planetes[1].demi_petit_axe = calc_demi_petit_axe(Planetes[1].demi_grand_axe, Planetes[1].excentricite);
	Planetes[1].perimetre = calc_perimetre(Planetes[1].demi_grand_axe, Planetes[1].demi_petit_axe);
	Planetes[1].masse = 490*pow(10,22);
	Planetes[1].vitesse_planete = 126.062;
	Planetes[1].iterations = calc_nb_iterations_selon_planete(Planetes[1].perimetre, Planetes[1].vitesse_planete);
	Planetes[1].multiple = 274.0;
	Planetes[1].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[1].demi_grand_axe, Planetes[1].demi_petit_axe), Planetes[1].iterations)/10;
	Planetes[1].coord_x = calloc(Planetes[1].iterations * Planetes[1].multiple, sizeof (double));
	Planetes[1].coord_y = calloc(Planetes[1].iterations * Planetes[1].multiple, sizeof (double));
	Planetes[1].cos_planete = 0;
	Planetes[1].sin_planete = 0;

	Planetes[2].nom = "Terre";
	Planetes[2].demi_grand_axe = 150.5*pow(10,3);
	Planetes[2].excentricite = 0.101;
	Planetes[2].demi_petit_axe = calc_demi_petit_axe(Planetes[2].demi_grand_axe, Planetes[2].excentricite);
	Planetes[2].perimetre = calc_perimetre(Planetes[2].demi_grand_axe, Planetes[2].demi_petit_axe);
	Planetes[2].masse = 600*pow(10,22);
	Planetes[2].vitesse_planete = 107.243;
	Planetes[2].iterations = calc_nb_iterations_selon_planete(Planetes[2].perimetre, Planetes[2].vitesse_planete);
	Planetes[2].multiple = 164.0;
	Planetes[2].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[2].demi_grand_axe, Planetes[2].demi_petit_axe), Planetes[2].iterations)/10;
	Planetes[2].coord_x = calloc(Planetes[2].iterations * Planetes[2].multiple, sizeof (double));
	Planetes[2].coord_y = calloc(Planetes[2].iterations * Planetes[2].multiple, sizeof (double));
	Planetes[2].cos_planete = 0;
	Planetes[2].sin_planete = 0;

	Planetes[3].nom = "Mars";
	Planetes[3].demi_grand_axe = 227.84*pow(10,3);
	Planetes[3].excentricite = 0.103;
	Planetes[3].demi_petit_axe = calc_demi_petit_axe(Planetes[3].demi_grand_axe, Planetes[3].excentricite);
	Planetes[3].perimetre = calc_perimetre(Planetes[3].demi_grand_axe, Planetes[3].demi_petit_axe);
	Planetes[3].masse = 64 * pow(10,22);
	Planetes[3].vitesse_planete = 87.226;
	Planetes[3].iterations = calc_nb_iterations_selon_planete(Planetes[3].perimetre, Planetes[3].vitesse_planete);
	Planetes[3].multiple = 88.0;
	Planetes[3].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[3].demi_grand_axe, Planetes[3].demi_petit_axe), Planetes[3].iterations)/10;
	Planetes[3].coord_x = calloc(Planetes[3].iterations * Planetes[3].multiple, sizeof (double));
	Planetes[3].coord_y = calloc(Planetes[3].iterations * Planetes[3].multiple, sizeof (double));;
	Planetes[3].cos_planete = 0;
	Planetes[3].sin_planete = 0;

	Planetes[4].nom = "Jupiter";
	Planetes[4].demi_grand_axe = 778.345*pow(10,3);
	Planetes[4].excentricite = 0.0507;
	Planetes[4].demi_petit_axe = calc_demi_petit_axe(Planetes[4].demi_grand_axe, Planetes[4].excentricite);
	Planetes[4].perimetre = calc_perimetre(Planetes[4].demi_grand_axe, Planetes[4].demi_petit_axe);
	Planetes[4].masse = 190000 * pow(10,22);
	Planetes[4].vitesse_planete = 47.196;
	Planetes[4].iterations = calc_nb_iterations_selon_planete(Planetes[4].perimetre, Planetes[4].vitesse_planete);
	Planetes[4].multiple = 14.0;
	Planetes[4].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[4].demi_grand_axe, Planetes[4].demi_petit_axe), Planetes[4].iterations);
	Planetes[4].coord_x = calloc(Planetes[4].iterations * Planetes[4].multiple, sizeof (double));
	Planetes[4].coord_y = calloc(Planetes[4].iterations * Planetes[4].multiple, sizeof (double));
	Planetes[4].cos_planete = 0;
	Planetes[4].sin_planete = 0;

	Planetes[5].nom = "Saturne";
	Planetes[5].demi_grand_axe = 1427.18*pow(10,3);
	Planetes[5].excentricite = 0.0593;
	Planetes[5].demi_petit_axe = calc_demi_petit_axe(Planetes[5].demi_grand_axe, Planetes[5].excentricite);
	Planetes[5].perimetre = calc_perimetre(Planetes[5].demi_grand_axe, Planetes[5].demi_petit_axe);
	Planetes[5].masse = 57000 * pow(10,22);
	Planetes[5].vitesse_planete = 34.962;
	Planetes[5].iterations = calc_nb_iterations_selon_planete(Planetes[5].perimetre, Planetes[5].vitesse_planete);
	Planetes[5].multiple = 6.0;
	Planetes[5].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[3].demi_grand_axe, Planetes[3].demi_petit_axe), Planetes[3].iterations);
	Planetes[5].coord_x = calloc(Planetes[5].iterations * Planetes[5].multiple, sizeof (double));
	Planetes[5].coord_y = calloc(Planetes[5].iterations * Planetes[5].multiple, sizeof (double));
	Planetes[5].cos_planete = 0;
	Planetes[5].sin_planete = 0;

	Planetes[6].nom = "Uranus";
	Planetes[6].demi_grand_axe = 2870.83*pow(10,3);
	Planetes[6].excentricite = 0.0482;
	Planetes[6].demi_petit_axe = calc_demi_petit_axe(Planetes[6].demi_grand_axe, Planetes[6].excentricite);
	Planetes[6].perimetre = calc_perimetre(Planetes[6].demi_grand_axe, Planetes[6].demi_petit_axe);
	Planetes[6].masse = 8700 * pow(10,22);
	Planetes[6].vitesse_planete = 24.459;
	Planetes[6].iterations = calc_nb_iterations_selon_planete(Planetes[6].perimetre, Planetes[6].vitesse_planete);
	Planetes[6].multiple = 2.0;
	Planetes[6].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[6].demi_grand_axe, Planetes[6].demi_petit_axe), Planetes[6].iterations);
	Planetes[6].coord_x = calloc(Planetes[6].iterations * Planetes[6].multiple, sizeof (double));
	Planetes[6].coord_y = calloc(Planetes[6].iterations * Planetes[6].multiple, sizeof (double));
	Planetes[6].cos_planete = 0;
	Planetes[6].sin_planete = 0;

	Planetes[7].nom = "Neptune";
	Planetes[7].demi_grand_axe = 4496.975*pow(10,3);
	Planetes[7].excentricite = 0.0098;
	Planetes[7].demi_petit_axe = calc_demi_petit_axe(Planetes[7].demi_grand_axe, Planetes[7].excentricite);
	Planetes[7].perimetre = calc_perimetre(Planetes[7].demi_grand_axe, Planetes[7].demi_petit_axe);
	Planetes[7].masse = 10000 * pow(10,22);
	Planetes[7].vitesse_planete = 19.566;
	Planetes[7].iterations = calc_nb_iterations_selon_planete(Planetes[7].perimetre, Planetes[7].vitesse_planete);
	Planetes[7].multiple = 1.0;
	Planetes[7].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[7].demi_grand_axe, Planetes[7].demi_petit_axe), Planetes[7].iterations);
	Planetes[7].coord_x = calloc(Planetes[7].iterations * Planetes[7].multiple, sizeof (double));
	Planetes[7].coord_y = calloc(Planetes[7].iterations * Planetes[7].multiple, sizeof (double));
	Planetes[7].cos_planete = 0;
	Planetes[7].sin_planete = 0;

	struct Asteroids Asteroide;
	Asteroide.nom = "Asteroid";
	Asteroide.masse = pow(10, 18);
	Asteroide.rayon = 500;
	Asteroide.v_x = 0;
	Asteroide.v_y = 0; 
	Asteroide.x_init = 0;
	Asteroide.y_init = 0;
	Asteroide.jours = 0;

	double asteroide_x_init = coor_ast("x");
	
	
	while (asteroide_x_init > 10000000 ){
		asteroide_x_init = coor_ast("x");
		
	}
	
	double asteroide_y_init = coor_ast("y");
	
	while ((asteroide_x_init >1000000 && asteroide_x_init < 9000000) && (asteroide_y_init > 1000000 && asteroide_y_init < 9000000) == true) {
		printf("l'asteroide est trop proche des planetes, il faut prendre une valeur de y entre 0 et 1000000 ou 9000000 et 10000000\n");
		asteroide_y_init = coor_ast("y");
	}
	
	Asteroide.x_init = asteroide_x_init;
	Asteroide.y_init = asteroide_y_init;
	Asteroide.v_x = calcul_V_0("v_x_init");
	Asteroide.v_y = calcul_V_0("v_y_init");
	Asteroide.jours = j_ast_pause();
	
	
	 CSV_valeur_demandees("valeurs_init.csv", Asteroide.x_init, Asteroide.y_init, Asteroide.v_x, Asteroide.v_y, Asteroide.jours); 

	char * nom_fichier_csv[] = {"planete_Mercure.csv", "planete_Venus.csv", "planete_Terre.csv", "planete_Mars.csv", "planete_Jupiter.csv", "planete_Saturne.csv", "planete_Uranus.csv", "planete_Neptune.csv"};

	for (int i = 0; i < 8; i++) {
		coordonnees_planetes_x (Planetes[i].coord_x, centre_x, Planetes[i].demi_grand_axe, Planetes[i].demi_petit_axe, Planetes[i].iterations, Planetes[i].multiple);
		coordonnees_planetes_y (Planetes[i].coord_y, centre_y, Planetes[i].demi_grand_axe, Planetes[i].demi_petit_axe, Planetes[i].iterations, Planetes[i].multiple);
		fichierCSV(nom_fichier_csv[i], Planetes[i].coord_x, Planetes[i].coord_y, Planetes[i].iterations, Planetes[i].multiple);
		
	}

	fichierCSV_Rayon_Collision("Rayon_planete_collision.csv", Planetes);

	double * coord_x_Asteroid = calloc(60000, sizeof (double));
	double * coord_y_Asteroid = calloc(60000, sizeof (double));

	coord_x_Asteroid[0] = Asteroide.x_init;
	coord_y_Asteroid[0] = Asteroide.y_init;

	for (int j = 0; j < 60000; j++) {
		if (coord_x_Asteroid[j] > pow(10, 7) || coord_y_Asteroid[j] > pow(10, 7) || coord_x_Asteroid[j] < 0 || coord_y_Asteroid[j] < 0 ) {
			coord_x_Asteroid[j+1] = coord_x_Asteroid[j]; 
			coord_y_Asteroid[j+1] = coord_y_Asteroid[j];
			
		}
		else {
			double tmp = Asteroide.v_x * (j+1) ;
			coord_x_Asteroid[j + 1] = coord_x_Asteroid[j] + tmp;
			tmp = Asteroide.v_y * (j+1);
			coord_y_Asteroid[j + 1] = coord_y_Asteroid[j] + tmp;
			
		}
        

    }
    
	fichierCSV_Asteroid("Asteroide.csv", Asteroide, coord_x_Asteroid, coord_y_Asteroid,  60000); 
     
 	
	return 0; 

}
