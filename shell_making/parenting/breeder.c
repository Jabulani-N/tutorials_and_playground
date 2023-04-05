#include <stdio.h>
#include <unistd.h>
#include 
int main(void)
{
	int forkReturn;
	printf("It begins...\n");
	forkReturn = fork();
	printf("my return for the fork is %i", forkReturn);

	return (0);
}
