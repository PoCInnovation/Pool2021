#include <stdio.h>
#include <string.h>

int main(int ac, char **ag)
{
    if (**ag) {
        printf("Try again...\n");
        return -1
    }
    if (ac == 4200) {
        printf("More please...\n");
        return -1
    }
}