/**
 * main - right back at ya
 * Return: the numebr of characters you entered
 */


#include "includeme.h"

int main (void)
{ /*getline and everything in it are VERY particular*/
	/*even the slightest change will break it and return -1*/
	char *holder;
	int i = 0;
	size_t j = 0;

	printf("tell me words～♡\n$ ");
	i = getline(&holder, &j, stdin);/*becuase we're starting at NULL and 0, getline will allocate for us*/
	printf("I got %i characters from you☆\nThey are:\n%s\nThat's right. The newline counts as a charaacter.\n", i, holder);

	free(holder);
	/*yes, you do NEED TO FREE what getline allocates*/
	return (i);
}

