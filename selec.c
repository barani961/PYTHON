#include<stdio.h>
void main()
{
    int n,min,i,j,swap;//declaration
    printf("entter the no of elements in array");
    scanf("%d",&n);
    int a[n];
    printf("enter the elements of array:\n");//input
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);

//implementation
   for(i=0;i<n-1;i++)
   {
       min=i;//min=0 in sub division
       for(j=i+1;j<n;j++)
       {
           if (a[j]<a[min])
           min=j;
       }
       if (min!=i)
       {
           swap=a[i];
           a[i]=a[min];
           a[min]=swap;
       }
   }
    printf("the sorted array:\n");
   for(i=0;i<n;i++)
   printf(" %d ",a[i]) ;

}
