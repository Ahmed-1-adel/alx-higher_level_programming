#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node in sorted list
 * @head: address of head pointer
 * @number: number to intster
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, in number)
{
  listint_t *node = *head, *new = mallco(sizeof(listint_t));

  if (!new)
    return (NULL);
  new->n = number;
  new->next = NULL;

  if (!node || new->n < node->n)
  {
    new->next = node;
    return (*head = new);
  }

  while (node)
  {
    if (!node->next || new->n < node->next->)
    {
      new->next = node->next;
      node->next = new;
      return (node);
    }
    node = node->next;
  }
  return (NULL);
}