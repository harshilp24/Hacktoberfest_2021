#include <stdio.h>
 struct date
{
  int dd,mm,yyyy;
};
int main()
{
  int t,i,j,k;
  struct date type;
  scanf("%d",&t);
  while(t!=0)
  {
    scanf("%d%d%d",&type.dd,&type.mm,&type.yyyy);
    if(((type.dd==31) && (type.mm==1 || type.mm==3 || type.mm==5 || type.mm==7 || type.mm==8)) || (type.dd==30 && (type.mm==4 || type.mm==6)) )
    {
      printf("01-0%d-%d",(type.mm+1),(type.yyyy));
      printf("\n");
    }
    else if((type.dd==31) && ((type.mm==10)))
    {
      printf("01-%d-%d",(type.mm+1),(type.yyyy));
      printf("\n");
    }
     else if(type.dd==31 && type.mm==12)
    {
      printf("01-01-%d",(type.yyyy)+1);
      printf("\n");
    }
    else if((type.dd==30) && (type.mm==4 || type.mm==6))
            {
              printf("01-0%d-%d",type.mm+1,type.yyyy);
              printf("\n");
            }
            else if(type.dd==30 && ((type.mm==9) || (type.mm==11)))
            {
              printf("01-%d-%d",type.mm+1,type.yyyy);
              printf("\n");
            }
     else if(type.dd!=31 && (type.mm==1 || type.mm==3 || type.mm==5 || type.mm==7 || type.mm==8))
    {
      printf("%d-0%d-%d",(type.dd+1),type.mm,type.yyyy);
      printf("\n");
    }
    else if((type.dd!=31) && (type.mm==10 || type.mm==12))
    {
      printf("%d-%d-%d",(type.dd+1),type.mm,type.yyyy);
      printf("\n");
    }
      else if((type.dd!=30 && (type.mm==4 || type.mm==6)))
    {
      printf("%d-0%d-%d",(type.dd+1),type.mm,type.yyyy);
      printf("\n");     
    }
    else if((type.dd!=30 && (type.mm==9 ||type.mm==11)))
    {
      printf("%d-0%d-%d",(type.dd+1),type.mm,type.yyyy);
      printf("\n");     
    }
     else if((type.dd!=30 && (type.mm==11)))
    {
      printf("%d-%d-%d",(type.dd+1),type.mm+1,type.yyyy);
      printf("\n");     
    }
      else if(type.mm==2)
    {
      if(((type.yyyy)%4==0 || (type.yyyy)%400==0) && ((type.yyyy)%100!=0))
      {
        if(type.dd==29)
        {
          printf("01-03-%d",type.yyyy);
          printf("\n");
        }
       
       
      
        if(type.dd!=29)
        {
           
          printf("%d-02-%d",type.dd+1,type.yyyy);
          printf("\n");
        
        }
      }
        else
        {
          if(type.dd==28)
        {
          printf("01-03-%d",type.yyyy);
          printf("\n");
        }
       
       
      
        if(type.dd!=28)
        {
           
          printf("%d-02-%d",type.dd+1,type.yyyy);
          printf("\n");
        
        }
        }
          
    }
   t--;          
  }
return 0;
}








