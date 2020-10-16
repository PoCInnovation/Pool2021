#include <stdio.h>

int decrement(int i)
{
    return i - 21;
}

int main(void)
{
    int first = 42;
    int second = 2;

    if (first * second == 84)
        first = decrement(first);
    else
        first += 1;
    return first - second;
}
