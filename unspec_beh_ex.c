/* Welcome to the Interactive C Tutorial.
Start by choosing a chapter and
write your code in this window. */

#include <stdio.h>
#include <limits.h>
#define NUMBER 0

int sum(int a, int b)
{
    return a + b;
}

int main() {
    int n = sum(printf("hello "), printf(" World!")); // order of arg evaluation - unspec, not an error
    printf ("\n%d\n", n);

    printf("%zu\n", sizeof(int)); // implementation defined behavior, not an error
    printf("%zu\n", sizeof(long int));
    printf("%zu\n", sizeof(long long int));

    // undefined beh - it is always error in program
    // check list of such in standard
    int x = INT_MAX;
    printf("%u\n", (x+1)>0);
    
    // observable behavior
    read and write voliatile
    call to library I/O functions

    // other are unobservable behavior and could be optimized by compilator
    // when we do not expect this, as example empty cycles.
    // memset() - as example - could be skipped as optimization on the end of other function



    // printf("%d\n", NUMBER);
    return 0;
}


/*

   1  cd src
   2  dir
	   3  exit
   4  gcc
   5  gcc hworld.c -S
   6  gcc hworld.c --save-temp
   7  ll
   8  ls
   9  ls -l
  10  gcc hworld.c --save-temp
  11  gcc hworld.c -v --save-temp
  12  gcc hworld.c -v --save-temp
  13  ./a.exe
  14  gcc hworld.c -v
  15  gcc hworld.c -v
  16  ./a.exe
  17  ldd a.exe
  18  objdump a.exe
  19  objdump -S a.exe
  20  objdump -S a.exe
  21  objdump -S a.exe | less
  22  hist
  23  history

unspecified behavior
undefined  behavior
implementation defined behavior
*/





/*
Practice: Implementing Huffman archiver)



*/