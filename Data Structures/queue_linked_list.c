#include<stdio.h>
#include<stdlib.h>


void enqueue();
void dequeue();
void display();

typedef struct NODE{
    int data;
    struct NODE *link;
}queue_node;


queue_node *front;
queue_node *rear;

int main(){
    int choice;
    while(1){
        printf("Enter your option.\n 1.Enqueue\n 2.Dequeue\n 3.Display\n 4.Exit\n");
        scanf("%d",&choice);
        switch(choice){
            case 1 : enqueue();
                     break;
            case 2 : dequeue();
                     break;
            case 3 : display();
                     break;
            case 4 : exit(0);
            default: printf("Wrong input! Try again.\n");
                     break;
        }
    }
    return 0;
}
void enqueue(){
    queue_node *p = malloc(sizeof(queue_node));
    int element;
    if(p == NULL){
        printf("overflow.\n");
    }
    else{
        printf("Enter element: \n");
        scanf("%d",&element);
        p->data = element;
        if (front == NULL){
            front = p;
            rear = p;
            front->link = NULL;
            rear->link = NULL;
        }
        else{
            rear->link = p;
            rear = p;
            rear->link = NULL;
        }
    }
}
void dequeue(){
    if(front==NULL){
        printf("underflow\n");
    }
    else{
        printf("Deleted element is : %d\n",front->data);
        p = front;
        front =front->link;
        free(p);
    }
}

void display(){
    queue_node *p;
    p = front;
    if(front==NULL){
        printf("Queue is empty.\n");
    }
    else{
        printf("Queue values are:\n");
        while(p != NULL){
            printf("%d \n",p->data);
            p = p->link;
        }
    }
}


        




