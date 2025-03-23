
#include "includeme.h"


		/**
		 * main - execve example
		 *
		 * Return: Always 0.
		 */
int main(int ac, char **av)
{

	/**argv[] = {address of what gets run, av[1], av[2], NULL*/
	/*you can use an explicit address or a relative address*/
	/*this is literally just a ways of saying */
	/*	/bin/ls -l /usr/*/


	if (ac < 2)
	{
		printf("usage: programname arguments\n");
		perror("Error:");
		return(0);
	}
	av++;
	printf("Before execve\n");
	if (execve(av[0], av, NULL) == -1)
	{
		perror("Error:");
	}
	printf("After execve\n");
	return (0);
}

