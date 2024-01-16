#include "lists.h"

/**
 * insert_node - This function adds a new node to a singly linked list
 * @head: The head node of the singly linked list
 * @number: The number to be inserted into the singly linked list
 * Return: The address of the new node on success; NULL on failure
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newNode, *current, *prev;

    newNode = (listint_t *)malloc(sizeof(listint_t));

    if (newNode == NULL)
        return NULL;

    newNode->n = number;
    newNode->next = NULL;

    current = *head;

    if (current == NULL || current->n >= number)
    {
        newNode->next = current;
        *head = newNode;
        return (newNode);
    }

    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    prev->next = newNode;
    newNode->next = current;
    return (newNode);
}
