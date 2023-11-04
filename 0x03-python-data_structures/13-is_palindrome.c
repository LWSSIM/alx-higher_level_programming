#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: ptr->linked_list
 *
 * Return: 0->False || 1->True
 */
int is_palindrome(listint_t **head)
{
	listint_t *p1, *p2;
	int count = 0;

	if (!head)
		return (1);

	p1 = *head;
	for (p2 = *head; p2->next != NULL; p2++)
		count++;
	while (count)
	{
		if (p1->n != p2->n)
			return (0);
		p1++, p2--, count--;
	}
	return (1);
}
