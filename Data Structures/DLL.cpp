#include<iostream>
#include<conio.h>
#include<cstdlib>
using namespace std;
template <class T> class Node
{	public:
	T info;
	Node <T> *next,*prev;
	Node(T data)
	{
		info=data;
		next=prev=NULL;
	}
};
template <class T> class DLL
{	private:
		Node <T> *head,*tail;

		void insertAtBeg(T data)
		{
			Node <T> *temp=new Node<T> (data);;
			if(head==NULL)
				head=tail=temp;
			else
			{
				temp->next=head;
				head->prev=temp;
				head=temp;	
			}
		}
				
		void insertAtEnd(T data)
		{
			Node <T> *temp=new Node<T>(data);;
			if(head==NULL)
				head=tail=temp;
			else
			{
				tail->next=temp;;
				temp->prev=tail;
				tail=temp;	
			}
		}
					
		void insertAtPos(T data,int pos)
		{
			Node <T> *temp=new Node<T>(data);
			if(head==NULL)
				head=tail=temp;
			else if(head==tail && pos>1)
				insertAtEnd(data);
			else if(pos==1)
				insertAtBeg(data);
			else
			{
				Node <T> *current=head;				
				while(pos>2&&current->next!=NULL)
					{
						current=current->next;	
						pos--;
					}
				if(current->next==NULL)
					insertAtEnd(data);
				else
				{
					temp->next=current->next;
					current->next=temp;
					temp->prev=current;
					current=current->next->next;
					current->prev=temp;
				}
				
			}
		}
				
		T deleteBeg()
		{	
			T val;
			if(head==NULL)
				throw "\n Linked List Empty";
			else if (head==tail)
				{
					val=head->info;
					delete head;
					head=tail=NULL;
					return val;
				}
			else 
				{
					val=head->info;
					head=head->next;
					delete head->prev;
					return val;
				}
		}
			
		T deleteEnd()
		{	
			T val;
			if(head==NULL)
				throw "\n Linked List Empty";
			else if (head==tail)
				{
					val=head->info;
					delete head;
					head=tail=NULL;
					return val;
				}
			else 
				{
					val=tail->info;
					tail=tail->prev;
					delete tail->next;
					tail->next=NULL;
					return val;
				}
		}
	
		void deleteData(T data)
		{
			if(head==NULL)
				throw "\n Linked List Empty";
			else if (head==tail)
				{
					if(head->info==data)
						deleteBeg();
					else
						throw "\n No such data in Linked List";
				}
			else if(head->info==data)
				deleteBeg();
			else if(tail->info==data)
				deleteEnd();
			else 
				{
					Node <T> *current=head;
					while(current->info!=data&&current!=tail)
						current=current->next;
					if(current!=tail)
						{
							current->prev->next=current->next;
							current->next->prev=current->prev;
							delete current;
						}
					else
						throw "\n No such data in Linked List";						
				}
		}
							
		void count()
		{
			Node <T> *current=head;
			int count=0;
			while(current!=NULL)
				{
					current=current->next;				
					count++;
				}
			if(count ==0)
				throw "Linked List is empty\n ";
			else
			cout<<"\n Total Elements in Linked List "<<count;
		}

		void display()
		{	
			Node <T> *current=head;
			if(current!=NULL)
			{
				int count=1;
				while(current!=NULL)
				{	
					cout<<"S.NO. "<<count++<<".\t"<<current->info<<"\n";			
					current=current->next;				
				}
			}
			else
				cout<<"\n Empty Linked List";
		}
			
		void reverse()
		{
			if(head!=NULL&&head!=tail)
			{
				bool tf=1;
				Node <T> *current=head;
				while(tf)
				{				
					Node <T> *temp=current->prev;
					current->prev=current->next;
					current->next=temp;
					current=current->prev;
					if(current==NULL)
					{
						temp=head;
						head=tail;
						tail=temp;
						tf=0;
					}
				}	
			}			
		}
		
		bool isPresent(T data)
		{	
			int f=0;
			Node <T> *temp=head;
			while(temp!=NULL)
			{	
				if(temp->info==data)
					{
						f=1;
						break;
					}
				temp=temp->next;
			}
			if(f==1)
				return 1;
			else
				return 0;				
		}

		
		int menu()
		{	
			int ch;
			cout<<"\n MENU\n";
			cout<<"1. Insert At Beginning\n";
			cout<<"2. Insert At End\n";
			cout<<"3. Insert At Particular Position\n";
			cout<<"4. Delete At Beginning\n";
			cout<<"5. Delete At End\n";
			cout<<"6. Delete At Particular Data\n";
			cout<<"7. Check if Data is present or Not\n";
			cout<<"8. Reverse\n";
			cout<<"9. Count the number of elements\n";
			cout<<"10. Display\n";
			cout<<"11. EXIT\n";
			cout<<"ENTER CHOICE\n";
			cin>>ch;
			return ch;
		}
	public:
		DLL()
		{
			head=tail=NULL;
		}
		void prog()
		{	
		T data;		
		int posdata, ch;
			do
			{	
			ch=menu();
			try
			{			
			switch(ch)
			{
				case 1: cout<<"Enter data to be inserted\n";
						cin>>data;
						insertAtBeg(data);
				break;
				case 2: cout<<"Enter data to be inserted\n";
						cin>>data;
						insertAtEnd(data);
				break;
				case 3: cout<<"Enter data to be inserted\n";
						cin>>data;
						cout<<"Enter postion at which insert needed\n";
						cin>>posdata;
						insertAtPos(data,posdata);
				break;
				case 4: data=deleteBeg();
						cout<<"Deleted data value at Beginning: "<<data<<"\n";							
				break;			
				case 5: data=deleteEnd();
						cout<<"Deleted data value at End: "<<data<<"\n";	
				break;
				case 6: cout<<"Enter data to be deleted\n";
						cin>>data;
						deleteData(data);					
				break;
				case 7:	cout<<"Enter data to be searched\n";
						cin>>data;
						if(isPresent(data))
							cout<<"Data is present\n";
						else
							cout<<"Data is not present\n";							
				break;		
				case 8: cout<<"Old Linked List\n";
						 display();				
						 reverse();
						 cout<<"Reversed Linked List\n";
						 display();	
				break;			
				case 9:count();
				break;
				case 10:display();
				break;
				case 11:exit(0);
				break;				
				default:cout<<"\nEntered Choice is Wrong\n";				
				exit(0);
			}
			}
			catch (const char* c)
				{
					cout<<c;
				}
						
			}while(true);
		}
};
int main()
{
	DLL <int> LL;
	LL.prog();
	getch();
}
