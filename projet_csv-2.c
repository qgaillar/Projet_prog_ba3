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
	double demi_petit_axe = calc_demi_petit_axe(150.5, 0.101);
	fichierCSV("planete_test.csv", 5000, 5000, 150.5, demi_petit_axe);
	return 0; 

}
