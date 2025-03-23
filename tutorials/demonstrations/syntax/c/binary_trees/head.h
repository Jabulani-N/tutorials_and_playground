

/*
 * subject wrote the entie header file before beginning livecode
 * though clevr, gives less time for notetaking
 */


#ifndef ROFL
#define ROFL

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>


struct binary_tree_s
{
	int n;
	struct binary_tree_s *mama_sama;
	struct binary_tree_s *left;
	struct binary_tree_s *right;
};
typedef struct binary_tree_s binary_tree_t;

binary_tree_t *add_node(binary_tree_t *parent, int value);
binary_tree_t **create_node(int value);


#endif
