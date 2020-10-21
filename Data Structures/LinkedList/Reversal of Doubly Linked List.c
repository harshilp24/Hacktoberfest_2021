#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *next;
    struct node *prev;
};
typedef struct node Node;
Node *head, *newnode, *tail;
void create()
{
    head = 0;
    //Node *tail;
    int choice = 1;
    while (choice != 0)
    {
        newnode = (Node *)malloc(sizeof(Node));
        printf("Enter data for Doubly Linked List: ");
        scanf("%d", &newnode->data);
        newnode->prev = 0;
        newnode->next = 0;
        if (head == 0)
        {
            head = tail = newnode;
        }
        else
        {
            tail->next = newnode;
            newnode->prev = tail;
            tail = newnode;
        }
        printf("Do you wanna continue(1 or 0)?");
        scanf("%d", &choice);
    }
    tail->next = 0;
    //printf("%p\n",tail);
}
void display()
{
    Node *temp;
    ;
    temp = head;
    while (temp != 0)
    {
        printf("%d==>", temp->data);
        // printf("\n%p\n",tail);
        temp = temp->next;
    }
    printf("NULL\n");
    f
}
void reverse()
{
    Node *current, *nextnode;
    if (head == 0)
    {
        printf("NULL");
    }
    else
    {
        current = head;
        while (current != 0)
        {
            nextnode = current->next;
            current->next = current->prev;
            current->prev = nextnode;
            current = nextnode;
        }
        current = head;
        head = tail;
        tail = current;
    }
}
int main()
{
    create();
    display();
    reverse();
    display();
    return 0;
}
