#include <stdio.h>

#include "printgrid.h"
#include "move.h"
#include "victorydetection.h"

/*
The grid will be like this :

 0 | 1 | 2
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
*/

char grid[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};


void clearScreen();
int isGridComplete(char grid[][3]); 


int main(int argc, char* argv[]) {
    int count = 0;

    game:

        printf("%d", count);

        clearScreen();
        
        printgrid(grid);

        move(grid, 'X');
        
        count++;

        printgrid(grid);

        move(grid, 'O');

        count++;

        char winner = ' ';

        if (victoryDetection(grid, 'X') == 'X') {
            winner = 'X';
            printf("%c", winner);
        } else if (victoryDetection(grid, 'O') == 'O') {
            winner = 'O';
            printf("%c", winner);
        }

        if (winner == ' ') {
            goto game;
        } else {
            printgrid(grid);
            printf("Winned by %c\n");
        }

        if (count == 9) {
            printf("There's no winner !\n");
        }


    return 0;
}

void clearScreen() {
    system("clear");
}