#include "binary_trees.h"

/**
 * binary_tree_balance - measures the balance factor of a binary tree
 * @tree: pointer to the root node of the tree to measure the balance factor
 *
 * Return: the balance factor
 *         0 if tree is NULL
 */
int binary_tree_balance(const binary_tree_t *tree)
{
	int h_left, h_right;

	if (!tree)
		return (0);

	h_left = tree->left ? (int)binary_tree_height(tree->left) : -1;
	h_right = tree->right ? (int)binary_tree_height(tree->right) : -1;

	return (h_left - h_right);
}
