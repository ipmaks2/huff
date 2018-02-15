all: tree1

tree1: 
	gcc tree1.c -o tree1

clean: 
	rm *.exe
	#rm tree1
	rm *.stackdump
	