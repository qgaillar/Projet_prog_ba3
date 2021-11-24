#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>


void fichierCSV ( char* filename, double coor_x, double coor_y) {
	FILE * file = fopen(filename, "w+");
	
	for (int i=0; i< 100; i++) {
		srand(time(NULL));
		double randomDomaine = RAND_MAX + 1.0;
		
		double v_x = rand() / randomDomaine * 100;
		double v_y = rand() / randomDomaine * 100;
		printf("%f\n", v_x);
	
		double asteroide_x = coor_x + v_x;
		double asteroide_y = coor_y + v_y;
		
		asteroide_x += coor_x;
		asteroide_y += coor_y;
		
		printf("%f\n", coor_x);
		
		if (asteroide_x < 0) break;
        if (asteroide_y < 0) break;
        if (asteroide_x > 10000) break;
        if (asteroide_y > 10000) break;
					
		fprintf(file, "%0.6f,%0.6f", asteroide_x, asteroide_y );    
		fprintf(file, "\n");
	}

    fclose(file);
}


/*
void coor_haut ( double coor_x, double coor_y) {
	
}
*/
int main(int argc, char * argv[]) {
	srand(time(NULL));
    double randomDomaine = RAND_MAX + 1.0;
    
    //int x_limite[] = {0, 1000, 0, 10000, 9000, 10000, 0, 10000};
    //int y_limite[] = {0, 10000, 0, 1000, 0, 10000, 9000, 10000};
    
   
    int tmp = (int) (rand() / randomDomaine * 4);
    printf("%d\n", tmp);
    int alea_zone = (int) (rand() / randomDomaine * 4);
    printf("%d\n", alea_zone);
    
    if (alea_zone == 0) {
		int coor_x = (int) (rand() / randomDomaine * 1000);
		int coor_y = (int) (rand() / randomDomaine * 10000);
		printf("%d, %d \n", coor_x, coor_y);
		fichierCSV ("asteroide.csv", coor_x, coor_y);
	}
	if (alea_zone == 1) {
		int coor_x = (int) (rand() / randomDomaine * 10000);
		int coor_y = (int) (rand() / randomDomaine * 1000);
		printf("%d, %d \n", coor_x, coor_y); 
		fichierCSV ("asteroide.csv", coor_x, coor_y);
	} 
	if (alea_zone == 2) {
		int coor_x = (int) (rand() / randomDomaine * 1000) + 9000;
		int coor_y = (int) (rand() / randomDomaine * 10000); 
		printf("%d, %d \n", coor_x, coor_y); 
		fichierCSV ("asteroide.csv", coor_x, coor_y);
	}
	if (alea_zone == 3) {
		int coor_x = (int) (rand() / randomDomaine * 10000);
		int coor_y = (int) (rand() / randomDomaine * 1000) + 9000;
		printf("%d, %d \n", coor_x, coor_y);
		fichierCSV ("asteroide.csv", coor_x, coor_y); 
	}
	
	
	
	
	 
    
}
