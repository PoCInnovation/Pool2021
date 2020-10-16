#include <stdio.h>
#include <string.h>

int main(int ac, char **ag)
{
    char flag[] = {26, 95, 57, 5, 91, 45, 47, 36, 55, 113, 61, 40, 67, 11, 46, 51, 0, 95, 32, 46, 94, 34, 38, 0, 33, 89, 58, 33};
    char key[] = "N0TF7LAG";

    if (ac != 2) {
        printf("You should try something else.\n");
        return -2;
    }
    for (int i = 0; i < 28; i++) {
        flag[i] ^= key[i % 8];
    }
    if (!strcmp(ag[1], flag)) {
        printf("HOW DID YOU DO THIS???\ngg\n");
        return 0;
    }
    printf("nope.\n");
    return -1;
}