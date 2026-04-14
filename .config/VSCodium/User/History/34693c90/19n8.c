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
    
    if (grid[row][column] != ' ') {
        printf("These coordinate are already taken !\n");
        goto move;
    } else {
        int index = column * 3 + row;
        grid[index] = player;
    }
}