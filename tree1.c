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



int is_present(char * string, char c){
    for (int i=0; string[i]!=0; i++){
        if (string[i] == c)
            return 1;
    }
    return 0;
}

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
   buffer->l = NULL;
   buffer->r = NULL;

   return buffer;

}

int debugnode(struct tHuffNode* p) {
    
    printf("Value:'%s'\n", p->value);
    printf("Count:%d\n", p->count);    
    printf("Node address %d\n", p); 
}

int debuglog(char* message, struct tHuffNode* p){
    if ( DEBUG ){
        printf(message);
        printf("\n");
        debugnode(p);
    }    
}    

int appendNodeL(struct tHuffNode*  p,  char c){
    int i = 0;
    printf("\nStartd cycle for letter %c\n", c); 
    do 
    {
     if (! strlen(p->value) && (!p->count)) {
         memset( p->value, c, sizeof(char)*1);  
         p->count = 1;
         debuglog("Added as new value", p);
         
         return 0;
     } 
     else {
         if (is_present(p->value, c)) {
             p->count++;
             debuglog("Increment for existed char", p);
             return 0;
         } 
         
         else {
             // go deeper
             // or
             // create next level
             if (p->l) {
                 p = p->l;
                 debuglog("Go deeper in left tree", p);
             }
             else {
                 p->l = newNode();
                 p = p->l;
                 debuglog("Created new node for left tree", p);
             }
         
         }

     }   
     
    printf("Next cycle %d\n", i++);
    } while (i<=256); // as we have 255 values in a byte, we should not go deeper 256 levels
    return 1; //Error - we reached too deep level
    //printf("Size: %d\n", p->size);
}    



int main() {
    char text[] = "This is testing text for building bin tree, used in arhiving tool.\n";
    // TODO chech with \0 character later
    struct tHuffNode* rootNode;
    printf("%s\n", text);
    rootNode = newNode(); 

    for (int i =0; text[i] != 0; i++) {
        // printf("%c\n", text[i]);
        appendNodeL(rootNode,text[i]);
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

