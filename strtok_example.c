#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main (void)
{ /*playng with strtok*/
	/*you can change stringy down here to whatever you wanna experiment on*/
	char *output, stringy[] = "word1 word2,word3.word4", *delim = "\t \n,.", *scapegoat;
	/*you can also use whatever you want to be the delimiter. even "r" is a valid one*/

	scapegoat = malloc(sizeof(stringy));
	scapegoat = strcpy(scapegoat, stringy);
	/*scapegoat will get shredded instead of stringy*/
	printf("\nthe string, 'stringy' started as [%s]\n\n", stringy);
	printf("the delimiters are stored in 'delim' (you can name it anything), and has [%s] (there is a space and tab in there)\n\n", delim);
	printf("becauase strtok will shred whtever you feed it, do: \n\nscapegoat=malloc(sizeof(stringy));\nstrcpy(scapegoat, stringy);\n\nIn order to protect the original string.\n\n");
	output = strtok(scapegoat, delim);
	printf("now if we do\noutput = strtok(scapegoat,delim)\noutput becomes [%s], but scapegoat also becomes [%s]\n\n", output, scapegoat);

	printf("stringy, however, survives, and is still [%s]\n", stringy);

	printf("if you do it agian, but type\n\noutput = strtok(NULL, delim)\n\n");
	output = strtok(NULL, delim);
	printf("then...\noutput will equal [%s]\nscapegoat will equal [%s]\nstringy will equal [%s]\n", output, scapegoat, stringy);

	free(scapegoat);

	return (0);
}

/*
 * potential pitfalls
 *
 * you can modify (and therefore use strtok on) stringy[]="content"
 * you canNOT modify (and therefore use strtok on) *stringy="content"
 *
 * you canNOT make a char pointer = a char array
 * char *ptr;
 * char array[];
 *  ptr = arrray; DOES NOT WORK
 */
