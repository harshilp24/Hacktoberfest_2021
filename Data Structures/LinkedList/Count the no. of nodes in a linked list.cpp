#include <iostream>
using namespace std;

struct Node
{
	int data;
	Node *next;
};
Node* insertAtBeg(Node *ptr)
{   
    int a;
	Node *temp= new Node();
	cout<<"Enter the data to be inserted at the beginning of the linked list  - \n";
	cin>>a;
	temp->data = a;
	temp->next = ptr;
	ptr = temp;
	return ptr;
}

int Count (Node *ptr)
{
    int count=0;
    while(ptr)
    {
        count++;
        ptr=ptr->next;
    }
    return count;
}
Node* display(Node *ptr)
{
	while(ptr!=NULL)
	{
		cout<<ptr->data<<" ";
		ptr = ptr->next;
	}
	cout<<"\n";
}
int main()
{   Node* Head = NULL;
    int num; 
	while(1)
	{
		cout<<"1. Enter 1 to insert an element in linked list\n2. Enter 2 to display element of a linked list\n3. Count the no. of nodes in a linked list\n4. Exit\nEnter you choice : ";
		cin>>num;
		switch(num)
		{
			case 1: Head = insertAtBeg(Head);
			        break;
			case 2: display(Head);
			        break;
			case 3: cout<<Count(Head);
			        break;
			case 4: exit(0);				  
		}
	}
	return 0;
}