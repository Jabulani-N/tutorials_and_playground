/**
 *
 */
#include "includeme.h"

int main (int ac, char **av, char **env)
{
	unsigned int i = 0;

	(void) ac;
	(void) av;

	while (env[i])
	{
		printf("env[%i]:\n%s\n\n", i, env[i]);
		i++;
	}
	return (0);
}

