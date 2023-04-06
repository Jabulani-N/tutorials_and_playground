### exxecve is how you open another program

it closes the function that called it, and begins a new process.

- the new one gets it's own new heap, stack, etc.

`
int execve(const char *pathname, char *const argv[], char *const envp[]);
`

argv[] is an array of arguments to open pathname with.

- convention says to make argv[0] be the name of the called function, the same way an automatic argv[0] or av[0] would be.


envp[] is 
