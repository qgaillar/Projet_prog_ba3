
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>
#define TRUE 1
#define FALSE 0

/*
int coor_asteroide (char* coor) {
    int coor_voulue;
    printf("Entrer une coordonnee %s :", coor );
    scanf("%d", &coor_voulue);  
    printf("coordonnee = %d\n",coor_voulue);
    return coor_asteroide;
    
}
*/


int coor_ast(char* coordonnee)
{
    char n[10]; // Car c'est le nombre max de chiffre pour un programme sur 32 bits
    int test_int;
    printf("Entrer une coordonnee %s entre 0 et 10^7:", coordonnee);

    do
    {        
        scanf(" %s", n);

        test_int = TRUE; 

        int i = 0, l = strlen(n);

        while (i < l)
        {            
            if (n[i] < '0' || n[i] > '9') // Vérifie si les valeurs sont des int ou non
            {              
                test_int = FALSE; // arrête la boucle si la condition n'est pas vérifiée
                break;
            }
            i++;
        }
        if (test_int == TRUE)
            printf("%i\n", atoi(n)); // change la valeur en int
       
        else 
            printf("Mettre une nouvelle valeur entre 0 et 10^7: ");
        }
	
    while (test_int == FALSE); 
    
    return 0;
}

int main (int argc, char * argv[]) {
	int asteroide_x = coor_ast("x");
	int asteroide_y = coor_ast("y");
	
	
	return 0;
}
