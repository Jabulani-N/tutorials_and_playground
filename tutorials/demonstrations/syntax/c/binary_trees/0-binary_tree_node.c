#include "binary_trees.h"
#include <stdlib.h>

/**
 * binary_tree_node - creates binary tree node
 * @parent : pointer
 * @value : value of node
 * Return: created node
 */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *node = malloc(sizeof(binary_tree_t));

	if (node ==  NULL)/*if malloc failed*/
		return (NULL);


	node->parent = parent;
	node->n = value;
	node->left = NULL;
	node->right = NULL;
	/*node initialized with parent*/
	return (node);
}

