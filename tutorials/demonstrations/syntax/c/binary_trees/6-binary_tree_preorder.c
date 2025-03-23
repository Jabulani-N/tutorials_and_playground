#include "binary_trees.h"
#include <stdlib.h>

/**
 * binary_tree_preorder - function that goes through a binary tree
 *	using pre-order traversal
 * @tree: pointer to the root node of the tree
 *	it's only the root node the first instance of htis funct
 *	recursive calls will NOT be the root.
 * @func: pointer to a function to call for each node
 *
 * Return: don't
 */
void binary_tree_preorder(const binary_tree_t *tree, void (*func)(int))
{
	if (!tree || !func)/*quit if either is not given properly*/
		return;

	printf("i'm the pre-order function run on the node containing!%i\n", tree->n);
	/*func is provided*/
	printf("I'm the node contatining %i, and I'm about to run the funciton on myself!", tree->n);
	func(tree->n);/*run the function on myself*/
	binary_tree_preorder(tree->left, func);/*run this whole operation on left*/
	binary_tree_preorder(tree->right, func);
}

