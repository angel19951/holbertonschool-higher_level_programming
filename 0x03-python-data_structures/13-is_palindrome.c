#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is palindrome.
 * @head: head of the list
 * Return: 0 if the list is not palindrome
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL && (*head)->next == NULL)
		return (1);

	listint_t *rev_list = reverse_list(*head);

	while (head != NULL && rev_list != NULL)
	{
		if ((*head)->n != rev_list->n)
			return (0);
		(*head) = (*head)->next;
		rev_list = rev_list->next;
	}
	return (1);
}

/**
 * reverse_list - reverses a linked list for comparison
 * @head: head of the list
 * Return: new reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *reversed = NULL;
	listint_t *temp;

	while (head != NULL)
	{
		temp = malloc(sizeof(listint_t));
		if (temp == NULL)
			return (NULL);
		temp->n = head->n;
		temp->next = reversed;
		reversed = temp;
		head = head->next;
	}
	return (reversed);
}
