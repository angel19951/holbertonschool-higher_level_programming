#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - check if a linked list has a cycle
 * @list: list to check
 * Return: 0 if the is no cycle || 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL)
	{
		return (0);
	}

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
	slow = slow->next;
	fast = fast->next->next;
		if (slow == fast)
		return (1);
	}
	return (0);
}
