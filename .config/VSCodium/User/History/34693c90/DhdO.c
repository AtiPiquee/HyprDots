#include <stdio.h>

#include "move.h"

void move(char grid[9], char player) {
    int column;
    int row; 

    move:

        printf("row ? [1 - 3] : ");
        scanf("%d", &row);

        row--;

        printf("column ? [1 - 3] : ");
        scanf("%d", &column);

        column--;
    
    int index = column * 3 + row;

    if (grid[index] != ' ') {
        printf("These coordinate are already taken !\n");
        goto move;
    } else {
        grid[index] = player;
    }
}