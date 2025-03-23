#include "includeme.h"

int main (void)
{
	int mypid, parentpid;

	mypid = getpid();
	parentpid = getppid();
	printf("my pid is %i and my parent's pid is %i\nThese are both pid_t, which is fancy for 'int'\n", mypid, parentpid);
	return(0);
}

