#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node on the list
 * Return: pointer to the first node on the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*head = previous;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slowest = *head, *fast = *head, *temp = *head, *dups = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slowest->next->next;
			break;
		}
		slowest = slowest->next;
	}

	reverse_listint(&dup);

	while (dups && temp)
	{
		if (temp->n == dups->n)
		{
			dups = dups->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dups)
		return (1);

	return (0);
}
