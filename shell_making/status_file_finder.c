/**
 * main - does main things
 * @ac: number of input agruments + 1
 * @av: aray of input args, starting with calling name.
 * Retrun: always 0
 */

#include "includeme.h"
int main (int ac, char **av)
{
	int i=1;
	struct stat st;

	if (ac < 2)
	{
		printf("lol no.\nyou need to call me with another file's name.\n");
		return (0);
	}
	while (av[i])
	{
		printf("file [%s]", av[i]);
		if (stat(av[i], &st)) /*it looks like this is the struct that'll hold stat data*/
		{
			printf(" was found.\n");
		}	
		else
		{
			printf(" was not found.\n");
		}
		i++;
	}
	return (0);
}

