#include "monty.h"

/**
 * get_free - function that frees stack
 * @stack: pointer to the top of the stack
 *
 * Return: see below
 * 1. upon success, nothing
 * 2. upon fail, EXIT_FAILURE
 */


void get_free(stack_t *stack)
{
	if (stack)
	{
		get_free(stack->next);
		free(stack);
	}
}
