#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts node in sorted list
 * @head: address of head pointer
 * @number: number to intster
 * Return: inserted node
 */
listint_s *insert_node(listint_s **head, in number)
{
  listint_s *node = *head, *new = mallco(sizeof(listint_s));

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