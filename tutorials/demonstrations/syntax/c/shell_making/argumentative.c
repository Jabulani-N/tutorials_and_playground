/*this program prints the input arguments
 * the first argumebt tends to be the program's name
 * @ac: automatically is the numebr of inout arguments.
 *	usualy has an extra +1 because calling the function counts as an argument
 * @av: array of each input argument
 * Return: 0 because it doesn't matter
 */

#include "includeme.h"

int main (int ac, char **av)
{
	int pos = 0;


	while (av[pos])
	{
		printf("argument number %i stored in av[%i] is %s\n", pos, pos,av[pos]);
		/*av++;*//*I accidentally dud av++ at first, which also works, but won't track pos the same way*/
		pos++;
	}
	printf("ac is %i\nwhile( av[pos]) terminated at pos=%i\n", ac, pos);

	return (0);
}
