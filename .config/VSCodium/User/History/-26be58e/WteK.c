#include <stdio.h>

void help() {
    printf("Todolist : A simple command line todolist : \n\n");
    printf("Usage : todolist <arg> <...>\n");
    printf("-a --add : add a new task\n");
    printf("-d --done : mark a task by its number has done\n");
    printf("-r --remove : delete a task by its number\n");
}

int main(int argc, char** argv) {

    char* arg = argv[1];

    if (arg[0] == '-') {
        switch (arg[1]) {
            case 'h':
                help();
                break;
        }
    }

    return 0;
}
