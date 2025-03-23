#include "includeme.h"

/**
 * main - forks, and makes child do something differernt from parent
 * Return: 0 if child; non-zer int if parent
 */

int main (void)
{
	int adultsOnly;

	printf("before fork\n");
	adultsOnly = fork();/*fork() returns 0 for the child. non-zero for parent*/
	if (adultsOnly)/*0 = false. !0 = true*/
		printf("I'm the parent!\n");
	else
		printf("I'm the child, and my days are numbered!\n");
	printf("my pid is %i\nmy parent's pid is %i\n\n", getpid(), getppid());

	return (adultsOnly);
}

