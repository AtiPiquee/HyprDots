#include <stdio.h>

#include "victorydetection.h"

char victoryDetection(char grid[9], char player) {
    char winner = ' ';

    int i = 0;
    int j = 2;

    horizontal:
        if (grid[i][0] == player && grid[i][1] == player && grid[i][2] == player) {
            winner = player;
        } else if (i <= 2 && winner == ' ') {
            i++;
            goto horizontal;
        } 

    i = 0;
           
    vertical:
       if (grid[0][i] == player && grid[1][i] == player && grid[2][i] == player) {
           winner = player;
       } else if (i <= 2 && winner == ' ') {
           i++;
           goto vertical;
       }

    i = 0;

    diagonal:
       if (grid[0][i] == player && grid[1][1] == player && grid[j][2] == player) {
           winner = player;
       } else if (i <= 2 && j >= 2 && winner == ' ') {
           i = i + 2;
           j = j - 2;
           goto diagonal;
        }

    return winner;
}