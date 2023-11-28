#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/* Definition for singly-linked list node */
typedef struct listint_t
{
  int data;
  struct listint_t *next;
} listint_t;

/* Function to insert a number into a sorted singly linked list */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new_node = malloc(sizeof(listint_t));
  if (new_node == NULL)
  {
    return NULL; // Allocation failure
  }

  new_node->data = number;
  new_node->next = NULL;

  if (*head == NULL || number < (*head)->data)
  {
    new_node->next = *head;
    *head = new_node;
  }
  else
  {
    listint_t *current = *head;
    while (current->next != NULL && current->next->data < number)
    {
      current = current->next;
    }
    new_node->next = current->next;
    current->next = new_node;
  }

  return new_node;
}

/* Function to print the linked list */
void print_list(listint_t *head)
{
  while (head != NULL)
  {
    printf("%d ", head->data);
    head = head->next;
  }
  printf("\n");
}

/* Function to free the memory of the linked list */
void free_list(listint_t *head)
{
  while (head != NULL)
  {
    listint_t *temp = head;
    head = head->next;
    free(temp);
  }
}

/* Example usage */
int main()
{
  listint_t *head = NULL;

  // Insert some elements into the sorted linked list
  insert_node(&head, 10);
  insert_node(&head, 5);
  insert_node(&head, 20);
  insert_node(&head, 15);

  // Print the resulting linked list
  print_list(head);

  // Free the memory used by the linked list
  free_list(head);

  return 0;
}
