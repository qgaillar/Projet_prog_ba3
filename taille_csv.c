
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>
#include "planete_perimetre.c"

void fichierCSV2 ( char* filename, int multiplication, char * fichier) {
	FILE * file = fopen(filename, "w+");
	
	FILE * fichier2 = fopen(fichier, "r");
	char c;
	
	for (int i = 0; i < multiplication; i++) { 
		while((c=fgetc(fichier2))!=EOF){
        printf("%c",c);
		} 
        fprintf(file, "%c", c);    
        fprintf(file, "\n");
    }

    fclose(file);
}

int main2(int argc, char * argv[]) {
	fichierCSV2("Mercure2.csv", 372, "planete_Mercure.csv");
	
	return 0;
} 
