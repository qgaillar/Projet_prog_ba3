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
		
		int ua = 150.5;	
		double coor_x = centre_x + 2.5*ua*demi_grand_axe*cos(M_PI*i/50);
		double coor_y = centre_y + 2.5*ua*demi_petit_axe *sin(M_PI*i/50);
                     
        fprintf(file, "%0.6f,%0.6f", coor_x, coor_y );    
        fprintf(file, "\n");
    }

    fclose(file);

}


int main(int argc, char * argv[]) {
	srand(time(NULL));
    double randomDomaine = RAND_MAX + 1.0;
    
    int centre_x = 5000;
    int centre_y = 5000;
    
    
    double demi_grand_axe_random = rand() / randomDomaine * 1;
    printf("%f\n", demi_grand_axe_random);
    
    double excentricite_random = rand() / randomDomaine * 0.5;
    printf("%f\n", excentricite_random);

    fichierCSV("planete_Asteroide.csv" , centre_x, centre_y, demi_grand_axe_random, calc_demi_petit_axe(demi_grand_axe_random, excentricite_random));

    return 0;

}
