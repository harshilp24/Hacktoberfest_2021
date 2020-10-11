#include <stdio.h>
#include <stdbool.h>
char po[30];
int st[30],top = -1;
void push(int n){
    top++;
    st[top] = n;
}
int pop(){
    int t = st[top];
    top--;
    return t;
}
void perform(char ch){
    int x,y;
    y = pop();
    x = pop();
    switch(ch){
        case '+':push(x+y);
                 break;
        case '-':push(x-y);
                 break;
        case '*':push(x*y);
                 break;
        case '/':push(x/y);
                 break;
        case '%':push(x%y);
                 break;
    }
}
bool isoperator(char ch){
    if(ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '%'){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    char c;
    int k;
    printf("Enter the postfix notation:");
    scanf("%s",po);
    for(int i=0;po[i] != '\0';i++){
        c = po[i];
        if(isoperator(c)){
            perform(c);
        }
        else{
            printf("Enter the value of %c:",c);
            scanf("%d",&k);
            push(k);
        }
    }
    printf("The result is:%d\n",st[top]);
    return 0;
}

