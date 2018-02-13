#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define  CHARBLOCK 10
#define  DEBUG 1

struct tHuffNode {
    char* value;
    int   size;
    int   count;
    struct tHuffNode* l;
    struct tHuffNode* r; 
    
} ;


int check_buff( void* buff ){
    if (buff == NULL) {
        printf("Error while allocating new memory\n");
        exit(1);
    }
   
    return 0;
}

struct tHuffNode * newNode(void){
   struct tHuffNode * buffer;
   char * charbuff;
   buffer = (struct tHuffNode*) malloc(sizeof(struct tHuffNode));
   check_buff(buffer);

   charbuff = malloc(sizeof(char) * CHARBLOCK  );
   check_buff(charbuff);

   memset(charbuff, 0, sizeof(char)*CHARBLOCK);
   buffer->size = CHARBLOCK;
   buffer->value = charbuff;
   buffer->count = 0;

   return buffer;

}

void appendNode(struct tHuffNode*  p,  char c){
     if (! strlen(p->value) && (!p->count)) {
         memset( p->value, c, sizeof(char)*1);  
         p->count = 1;
     } 
     else {
         if (p->value == c) {
             p->count++;
         } 
         
         else {

             while (p->l) {
                 p = p->l;
             }
           
         p = newNode();
         memset( p->value, c, sizeof(char)*1);  
         p->count = 1;

     }

     printf("Value:%s\n", p->value);
     printf("Count:%d\n", p->count);
     printf("Size: %d\n", p->size);
}    



int main() {
    char text[] = "This is testing text for building bin tree, used in arhiving tool.\n";
    // TODO chech with \0 character later
    struct tHuffNode* rootNode;
    printf("%s\n", text);
    rootNode = newNode(); 

    for (int i =0; text[i] != 0; i++) {
        // printf("%c\n", text[i]);
        appendNode(rootNode,text[i]);
    }

    // TODO free mem - for all nodes
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

