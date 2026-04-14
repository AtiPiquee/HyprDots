#include <stdio.h>

void help() {
    printf("Todolist : A simple command line todolist : \n\n");
    printf("");
}

int main(int argc, char** argv) {
    
    for (int i = 1; i < argc; i++ ) {
        printf("%d : %s\n", i, argv[i]);
    }

    return 0;
}
