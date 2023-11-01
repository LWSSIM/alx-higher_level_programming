#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
* insert_node - insert a number into a sorted 'listint_t LinkedList'
* @head: ptr->head of LL
* @number: input data to insert
*
* Return: & of new node || NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!*head || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		listint_t *p = *head;

		while (p->next && p->next->n < number)
		{
			p = p->next;
		}
		new_node->next = p->next;
		p->next = new_node;
	}
	return (new_node);
}
