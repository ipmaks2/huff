/* Welcome to the Interactive C Tutorial.
Start by choosing a chapter and
write your code in this window. */

#include <stdio.h>
#define NUMBER 0
int main() {
    printf("Hello, World!\n");
    printf("%d\n", NUMBER);
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