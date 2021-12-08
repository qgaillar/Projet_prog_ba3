
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>

int coor_voulue (char* coor) {
    int coor_asteroide;
    printf("Entrer une coordonnee %s :", coor );
    scanf("%d", &coor_asteroide);  
    printf("coordonnee = %d\n",coor_asteroide);
    return coor_asteroide;
    
}

int main (int argc, char * argv[]) {
	coor_voulue("x");
	coor_voulue("y");
	
	return 0;
}
