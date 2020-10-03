#include<stdio.h>
#include<stdlib.h>
struct node{
    int info;
    node *next;
};
struct node *head=NULL;
struct node* createnode(){
  struct node *n;
  n=(struct node*)malloc(sizeof(struct node));
  return n;
}
void pushnode(int a){
   node *n=createnode();
   n->info=a;
   if(head==NULL){
       n->next=NULL;
       head=n;
     }
  else{
      n->next=head;
      head=n;
  }
}
int popnode(){
  node *temp;
  int a;
  if(head==NULL){
    printf("empty\n");
    return -1;
    }
  else
  {
    a=head->info;
    temp=head;
    head=head->next;
    free(temp);
  }
return a;
}
void topnode(){
if(head!=NULL){
  int a=popnode();
  pushnode(a);
  printf("%d\n",a);
  }
  else
  {
    printf("empty\n");
  }
}
int main(){
  int q,ch,a,b;
  head=NULL;
  while(1){

    printf("Enter 1 for inserting in stack\n");
    printf("Enter 2 for deleting top element is stack\n");
    printf("Enter 3 for viewing top element in stack\n");
    printf("Enter 0 for to exit\n");
    scanf("%d",&ch);
    switch(ch){
      case 1:scanf("%d",&a);
             pushnode(a);
             break;
      case 2:b=popnode();
            break;
      case 3:topnode();
      break;
      case 0:return 0;
    }
  }
}
