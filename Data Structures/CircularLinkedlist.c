#include<stdio.h>
#include<stdlib.h>
typedef struct CirclLL{
    int data;
    struct CirclLL* link;
}CLL;
CLL* head=NULL;
void create(){
    int element;
    printf("Enter element:");
    scanf("%d",&element);
    CLL *p=malloc(sizeof(CLL));
    p->data=element;
    head=p;
    p->link=head;
    return;
}
void insert_begin(){
    CLL* p=malloc(sizeof(CLL));
    int val;
    printf("Enter a value:");
    scanf("%d",&val);
    p->data=val;
    CLL* m=head;
    while(m->link!=head){
        m=m->link;
    }
    p->link=head;
    m->link=p;
    head=p;
    return;
}
void insert_end(){
    CLL* t=head;
    CLL* p=malloc(sizeof(CLL));
    int val;
    printf("Enter a value:");
    scanf("%d",&val);
    p->data=val;
    while(t->link!=head){
        t=t->link;
    }
    t->link=p;
    p->link=head;
    return;
}
void insert_anywhere(){
    int pos,count=1;
    printf("Enter pos:");
    scanf("%d",&pos);
    CLL* temp=head;
    while(temp->link!=head){
        if(count==pos){
            int x;
            CLL* p=malloc(sizeof(CLL));
            printf("Enter a value:");
            scanf("%d",&x);
            p->data=x;
            p->link=temp->link;
            temp->link=p;
            return;
        }
        temp=temp->link;
        ++count;
    }
    printf("Invalid position\n");
    return;
}
void insert(){
    if(head==NULL){
        create();
    }else{
        int choice;
        while(1){
            printf("Enter choice(1.insert_begin;2.insert_end;3.insert_anywhere;4.exit;):");
            scanf("%d",&choice);
            switch(choice){
                case 1:insert_begin();break;
                case 2:insert_end();break;
                case 3:insert_anywhere();break;
                case 4:return;
            }
        }
    }
}
void delete_begin(){
    CLL* p=head;
    CLL* q=head;
    while(p->link!=head){
        p=p->link;
    }
    p->link=q->link;
    head=q->link;
    printf("%d deleted\n",q->data);
    free(q);
    return;
}
void delete_end(){
    CLL* p=head;
    CLL* q;
    while(p->link!=head){
        q=p;
        p=p->link;
    }
    q->link=head;
    printf("%d deleted\n",p->data);
    free(p);
    return;
}
void delete_anywhere(){
    int pos,count=0;
    CLL* temp=head;
    CLL* p;
    printf("Enter pos:");
    scanf("%d",&pos);
    while(temp->link!=head){
        if(count==pos){
            p->link=p->link->link;
            printf("%d deleted\n",temp->data);
            free(temp);
            return;
        }
        p=temp;
        temp=temp->link;
        count++;
    }
    printf("Invalid position\n");
    return;
}
void delete(){
    if(head==NULL){
        printf("Deletion can't be performed\n");
    }else{
        int choice;
        while(1){
            printf("Enter choice(1.delete_begin;2.delete_end;3.delete_anywhere;4.exit;):");
            scanf("%d",&choice);
            switch(choice){
                case 1:delete_begin();break;
                case 2:delete_end();break;
                case 3:delete_anywhere();break;
                case 4:return;
            }
        }
    }
}
void display(){
    CLL* temp=head;
    if(head==NULL){
        printf("EMPTY");
        return;
    }
    while(temp->link!=head){
            printf("%d ",temp->data);
            temp=temp->link;
    }
    printf("%d\n",temp->data);
    return;
}
int main(){
    int choice;
    while(1){
        printf("Enter choice(1.Insert;2.Delete;3.Display;4.Exit):");
        scanf("%d",&choice);
        switch(choice){
            case 1:insert();break;
            case 2:delete();break;
            case 3:display();break;
            case 4:exit(0);
        }
    }
    return 0;
}













