#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char c[26];
    int i, j=0, b=0;
    printf("Please enter a word below 26 characters : ");
    scanf("%s",&c);

    for(i=strlen(c)-1;i>=0;i--)
    {
        if(c[i]!=c[j])
        {
            b=1;
            break;
        }
        j++;
    }
    if(b==0)
        printf("\n\tThe word is Palindrome\n");
    else
        printf("\n\tThe word is not Palindrome\n");

    return 0;
}
