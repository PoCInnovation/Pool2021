# pwn

pwn is the security field where you exploit memory corruptions breach and vulnerable designs. This field is really interesting because it helps you discover and exploit the various errors a developer can make.
In this workshop, we are going to study :
* stack buffer overflows
* format string injections
* race conditions
* use after free

# 1 - Format String Injections

printf, scanf etc. are really useful when you develop a program. But you can have severe security vulnerabilities if you use them without RTFM.

## Read the Stack

The first consequence of a format string injection vulnerability is that the attacker can read the stack. And as we know, the stack contains our local variables, which can store some precious content...

Solve the `Format String 1` challenge.

# 2 - Stack Buffer Overflows

## Introduction

In the Reverse Enginneering #1 workshop, we saw how the stack worked. Stack buffer overflow is a vulnerability that is used to write over some values on the stack. To understand it clearly, you must first find out why this code never prints "Hello World" :
```C
#include <stdio.h>

int main(void)
{
    int i = 0;
    char buffer[6];

    while (i < 7) {
        buffer[i] = 0;
        i += 1;
    }
    printf("Hello world !\n");
    return 0;
}
```

Your explanation must include a schema of the stack.

## Time to exploit

Now that we understand how this vulnerability works, we are going to see how we can exploit it and what we can do with it.

### Changing variables values

You must solve the `Dead Beef` challenge.

### Calling functions

You must solve the `Please be nice` challenge.

# 3 - ROP chain

Returned Oriented Programming is a way to exploit memory corruption vulnerability to modify the program behaviour. The goal here is to modify the execution flow of a binary in order to make it perform different actions (open files on the system, call a functions with specific parameters ...)

### Discover pwntools

pwntools is a framework used to automate pwn and reverse challenges resolution. We need it to go through ROP chain challenges. You must install it with
```py
python3 -m pip install --upgrade pwntools
```
If you have any issue with the installation, try to install the [development version](https://docs.pwntools.com/en/stable/install.html)

You must flag the `Please be nice` challenge again using pwntools. Show it to an organizer to get your flag.

### Your first ROP chain

The challenge is available [here]. Here is some help to resolve it:
1. What is the binary doing ?
2. Can you find a memory corruption vulnerability ?
3. What would you like the binary to do ?
4. Write your ROP chain with pwntools

Note that pwntools supports TCP communication. In order to make the challenge execute your payload, you may want to use [the remote function](https://docs.pwntools.com/en/stable/tubes/sockets.html)

You must solve the `Abuse Me` challenge.

# 4 - Use after Free

When you allocate memory with malloc / calloc / realloc, this memory is dynamically given to you and you can modify its content. Imagine that you allocate 5 bytes of memory, in which you write "AAAAA". If you free this memory, we won't be able to access it anymore BUT the "AAAAA" value is not reset : it is still written in memory and our pointer still points to this adress !

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(void)
{
    char *admin = (char *)malloc(sizeof(char) * 6);
    char *user;

    for (int i = 0; i < 6; i += 1) {
        admin[i] = 0;
    }
    free(admin);
    user = (char *)malloc(sizeof(char) * 6);
    read(0, user, 5);
    if (admin && strcmp(admin, "admin") == 0) {
        printf("Welcome admin !\n");
        return 0;
    }
    printf("You are not admin, get out !\n");
    free(user);
    return 1;
}
```

What sould you do to be recognize as an administrator here ? Your explanation must contain a representation of the memory at the variable addresses. What can you say about the value contained in the pointers admin and user throughout the program ?

## Exploitation

Here is a nice challenge on exploiting a Use After Free vulnerability to gain privileges in the program !

[Root-me ELF x86 Use After Free](https://www.root-me.org/fr/Challenges/App-Systeme/ELF-x86-Use-After-Free-basic)

# 5 - Race Condition

The logical flow of a program can be poorly designed by the developer and have non-desired consequences. To exploit a race condition, you have to do a certain action at a certain timing, be quick !

Solve this [Root-me Challenge](https://www.root-me.org/fr/Challenges/App-Systeme/ELF-x86-Race-condition) !

# The End

In this workshop, we have learnt a lot on how we can exploit error of memory use and poor design in software logic to modify its behaviour.
