#include <stdio.h>

#include "printgrid.h"

void printgrid(char grid[9]) {

    printf("\n");
    printf(" %c | %c | %c \n", grid[0], grid[1], grid[2]);
    printf("---|---|---\n");
    printf(" %c | %c | %c \n", grid[3], grid[4], grid[5]);
    printf("---|---|---\n");
    printf(" %c | %c | %c \n", grid[6], grid[7], grid[8]);

}
