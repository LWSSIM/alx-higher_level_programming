#include "lists.h"

/**
* check_cycle - check wether a linked list contains a cycle [slow:fast] method
* @list: pointer to linked list head
*
* Return: 0>No_cycle || 1>Cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);

	slow = fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
