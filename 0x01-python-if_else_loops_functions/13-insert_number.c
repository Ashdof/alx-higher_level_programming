#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - add a new node to a sorted singly linked list
 * @head: a reference pointer to the head of the singly linked list
 * @number: the new value to add to the linked list
 *
 * Return: address of new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *p;

	if (*head == NULL)
		return (NULL);

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;

	if ((*head)->n >= number)
	{
		newnode->next = *head;
		*head = newnode;

		return (newnode);
	}

	p = *head;
	while (p && p->next && p->next->n < number)
		p = p->next;

	newnode->next = p->next;
	p->next = newnode;

	return (newnode);
}
