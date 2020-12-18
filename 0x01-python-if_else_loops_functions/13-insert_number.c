#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: refrence to head
 * @number: number to be added
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node;
    listint_t *temp = *head;

    if (head == NULL && number != '\0')
        return (NULL);

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }
    while (head != NULL)
    {
        if (new_node->n < temp->next->n && new_node->n > temp->n)
        {
            new_node->next = temp->next;
            temp->next = new_node;
            return (new_node);
        }
        temp = temp->next;
    }
    return (NULL);
}
