#include <iostream>

using namespace std;

class node{
    public:
        int data;
        node *next;
};
node *start=NULL;
node *last = NULL;

void createnode(int n)
{
    node *tmp = new node;
    tmp->data = n;
    
    if (last==NULL)
    {
        last = tmp;
        tmp->next = last;
    }
    else
    {
        tmp->next = last->next;
        last->next = tmp;
        last = tmp;
    }
}

void insertbeg(int n)
{
    node *tmp = new node;
    tmp->data = n;
    if (last==NULL)
    {
        last = tmp;
        tmp->next = last;
    }
    else
    {
        tmp->next = last->next;
        last->next = tmp;
    }
    
}
void insertend(int n)
{
    node *tmp = new node;
    tmp->data = n;
    if (last==NULL)
    {
        last = tmp;
        tmp->next = last;
    }
    else
    {
        tmp->next = last->next;
        last->next = tmp;
        last = tmp;
    }
    
}
void display()
{
    node *s;
    if (last==NULL)
    {
        cout<<"List does not exist:"<<endl;
    }
    s=last->next;
    while(s!=last)
    {
        cout<<s->data<<" ";
        s =s->next;
    }
    cout<<s->data<<endl;
}

void insert(int n, int pos)
{
    node *tmp = new node;
    tmp->data = n;
    node *s;
    if (pos==1)
        insertbeg(n);
    else if(last==NULL)
        createnode(n);
    else
        s=last->next;
        for (int i=0;i<pos-1;i++)
            s=s->next;
        tmp->next = s->next;
        s->next=tmp;
        
    
}

void deletebeg()
{
    if (last->next == last)
    {
        delete(last);
        last = NULL;
    }
    else
    {
        node *ptr;
        ptr= last->next;
        last->next = ptr->next;
        delete(ptr);
    }
    
}
void deleteend()
{
    if (last->next == last)
    {
        delete(last);
        last = NULL;
    }
    else
    {
        node *ptr;
        ptr = last;
        while(ptr->next!=last)
            ptr = ptr->next;
            
        ptr->next = last->next;
        delete(last);
        last = ptr;
        
    }
}
void deletespec(int val)
{
    if (last==NULL)
        cout<<"The list does not exist"<<endl;
    node *ptr,*tmp = last;
    if (tmp->data == val)
        deleteend();
    else if(tmp->next->data == val)
        deletebeg();
    else if
        {
            ptr = last->next;
            while(ptr->next!=last)
            {   
                if(ptr->next->data == val)
                {    
                    tmp = ptr->next;
                    ptr->next = tmp->next;
                    delete(tmp);
                
                }
                ptr = ptr->next;
            }        
        }
    else
        cout<<"Value not Found:"<<endl;
}


int main()
{   
    
    createnode(5);
    createnode(10);
    createnode(15);
    insertbeg(1);
    insertend(20);
    display();
    deletespec(1);
    display();
    
    
    return 0;
}
