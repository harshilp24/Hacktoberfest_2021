#include<stdio.h>
#include<string.h>
#include<ctype.h>
#define MAX 10
char infix[30];
char postfix[30];
char STACK[MAX];
int top=-1;
int length;
void push(char ch){
    top++;
    STACK[top]=ch;
    return;
}
void read_input(){
    printf("Enter Infix notation:");
    scanf("%s",infix);
    length=strlen(infix);
    infix[length]=')';
    push('(');
}
char pop(){
    char element=STACK[top];
    top--;
    return element;
}
void convert(){
    int j=0;
    for(int i=0;i<=length;i++){
        if(isalpha(infix[i])){
            postfix[j]=infix[i];
            j++;
        }else{
            switch(infix[i]){
                case '(':
                    push('(');
                    break;
                case '*':
                case '/':while(STACK[top]=='*'||STACK[top]=='/'){
                             postfix[j]=pop();
                             j++;
                         }
                         
                         push(infix[i]);
                         
                         break;
                case '+':
                case '-':while(STACK[top]=='*'||STACK[top]=='/'||STACK[top]=='+'||STACK[top]=='-'){
                             postfix[j]=pop();
                             j++;
                         }
                         push(infix[i]);
                         break;
                case ')':while(STACK[top]!='('){
                             postfix[j]=pop();
                             j++;
                             
                         }
                         top--;
                         break;
            }
        }
    }
    postfix[j]=='\0';
    printf("POSTFIX:%s\n",postfix);
    return;
}
int main(){
    read_input();
    printf("%s\n",infix);
    convert();
    return 0;
}



















