#include <stdio.h>
#include <stdlib.h>
#define NUMBER 0


struct tHuffNode {
    char* desc ;
    struct tHuffNode* l;
    struct tHuffNode* r; 
    char value ;  
} ;

struct tHuffNode * newNode(void){
   struct tHuffNode * buffer;
   buffer = (struct tHuffNode*) malloc(sizeof(struct tHuffNode));
   if (buffer == NULL) {
       printf("Error creating new node\n");
       exit(1);
   }
}
int main() {
    char text[] = "This is test ing text for build ing bin tree, used in arhiving tool.\n";
    struct tHuffNode* rootNode;
    printf(text);
    rootNode = newNode(); 
    // free mem - all nodes
    free(rootNode);
    return 0;
}


/*

   5  gcc hworld.c -S
   6  gcc hworld.c --save-temp
  15  gcc hworld.c -v
  17  ldd a.exe
  19  objdump -S a.exe

unspecified behavior
undefined  behavior
implementation defined behavior


*/
