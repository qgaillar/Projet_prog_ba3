
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
	double V0;  //vitesse initiale de notre asteroid
	double theta; //angle initiale de direction asteroid, en °
	double x_init;
	double y_init;
	double coord_x;
	double coord_y;
};

struct Etoile {
	char * nom;
	double masse;
	double coord_x;
	double coord_y;
	double cos_etoile;
	double sin_etoile;
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

double coor_ast(char* coordonnee)
{
    double n; 
    
	printf("Entrer une coordonnee %s entre 0 et 10^7:", coordonnee);     
    scanf(" %lf", &n);

    return n;
}

double Fg(double masse, double masse_asteroide, double x_Asteroid_t_reel, double y_Asteroid_t_reel, double x_planete, double y_planete){
	double G = 6.67*pow(10, -11);
    double delta_x = x_Asteroid_t_reel - x_planete;
    double delta_y = y_Asteroid_t_reel - y_planete;
    double dist = pow(pow(delta_x,2) + pow(delta_y,2), 1/2);
    double Force_gravitationnelle = (G * masse * masse_asteroide) / pow((dist * 10e3),2);  //10e3 = conversion en mètres
    return Force_gravitationnelle;
}


double Fg_totale_x(double x_Asteroid_crash_test, double y_Asteroid_crash_test, int i, struct Asteroids Asteroid, struct Planete Planetes[], struct Etoile Soleil) {
	double Fg_tot_x = 0;
	for (int j = 0; j < 8; j++) {
		Planetes[j].cos_planete = fabs(x_Asteroid_crash_test - Planetes[0].coord_x[i]) / pow((x_Asteroid_crash_test - pow(Planetes[0].coord_x[i],2) + (y_Asteroid_crash_test - pow(Planetes[0].coord_y[i],2))), 1/2);
		Fg_tot_x += Fg(Planetes[j].masse, Asteroid.masse, x_Asteroid_crash_test, y_Asteroid_crash_test, Planetes[j].coord_x[i], Planetes[j].coord_y[i]) * Planetes[j].cos_planete;
	}
	Soleil.cos_etoile = fabs(x_Asteroid_crash_test - Soleil.coord_x) / pow((x_Asteroid_crash_test - pow(Soleil.coord_x,2) + (y_Asteroid_crash_test - pow(Soleil.coord_y,2))), 1/2);
	Fg_tot_x += Fg(Soleil.masse, Asteroid.masse, x_Asteroid_crash_test, y_Asteroid_crash_test, Soleil.coord_x, Soleil.coord_y) * Soleil.cos_etoile;
	return Fg_tot_x;
}




double Fg_totale_y(double x_Asteroid_crash_test, double y_Asteroid_crash_test, int i, struct Asteroids Asteroid, struct Planete Planetes[], struct Etoile Soleil) {
	double Fg_tot_y = 0;
	for (int j = 0; j < 8; j++) {
		Planetes[j].sin_planete = fabs(y_Asteroid_crash_test - Planetes[0].coord_y[i]) / pow((x_Asteroid_crash_test - pow(Planetes[0].coord_x[i],2) + (y_Asteroid_crash_test - pow(Planetes[0].coord_y[i],2))), 1/2);
		Fg_tot_y += Fg(Planetes[j].masse, Asteroid.masse, x_Asteroid_crash_test, y_Asteroid_crash_test, Planetes[j].coord_x[i], Planetes[j].coord_y[i]) * Planetes[j].sin_planete;
	}
	Soleil.sin_etoile = fabs(y_Asteroid_crash_test - Soleil.coord_y) / pow((x_Asteroid_crash_test - pow(Soleil.coord_x,2) + (y_Asteroid_crash_test - pow(Soleil.coord_y,2))), 1/2);
	Fg_tot_y += Fg(Soleil.masse, Asteroid.masse, x_Asteroid_crash_test, y_Asteroid_crash_test, Soleil.coord_x, Soleil.coord_y) * Soleil.sin_etoile;
	return Fg_tot_y;
}


void fichierCSV_Asteroid ( char* filename, int iterations,  struct Asteroids Asteroid, double coord_x_Asteroid[], double coord_y_Asteroid[], int j) {
	FILE * file = fopen(filename, "w+");
	
	if (iterations % 2 != 0) iterations += 1;
	else ;

	for (int i = 0; i < j; i++) {
	
		fprintf(file, "%0.6f,%0.6f", coord_x_Asteroid[i], coord_y_Asteroid[i] );    
		fprintf(file, "\n");
	}

    fclose(file);
}




/*
double Fg_totale_x(x_Asteroid_crash_test, y_Asteroid_crash_test, i){

    double cos_Mercure = (fabs(x_Asteroid_crash_test - Mercure.coord_x[i]) / pow((x_Asteroid_crash_test - pow(Mercure.coord_x[i],2) + (y_Asteroid_crash_test - pow(Mercure.coord_y[i],2))), 1/2);
    double cos_Venus = (abs(x_Asteroid_crash_test - Venus.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Venus.coord_x[i])**2 + (y_Asteroid_crash_test - Venus.coord_y[i])**2));
    double cos_Terre = (abs(x_Asteroid_crash_test - Terre.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Terre.coord_x[i])**2 + (y_Asteroid_crash_test - Terre.coord_y[i])**2));
    double cos_Mars = (abs(x_Asteroid_crash_test - Mars.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Mars.coord_x[i])**2 + (y_Asteroid_crash_test - Mars.coord_y[i])**2));
    double cos_Jupiter = (abs(x_Asteroid_crash_test - Jupiter.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Jupiter.coord_x[i])**2 + (y_Asteroid_crash_test - Jupiter.coord_y[i])**2));
    double cos_Saturne = (abs(x_Asteroid_crash_test - Saturne.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Saturne.coord_x[i])**2 + (y_Asteroid_crash_test - Saturne.coord_y[i])**2));
    double cos_Uranus = (abs(x_Asteroid_crash_test - Uranus.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Uranus.coord_x[i])**2 + (y_Asteroid_crash_test - Uranus.coord_y[i])**2));
    double cos_Neptune = (abs(x_Asteroid_crash_test - Neptune.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Neptune.coord_x[i])**2 + (y_Asteroid_crash_test - Neptune.coord_y[i])**2));
    double cos_Soleil = (abs(x_Asteroid_crash_test - Soleil.coord_x) / np.sqrt((x_Asteroid_crash_test - Soleil.coord_x)**2 + (y_Asteroid_crash_test - Soleil.coord_y)**2));

    Fg_tot_x = (
        Fg(Mercure.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Mercure.coord_x[i], Mercure.coord_y[i]) * cos_Mercure + //pb avec Fg qui génère 1705 valeurs d'un coup 
        Fg(Venus.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Venus.coord_x[i], Venus.coord_y[i]) * cos_Venus +
        Fg(Terre.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Terre.coord_x[i], Terre.coord_y[i]) * cos_Terre +
        Fg(Mars.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Mars.coord_x[i], Mars.coord_y[i]) * cos_Mars +
        Fg(Jupiter.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Jupiter.coord_x[i], Jupiter.coord_y[i]) * cos_Jupiter +
        Fg(Saturne.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Saturne.coord_x[i], Saturne.coord_y[i]) * cos_Saturne +
        Fg(Uranus.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Uranus.coord_x[i], Uranus.coord_y[i]) * cos_Uranus +
        Fg(Neptune.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Neptune.coord_x[i], Neptune.coord_y[i]) * cos_Neptune +
        Fg(Soleil.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Soleil.coord_x, Soleil.coord_y) * cos_Soleil
    )
    return Fg_tot_x
}

def Fg_totale_y(x_Asteroid_crash_test, y_Asteroid_crash_test, i):

    sin_Mercure = (abs(y_Asteroid_crash_test - Mercure.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Mercure.coord_x[i])**2 + (y_Asteroid_crash_test - Mercure.coord_y[i])**2))
    sin_Venus = (abs(y_Asteroid_crash_test - Venus.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Venus.coord_x[i])**2 + (y_Asteroid_crash_test - Venus.coord_y[i])**2))
    sin_Terre = (abs(y_Asteroid_crash_test - Terre.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Terre.coord_x[i])**2 + (y_Asteroid_crash_test - Terre.coord_y[i])**2))
    sin_Mars = (abs(y_Asteroid_crash_test - Mars.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Mars.coord_x[i])**2 + (y_Asteroid_crash_test - Mars.coord_y[i])**2))
    sin_Jupiter = (abs(y_Asteroid_crash_test - Jupiter.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Jupiter.coord_x[i])**2 + (y_Asteroid_crash_test - Jupiter.coord_y[i])**2))
    sin_Saturne = (abs(y_Asteroid_crash_test - Saturne.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Saturne.coord_x[i])**2 + (y_Asteroid_crash_test - Saturne.coord_y[i])**2))
    sin_Uranus = (abs(y_Asteroid_crash_test - Uranus.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Uranus.coord_x[i])**2 + (y_Asteroid_crash_test - Uranus.coord_y[i])**2))
    sin_Neptune = (abs(y_Asteroid_crash_test - Neptune.coord_y[i]) / np.sqrt((x_Asteroid_crash_test - Neptune.coord_x[i])**2 + (y_Asteroid_crash_test - Neptune.coord_y[i])**2))
    sin_Soleil = (abs(y_Asteroid_crash_test - Soleil.coord_y) / np.sqrt((x_Asteroid_crash_test - Soleil.coord_y)**2 + (y_Asteroid_crash_test - Soleil.coord_y)**2))


    Fg_tot_y = (
        Fg(Mercure.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Mercure.coord_x[i], Mercure.coord_y[i]) * sin_Mercure +
        Fg(Venus.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Venus.coord_x[i], Venus.coord_y[i]) * sin_Venus +
        Fg(Terre.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Terre.coord_x[i], Terre.coord_y[i]) * sin_Terre +
        Fg(Mars.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Mars.coord_x[i], Mars.coord_y[i]) * sin_Mars +
        Fg(Jupiter.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Jupiter.coord_x[i], Jupiter.coord_y[i]) * sin_Jupiter +
        Fg(Saturne.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Saturne.coord_x[i], Saturne.coord_y[i]) * sin_Saturne +
        Fg(Uranus.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Uranus.coord_x[i], Uranus.coord_y[i]) * sin_Uranus +
        Fg(Neptune.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Neptune.coord_x[i], Neptune.coord_y[i]) * sin_Neptune +
        Fg(Soleil.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Soleil.coord_x, Soleil.coord_y) * sin_Soleil
    )
    return Fg_tot_y


coord_x_Asteroid = [asteroide_x_init]
coord_y_Asteroid = [asteroide_y_init]

def coord_Asteroid(coord_x_Asteroid, coord_y_Asteroid, j, V0, theta):

    for i in range(0, j):

        x_Asteroid_crash_test = coord_x_Asteroid[i] + ((Fg_totale_x(coord_x_Asteroid[i], coord_y_Asteroid[i], i)) / Asteroid_crash_test.mass * ((i+1)**2/2)) + V0 * (i+1) * np.cos(theta)
        y_Asteroid_crash_test = coord_y_Asteroid[i] + ((Fg_totale_y(coord_x_Asteroid[i], coord_y_Asteroid[i], i)) / Asteroid_crash_test.mass * ((i+1)**2/2)) + V0 * (i+1) * np.sin(theta)

        coord_x_Asteroid.append(x_Asteroid_crash_test)
        coord_y_Asteroid.append(y_Asteroid_crash_test)

    return np.array(coord_x_Asteroid), np.array(coord_y_Asteroid)


coord_Asteroid(coord_x_Asteroid, coord_y_Asteroid, 60000, V0, theta)
*/




int main(int argc, char * argv[]) {
	
	/* nous avons décidés de compter en milliers de kilomètres c est pourquoi toutes nos valeurs de demi grand axe et la vistesse sont divisées par 1000
	 par rapport aux vraies valeurs, sinon notre plot aurait eu une taille de 10^10, ce qui n'aurait pas pu être possible étant donné que les int 
	 vont jusqu'à 2^31.  
	
	   pour les structures, nous avons initialisés les demis petits axes et les itérations à 0 car nous les calculons juste après avec les valeurs que 
	  nous avons implémentées.
	*/
	


	//struct Planete Mercure = {"Mercure", 56.625*pow(10,3), 0.2589, 0, 33*pow(10,22), 0, 175.936, 732,0};
	//struct Planete Venus = {"Venus", 105.615*pow(10,3), 0.0051, 0, 490, 0, 126.062, 274,0};
	//struct Planete Terre = {"Terre", 150.5*pow(10,3), 0.101, 0, 600, 0, 107.243, 164,0};
	//struct Planete Mars = {"Mars", 227.84*pow(10,3), 0.103, 0, 64, 0, 87.226, 88,0};
	//struct Planete Jupiter = {"Jupiter", 778.345*pow(10,3), 0.0507, 0, 190000, 0, 47.196, 14,0};
	//struct Planete Saturne = {"Saturne", 1427.18*pow(10,3), 0.0593, 0, 57000, 0, 34.962, 6,0};
	//struct Planete Uranus = {"Uranus", 2870.83*pow(10,3), 0.0482, 0, 8700, 0, 24.459, 2,0};
	//struct Planete Neptune = {"Neptune", 4496.975*pow(10,3), 0.0098, 0, 10000, 0, 19.566, 1,0};



	struct Planete Planetes[8];

	Planetes[0].nom = "Mercure";
	Planetes[0].demi_grand_axe = 56.625*pow(10,3);
	Planetes[0].excentricite = 0.2589;
	Planetes[0].demi_petit_axe = calc_demi_petit_axe(Planetes[0].demi_grand_axe, Planetes[0].excentricite);
	Planetes[0].masse = 33*pow(10,22);
	Planetes[0].iterations = calc_nb_iterations_selon_planete(calc_perimetre(Planetes[0].demi_grand_axe, Planetes[0].demi_petit_axe), Planetes[0].vitesse_planete);
	Planetes[0].vitesse_planete = 175.936;
	Planetes[0].multiple = 732,0;
	Planetes[0].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[0].demi_grand_axe, Planetes[0].demi_petit_axe), Planetes[0].iterations);
	Planetes[0].coord_x = 0;
	Planetes[0].coord_y = 0;
	Planetes[0].cos_planete = 0;
	Planetes[0].sin_planete = 0;

	Planetes[1].nom = "venus";
	Planetes[1].demi_grand_axe = 105.615*pow(10,3);
	Planetes[1].excentricite = 0.0051;
	Planetes[1].demi_petit_axe = calc_demi_petit_axe(Planetes[1].demi_grand_axe, Planetes[1].excentricite);
	Planetes[1].masse = 490*pow(10,22);
	Planetes[1].iterations = calc_nb_iterations_selon_planete(calc_perimetre(Planetes[1].demi_grand_axe, Planetes[1].demi_petit_axe), Planetes[1].vitesse_planete);
	Planetes[1].vitesse_planete = 126.062;
	Planetes[1].multiple = 274,0;
	Planetes[1].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[1].demi_grand_axe, Planetes[1].demi_petit_axe), Planetes[1].iterations);
	Planetes[1].coord_x = 0;
	Planetes[1].coord_y = 0;
	Planetes[1].cos_planete = 0;
	Planetes[1].sin_planete = 0;

	Planetes[2].nom = "Terre";
	Planetes[2].demi_grand_axe = 150.5*pow(10,3);
	Planetes[2].excentricite = 0.101;
	Planetes[2].demi_petit_axe = calc_demi_petit_axe(Planetes[2].demi_grand_axe, Planetes[2].excentricite);
	Planetes[2].masse = 600*pow(10,22);
	Planetes[2].iterations = calc_nb_iterations_selon_planete(calc_perimetre(Planetes[2].demi_grand_axe, Planetes[2].demi_petit_axe), Planetes[2].vitesse_planete);
	Planetes[2].vitesse_planete = 107.243;
	Planetes[2].multiple = 164,0;
	Planetes[2].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[2].demi_grand_axe, Planetes[2].demi_petit_axe), Planetes[2].iterations);
	Planetes[2].coord_x = 0;
	Planetes[2].coord_y = 0;
	Planetes[2].cos_planete = 0;
	Planetes[2].sin_planete = 0;

	Planetes[3].nom = "Mars";
	Planetes[3].demi_grand_axe = 227.84*pow(10,3);
	Planetes[3].excentricite = 0.103;
	Planetes[3].demi_petit_axe = calc_demi_petit_axe(Planetes[3].demi_grand_axe, Planetes[3].excentricite);
	Planetes[3].masse = 64 * pow(10,22);
	Planetes[3].iterations = calc_nb_iterations_selon_planete(calc_perimetre(Planetes[3].demi_grand_axe, Planetes[3].demi_petit_axe), Planetes[3].vitesse_planete);
	Planetes[3].vitesse_planete = 87.226;
	Planetes[3].multiple = 88,0;
	Planetes[3].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[3].demi_grand_axe, Planetes[3].demi_petit_axe), Planetes[3].iterations);
	Planetes[3].coord_x = 0;
	Planetes[3].coord_y = 0;
	Planetes[3].cos_planete = 0;
	Planetes[3].sin_planete = 0;

	Planetes[4].nom = "Jupiter";
	Planetes[4].demi_grand_axe = 778.345*pow(10,3);
	Planetes[4].excentricite = 0.0507;
	Planetes[4].demi_petit_axe = calc_demi_petit_axe(Planetes[4].demi_grand_axe, Planetes[4].excentricite);
	Planetes[4].masse = 190000 * pow(10,22);
	Planetes[4].iterations = calc_nb_iterations_selon_planete(calc_perimetre(Planetes[4].demi_grand_axe, Planetes[4].demi_petit_axe), Planetes[4].vitesse_planete);
	Planetes[4].vitesse_planete = 47.196;
	Planetes[4].multiple = 14,0;
	Planetes[4].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[4].demi_grand_axe, Planetes[4].demi_petit_axe), Planetes[4].iterations);
	Planetes[4].coord_x = 0;
	Planetes[4].coord_y = 0;
	Planetes[4].cos_planete = 0;
	Planetes[5].sin_planete = 0;

	Planetes[5].nom = "Saturne";
	Planetes[5].demi_grand_axe = 1427.18*pow(10,3);
	Planetes[5].excentricite = 0.0593;
	Planetes[5].demi_petit_axe = calc_demi_petit_axe(Planetes[5].demi_grand_axe, Planetes[5].excentricite);
	Planetes[5].masse = 57000 * pow(10,22);
	Planetes[5].iterations = calc_nb_iterations_selon_planete(calc_perimetre(Planetes[5].demi_grand_axe, Planetes[5].demi_petit_axe), Planetes[5].vitesse_planete);
	Planetes[5].vitesse_planete = 34.962;
	Planetes[5].multiple = 6,0;
	Planetes[5].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[3].demi_grand_axe, Planetes[3].demi_petit_axe), Planetes[3].iterations);
	Planetes[5].coord_x = 0;
	Planetes[5].coord_y = 0;
	Planetes[5].cos_planete = 0;
	Planetes[5].sin_planete = 0;

	Planetes[6].nom = "Uranus";
	Planetes[6].demi_grand_axe = 2870.83*pow(10,3);
	Planetes[6].excentricite = 0.0482;
	Planetes[6].demi_petit_axe = calc_demi_petit_axe(Planetes[6].demi_grand_axe, Planetes[6].excentricite);
	Planetes[6].masse = 8700 * pow(10,22);
	Planetes[6].iterations = calc_nb_iterations_selon_planete(calc_perimetre(Planetes[6].demi_grand_axe, Planetes[6].demi_petit_axe), Planetes[6].vitesse_planete);
	Planetes[6].vitesse_planete = 24.459;
	Planetes[6].multiple = 2,0;
	Planetes[6].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[6].demi_grand_axe, Planetes[6].demi_petit_axe), Planetes[6].iterations);
	Planetes[6].coord_x = 0;
	Planetes[6].coord_y = 0;
	Planetes[6].cos_planete = 0;
	Planetes[6].sin_planete = 0;

	Planetes[7].nom = "Neptune";
	Planetes[7].demi_grand_axe = 4496.975*pow(10,3);
	Planetes[7].excentricite = 0.0098;
	Planetes[7].demi_petit_axe = calc_demi_petit_axe(Planetes[7].demi_grand_axe, Planetes[7].excentricite);
	Planetes[7].masse = 10000 * pow(10,22);
	Planetes[7].iterations = calc_nb_iterations_selon_planete(calc_perimetre(Planetes[7].demi_grand_axe, Planetes[7].demi_petit_axe), Planetes[7].vitesse_planete);
	Planetes[7].vitesse_planete = 19.566;
	Planetes[7].multiple = 1,0;
	Planetes[7].rayon_collision = calc_rayon_collision(calc_perimetre(Planetes[7].demi_grand_axe, Planetes[7].demi_petit_axe), Planetes[7].iterations);
	Planetes[7].coord_x = 0;
	Planetes[7].coord_y = 0;
	Planetes[7].cos_planete = 0;
	Planetes[7].sin_planete = 0;


	struct Etoile Soleil;
	Soleil.nom = "Soleil";
	Soleil.masse = 1.989e30;
	Soleil.coord_x = 4.9985 * 10e5;
	Soleil.coord_y = 5 * 10e5;
	Soleil.cos_etoile = 0;
	Soleil.sin_etoile = 0;

	struct Asteroids Asteroid;
	Asteroid.nom = "Asteroid";
	Asteroid.masse = 10e18;
	Asteroid.rayon = 0;
	Asteroid.V0 = 1;
	Asteroid.theta = 0; 
	Asteroid.x_init = coor_ast("x");
	Asteroid.y_init = coor_ast("y");

	double asteroide_x_init=coor_ast("x");
	
	
	while (asteroide_x_init > 10000000){
		asteroide_x_init = Asteroid.x_init;
		
	}
	// pas besoin de mettre <0 car notre programme reconnait le - comme n'étant pas un int
	
	double asteroide_y_init = coor_ast("y");
	
	while ((asteroide_x_init >1000000 && asteroide_x_init < 9000000) && (asteroide_y_init > 1000000 && asteroide_y_init < 9000000) == true) {
		printf("l'asteroide est trop proche des planetes, il faut prendre une valeur de y entre 0 et 1000000 ou 9000000 et 10000000");
		asteroide_y_init = Asteroid.y_init;
	}

	/* Planetes[0].demi_petit_axe = calc_demi_petit_axe(Mercure.demi_grand_axe, Mercure.excentricite);
	Mercure.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Mercure.demi_grand_axe, Mercure.demi_petit_axe), Mercure.vitesse_planete);
	Mercure.rayon_collision = calc_rayon_collision(calc_perimetre(Mercure.demi_grand_axe, Mercure.demi_petit_axe), Mercure.iterations);
	// le perimetre de Mercure étant calculé à l'aide du demi-grand axe et du demi-petit axe, nous avons un périmètre assez éloigné de la valeur réelle
	
	
	Venus.demi_petit_axe = calc_demi_petit_axe(Venus.demi_grand_axe, Venus.excentricite);
	Venus.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Venus.demi_grand_axe, Venus.demi_petit_axe), Venus.vitesse_planete);
	Venus.rayon_collision = calc_rayon_collision(calc_perimetre(Venus.demi_grand_axe, Venus.demi_petit_axe), Venus.iterations);
	
	
	Terre.demi_petit_axe = calc_demi_petit_axe(Terre.demi_grand_axe, Terre.excentricite);
	Terre.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Terre.demi_grand_axe, Terre.demi_petit_axe), Terre.vitesse_planete);
	Terre.rayon_collision = calc_rayon_collision(calc_perimetre(Terre.demi_grand_axe, Terre.demi_petit_axe), Terre.iterations);
	
	
	Mars.demi_petit_axe = calc_demi_petit_axe(Mars.demi_grand_axe, Mars.excentricite);
	Mars.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Mars.demi_grand_axe, Mars.demi_petit_axe), Mars.vitesse_planete);
	Mars.rayon_collision = calc_rayon_collision(calc_perimetre(Mars.demi_grand_axe, Mars.demi_petit_axe), Mars.iterations);
	
	
	Jupiter.demi_petit_axe = calc_demi_petit_axe(Jupiter.demi_grand_axe, Jupiter.excentricite);
	Jupiter.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Jupiter.demi_grand_axe, Jupiter.demi_petit_axe), Jupiter.vitesse_planete);
	Jupiter.rayon_collision = calc_rayon_collision(calc_perimetre(Jupiter.demi_grand_axe, Jupiter.demi_petit_axe), Jupiter.iterations);
	
	
	Saturne.demi_petit_axe = calc_demi_petit_axe(Saturne.demi_grand_axe, Saturne.excentricite);
	Saturne.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Saturne.demi_grand_axe, Saturne.demi_petit_axe), Saturne.vitesse_planete);
	Saturne.rayon_collision = calc_rayon_collision(calc_perimetre(Saturne.demi_grand_axe, Saturne.demi_petit_axe), Saturne.iterations);
	
	
	Uranus.demi_petit_axe = calc_demi_petit_axe(Uranus.demi_grand_axe, Uranus.excentricite);
	Uranus.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Uranus.demi_grand_axe, Uranus.demi_petit_axe), Uranus.vitesse_planete);
	Uranus.rayon_collision = calc_rayon_collision(calc_perimetre(Uranus.demi_grand_axe, Mercure.demi_petit_axe), Uranus.iterations);
	
	
	Neptune.demi_petit_axe = calc_demi_petit_axe(Neptune.demi_grand_axe, Neptune.excentricite);
	Neptune.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Neptune.demi_grand_axe, Neptune.demi_petit_axe), Neptune.vitesse_planete);
	Neptune.rayon_collision = calc_rayon_collision(calc_perimetre(Neptune.demi_grand_axe, Neptune.demi_petit_axe), Neptune.iterations);
	*/


	double centre_x = 5.0e+6;
	double centre_y = 5.0e+6;

	char * nom_fichier_csv[] = {"planete_Mercure.csv", "planete_Venus.csv", "planete_Terre.csv", "planete_Mars.csv", "planete_Jupiter.csv", "planete_Saturne.csv", "planete_Neptune.csv"};

	for (int i = 0; i < 8; i++) {
		fichierCSV(nom_fichier_csv[i], centre_x, centre_y, Planetes[i].demi_grand_axe, Planetes[i].demi_petit_axe, Planetes[i].iterations, Planetes[i].multiple);
	}

	double * coord_x_Asteroid = calloc(60000, sizeof (double));
	double * coord_y_Asteroid = calloc(60000, sizeof (double));

	coord_x_Asteroid[0] = Asteroid.x_init;
	coord_y_Asteroid[0] = Asteroid.y_init;

	for (int i = 0; i < 60000; i++) {
		coord_x_Asteroid[i + 1] = coord_x_Asteroid[i] + ((Fg_totale_x(coord_x_Asteroid[i], coord_y_Asteroid[i], i, , struct Planete Planetes[], struct Etoile Soleil)) / Asteroid.masse * (pow((i+1),2)/2)) + Asteroid.V0 * (i+1) * cos(Asteroid.theta);
        coord_y_Asteroid[i + 1] = coord_y_Asteroid[i] + ((Fg_totale_y(coord_x_Asteroid[i], coord_y_Asteroid[i], i, )) / Asteroid.masse * (pow((i+1),2)/2)) + Asteroid.V0 * (i+1) * sin(Asteroid.theta);
	

 









/*fichierCSV("planete_Mercure.csv", centre_x, centre_y, Mercure.demi_grand_axe, Mercure.demi_petit_axe, Mercure.iterations, Mercure.multiple);
	fichierCSV("planete_Venus.csv", centre_x, centre_y, Venus.demi_grand_axe, Venus.demi_petit_axe, Venus.iterations, Venus.multiple);
	fichierCSV("planete_Terre.csv", centre_x, centre_y, Terre.demi_grand_axe, Terre.demi_petit_axe, Terre.iterations, Terre.multiple);
	fichierCSV("planete_Mars.csv", centre_x, centre_y, Mars.demi_grand_axe, Mars.demi_petit_axe, Mars.iterations, Mars.multiple);
	fichierCSV("planete_Jupiter.csv", centre_x, centre_y, Jupiter.demi_grand_axe, Jupiter.demi_petit_axe, Jupiter.iterations, Jupiter.multiple);
	fichierCSV("planete_Saturne.csv", centre_x, centre_y, Saturne.demi_grand_axe, Saturne.demi_petit_axe, Saturne.iterations, Saturne.multiple);
	fichierCSV("planete_Uranus.csv", centre_x, centre_y, Uranus.demi_grand_axe, Uranus.demi_petit_axe, Uranus.iterations, Uranus.multiple);
	fichierCSV("planete_Neptune.csv", centre_x, centre_y, Neptune.demi_grand_axe, Neptune.demi_petit_axe, Neptune.iterations, Neptune.multiple);
*/

	return 0; 
}
