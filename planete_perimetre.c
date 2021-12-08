
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
	

};

struct Asteroid {
	char* nom;
	double masse;
	double rayon;
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

double Fg(double masse,double masse_asteroide, double x_Asteroid_t_reel, double y_Asteroid_t_reel, double x_planete, double y_planete){
	double G = 6.67*pow(10, -11);
    double delta_x = x_Asteroid_t_reel - x_planete;
    double delta_y = y_Asteroid_t_reel - y_planete;
    double dist = pow(pow(delta_x,2) + pow(delta_y,2), 1/2);
    double Force_gravitationnelle = (G * masse * masse_asteroide) / pow((dist * 10e3),2);  //10e3 = conversion en mètres
    return Force_gravitationnelle;
}
/*
def Fg_totale_x(x_Asteroid_crash_test, y_Asteroid_crash_test, i):

    cos_Mercure = (abs(x_Asteroid_crash_test - Mercure.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Mercure.coord_x[i])**2 + (y_Asteroid_crash_test - Mercure.coord_y[i])**2))
    cos_Venus = (abs(x_Asteroid_crash_test - Venus.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Venus.coord_x[i])**2 + (y_Asteroid_crash_test - Venus.coord_y[i])**2))
    cos_Terre = (abs(x_Asteroid_crash_test - Terre.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Terre.coord_x[i])**2 + (y_Asteroid_crash_test - Terre.coord_y[i])**2))
    cos_Mars = (abs(x_Asteroid_crash_test - Mars.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Mars.coord_x[i])**2 + (y_Asteroid_crash_test - Mars.coord_y[i])**2))
    cos_Jupiter = (abs(x_Asteroid_crash_test - Jupiter.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Jupiter.coord_x[i])**2 + (y_Asteroid_crash_test - Jupiter.coord_y[i])**2))
    cos_Saturne = (abs(x_Asteroid_crash_test - Saturne.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Saturne.coord_x[i])**2 + (y_Asteroid_crash_test - Saturne.coord_y[i])**2))
    cos_Uranus = (abs(x_Asteroid_crash_test - Uranus.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Uranus.coord_x[i])**2 + (y_Asteroid_crash_test - Uranus.coord_y[i])**2))
    cos_Neptune = (abs(x_Asteroid_crash_test - Neptune.coord_x[i]) / np.sqrt((x_Asteroid_crash_test - Neptune.coord_x[i])**2 + (y_Asteroid_crash_test - Neptune.coord_y[i])**2))
    cos_Soleil = (abs(x_Asteroid_crash_test - Soleil.coord_x) / np.sqrt((x_Asteroid_crash_test - Soleil.coord_x)**2 + (y_Asteroid_crash_test - Soleil.coord_y)**2))

    Fg_tot_x = (
        Fg(Mercure.mass, x_Asteroid_crash_test, y_Asteroid_crash_test, Mercure.coord_x[i], Mercure.coord_y[i]) * cos_Mercure + #pb avec Fg qui génère 1705 valeurs d'un coup 
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
*/
int main(int argc, char * argv[]) {
	
	/* nous avons décidés de compter en milliers de kilomètres c est pourquoi toutes nos valeurs de demi grand axe et la vistesse sont divisées par 1000
	 par rapport aux vraies valeurs, sinon notre plot aurait eu une taille de 10^10, ce qui n'aurait pas pu être possible étant donné que les int 
	 vont jusqu'à 2^31.  
	
	   pour les structures, nous avons initialisés les demis petits axes et les itérations à 0 car nous les calculons juste après avec les valeurs que 
	  nous avons implémentées.
	*/
	
	struct Planete Mercure = {"Mercure", 56.625*pow(10,3), 0.2589, 0, 33*pow(10,22), 0, 175.936, 732,0};
	Mercure.demi_petit_axe = calc_demi_petit_axe(Mercure.demi_grand_axe, Mercure.excentricite);
	Mercure.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Mercure.demi_grand_axe, Mercure.demi_petit_axe), Mercure.vitesse_planete);
	Mercure.rayon_collision = calc_rayon_collision(calc_perimetre(Mercure.demi_grand_axe, Mercure.demi_petit_axe), Mercure.iterations);
	// le perimetre de Mercure étant calculé à l'aide du demi-grand axe et du demi-petit axe, nous avons un périmètre assez éloigné de la valeur réelle
	
	struct Planete Venus = {"Venus", 105.615*pow(10,3), 0.0051, 0, 490, 0, 126.062, 274,0};
	Venus.demi_petit_axe = calc_demi_petit_axe(Venus.demi_grand_axe, Venus.excentricite);
	Venus.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Venus.demi_grand_axe, Venus.demi_petit_axe), Venus.vitesse_planete);
	Venus.rayon_collision = calc_rayon_collision(calc_perimetre(Venus.demi_grand_axe, Venus.demi_petit_axe), Venus.iterations);
	
	struct Planete Terre = {"Terre", 150.5*pow(10,3), 0.101, 0, 600, 0, 107.243, 164,0};
	Terre.demi_petit_axe = calc_demi_petit_axe(Terre.demi_grand_axe, Terre.excentricite);
	Terre.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Terre.demi_grand_axe, Terre.demi_petit_axe), Terre.vitesse_planete);
	Terre.rayon_collision = calc_rayon_collision(calc_perimetre(Terre.demi_grand_axe, Terre.demi_petit_axe), Terre.iterations);
	
	struct Planete Mars = {"Mars", 227.84*pow(10,3), 0.103, 0, 64, 0, 87.226, 88,0};
	Mars.demi_petit_axe = calc_demi_petit_axe(Mars.demi_grand_axe, Mars.excentricite);
	Mars.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Mars.demi_grand_axe, Mars.demi_petit_axe), Mars.vitesse_planete);
	Mars.rayon_collision = calc_rayon_collision(calc_perimetre(Mars.demi_grand_axe, Mars.demi_petit_axe), Mars.iterations);
	
	struct Planete Jupiter = {"Jupiter", 778.345*pow(10,3), 0.0507, 0, 190000, 0, 47.196, 14,0};
	Jupiter.demi_petit_axe = calc_demi_petit_axe(Jupiter.demi_grand_axe, Jupiter.excentricite);
	Jupiter.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Jupiter.demi_grand_axe, Jupiter.demi_petit_axe), Jupiter.vitesse_planete);
	Jupiter.rayon_collision = calc_rayon_collision(calc_perimetre(Jupiter.demi_grand_axe, Jupiter.demi_petit_axe), Jupiter.iterations);
	
	struct Planete Saturne = {"Saturne", 1427.18*pow(10,3), 0.0593, 0, 57000, 0, 34.962, 6,0};
	Saturne.demi_petit_axe = calc_demi_petit_axe(Saturne.demi_grand_axe, Saturne.excentricite);
	Saturne.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Saturne.demi_grand_axe, Saturne.demi_petit_axe), Saturne.vitesse_planete);
	Saturne.rayon_collision = calc_rayon_collision(calc_perimetre(Saturne.demi_grand_axe, Saturne.demi_petit_axe), Saturne.iterations);
	
	struct Planete Uranus = {"Uranus", 2870.83*pow(10,3), 0.0482, 0, 8700, 0, 24.459, 2,0};
	Uranus.demi_petit_axe = calc_demi_petit_axe(Uranus.demi_grand_axe, Uranus.excentricite);
	Uranus.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Uranus.demi_grand_axe, Uranus.demi_petit_axe), Uranus.vitesse_planete);
	Uranus.rayon_collision = calc_rayon_collision(calc_perimetre(Uranus.demi_grand_axe, Mercure.demi_petit_axe), Uranus.iterations);
	
	struct Planete Neptune = {"Neptune", 4496.975*pow(10,3), 0.0098, 0, 10000, 0, 19.566, 1,0};
	Neptune.demi_petit_axe = calc_demi_petit_axe(Neptune.demi_grand_axe, Neptune.excentricite);
	Neptune.iterations = calc_nb_iterations_selon_planete(calc_perimetre(Neptune.demi_grand_axe, Neptune.demi_petit_axe), Neptune.vitesse_planete);
	Neptune.rayon_collision = calc_rayon_collision(calc_perimetre(Neptune.demi_grand_axe, Neptune.demi_petit_axe), Neptune.iterations);
	
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
	
	double asteroide_x_init=coor_ast("x");
	
	
	while (asteroide_x_init > 10000000){
		asteroide_x_init = coor_ast("x");
		
	}
	// pas besoin de mettre <0 car notre programme reconnait le - comme n'étant pas un int
	
	double asteroide_y_init = coor_ast("y");
	
	while ((asteroide_x_init >1000000 && asteroide_x_init < 9000000) && (asteroide_y_init > 1000000 && asteroide_y_init < 9000000) == true) {
		printf("l'asteroide est trop proche des planetes, il faut prendre une valeur de y entre 0 et 1000000 ou 9000000 et 10000000");
		asteroide_y_init = coor_ast("y");
	}
	
	
	
	return 0; 
}
