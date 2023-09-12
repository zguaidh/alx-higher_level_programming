#include "lists.h"
/*
 *check_cycle - checks if a singly linked list has a cycle in it
 *
 *@list: the head of the list
 *
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *check = list;

	while (list != NULL && list->next != NULL)
	{
		current = current->next;
		check = check->next->next;
		if (current == check)
		{
			return (1);
		}
	}
	return (0);

}
