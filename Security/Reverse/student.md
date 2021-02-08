
# Introduction
Reverse Engineering aims to understand what a program does. The goal of the Reverse Engineer is to deduce the source code of a given program from the analysis he made on it.

This field of security is often encountered in :

-   video games / software cracking (analysis of the way the game is protected -> binary patching)
-   malware analysis (understand the way it works -> conclude how to neutralize it)
-   vulnerability analysis

Reverse Engineer implies a certain knowledge of the way the computer memory works and of creation and execution of a binary. Here are some keywords you should be able to understand to start your Reverse Engineering journey :

-   binary file
-   ELF
-   compilation
-   memory segmentation
-   stack
-   registers
# GDB-Peda
For this part, you will need to install  `gdb`  (if not already installed on your system) and  [PEDA](https://github.com/longld/peda), a Python plugin for the debugger.

_N.B: If you don’t manage to run the binaries and encounter a “File not found”, you must install a 32bits library. You may try glibc.i686_
## 0 - Reflexes
Here is the first exercice. The purpose here is to make you have the good reflexes when you start the analysis of a binary.

-   What is the format of the  _reflexes_  binary ?
-   What is the targeted architecture ?
-   Is it 32 or 64 bits ? You should find two ways of finding the password of this challenge.
- What happen when you execute the binary ? ?

Keep all this recognition process in mind, it’s really useful when you face a reverse engineering challenge.
## 1 - Translate me
Static analysis is the process of studying a program without running it. To do so, we can use GDB to interpret the asm code in binary form to plaintext binary. Then we read this code and deduce the way the program work. So go ahead and open  _translate_me_  with  `gdb ./translate_me`  ! To display the asm instructions of a function, use  `pdisas function_name`  or  `pd function_name`.

The purpose of this challenge is not to find a flag but to translate the asm code you get with gdb to C code and then send it to us so we can give you the flag.
## 2- Dynamic Analysis
Now we are going to learn how to analyze dynamically a binary. With GDB we can run our binary instruction by instruction and see, for each one of them, the corresponding values of the registers and the stack. To dynamically analyze a binary, you can use  `start`  in gdb. Here are the most useful commands during a dynamic analysis in GDB :

-   `s`  to execute the next instruction.
-   `finish`  to go directly to the next instruction after the current function.
-   `b*addr`  where addr is the address of an instruction. This sets a breakpoint to this address.
-   `run`  to go to the next breakpoint or to the end of the program if no breakpoint set.
## 3- Basic protection
There various way of protecting a binary from Reverse Engineering, for example :

-   obfuscation : you pollute your binary with useless instructions to make the work of the reverse engineer harder.
-   dynamic analysis protection with ptrace
-   stripped binaries : remove the useful debugging information, which are basically metadata about variables and functions addresses and names.

Try to identify which protection(s) is/are used on  _im-protected_. Find a way to bypass it and solve the challenge !

## 4- Vault
[Polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)) is the idea of self-modifying programs. You should already have had a talk about it. Feel free to search about it anyway.
If you're familiar with this concept, you should know a bit about the linux's ELF format and it's sections. Don't hesitate to document yourself about it aswell.

You saw what GDB's about, that's cool! Now let's learn a little about `objdump`. It's a prorgam that can show you a lot about file objects, so everything tied to compilation (your binary for example). Here are some random options :
- `-D` Display assembler content of your binary and it's different sections
- `-x` Display all the headers informations
- `-EB` Assume Big Endian
- `-EL` Assume Little Endian
`man objdump` is your friend :)

This program is crypted ! There should be a key somewhere that could help me decrypt it.. 

Find the encryption key in the ELF sections.

Flag format: `PoC{key}`

`key` is 17 bytes long. It must be submitted in base 16.


# 5 - Alien

*Challenge name: alien*

The *alien* binary is different from what we have encountered so far. Find out why and try to flag the challenge anyway.
Find the flag !

## 6 - Robbery
This is an x64 ELF polymorphic binary.

Find the real instruction at offset `401ad1`.

Flag format: `PoC{ins}`

`ins` is the instruction and it's operand(s), as seen in a disassambler, but the binary is still crypted..
Get back to GDB!

<details>
  <summary>hint</summary>
This instruction is found in a malicious function.  
</details>

## 7 - Gladiator
It’s time to use your knowledge in a typical CTF exercice. The _gladiator_ binary will take you through various way to check an input. Each step has its own logic : you have to find ways to go and to validate the final step. Try to strictly apply all the techniques you have learnt before !
# Cutter
GDB and PEDA are good tools but when we face complex / heavy programs, it’s hard to make an efficient analysis. That’s why today we are going to learn how to use Cutter, a GUI tool built on top of  [Radare2](https://github.com/radareorg/radare2)  This tool is great because it features :

-   a clean and efficient interface
-   a good integration of the Ghidra decompiler (a decompiler deduces the C code from the binary asm instructions).  [Ghidra](https://github.com/NationalSecurityAgency/ghidra)  was developped and released by the NSA.
-   a built-in debugger

Discover and install Cutter [here](https://cutter.re).

![cutter img](https://cutter.re/assets/images/cutter_head_light_theme.png)

## 0 - hash
Cutter gives you a nice dashboard every time you load a binary. Try to check it out on this binary and find the sha1 hash to validate the challenge.
## 1 - strings
A string containing the flag is hidden in this binary. Try to find at which address it is located with Cutter. When you have the address, you validate this challenge.
## 2 - imports
What is the name of the function imported in the binary from the magic library ?
## 3 - graph
This challenge does various checks on your input. With the Graph view of Cutter, try to understand what the code is doing and find an input that matches all the checks !
## 4 - patching
This challenge is litteraly impossible to solve. Try to edit it with Cutter to get the victory print !
## 5 - checks
This program is a brand new ultra-secured password checking system. Can you break it ?

You may use the Graph, the Disassembly and the Decompiler views but you SHOULD NOT use the patching features provided by Cutter.
## 6 - mycraft
I can't play a game of MyCraft, it keeps telling me "Wrong Licence" .... :'(

HELP MEEEEEEEEEEEEEEEEEEEEEEEEE

Download the files here : https://pwnh4.com/poc-workshop-craft.zip 

When you have unzip this folder, you have to :

1. Install libcurl4-openssl-dev with your system packet manager, if not already installed
2. Do a `mkdir build && cd build && cmake .. && make && ./craft`

Load the binary in writabe mode in Cutter and use the edition feature to bypass all the licence checks !
## 7 - arena
Welcome to the Arena.

You must defeat all champions to get the flag.

You can use all the Cutter features except patching, which is useless here to get the flag.

May the force be with you !
## 8 - Heroes
All the informations you need are in the challenge description at https://challs.poc-innovation.com.
