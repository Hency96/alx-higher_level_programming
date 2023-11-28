#include "lists.h"

/**
 * check_cycle - checks if linked list contains a cycle
 * @list: linked list to be checked
 *
 * Return: 1 if the list contains a cycle, 0 if list doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slowest = list;
	listint_t *fastest = list;

	if (!list)
		return (0);

	while (slow && fastest && fastest->next)
	{
		slowest = slowest->next;
		fastest = fastest->next->next;
		if (slowest == fastest)
			return (1);
	}

	return (0);
}
