
#include "includeme.h"


		/**
		 * main - execve example
		 *
		 * Return: Always 0.
		 */
int main(void)
{
  char *exampleArgv[] = {"/bin/ls", "-l", "/usr/", NULL};
  /**argv[] = {address of what gets run, av[1], av[2], NULL*/
  /*you can use an explicit address or a relative address*/
  /*this is literally just a ways of saying 
   *	/bin/ls -l /usr/
   */

  printf("Before execve\n");
  if (execve(exampleArgv[0], exampleArgv, NULL) == -1)
    {
      perror("Error:");
    }
  printf("After execve\n");
  return (0);
}
