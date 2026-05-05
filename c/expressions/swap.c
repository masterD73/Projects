#include <stdio.h>

int swap(int *num1, int *num2)
{
  int temp;
  
  temp =  *num1;
  *num1 = *num2;
  *num2 = temp;
}


int main()
{
  int x,y;
  
  x =  10, y =  5;
  printf("the  pair value (x,y) is: (%d,%d).\n", x, y);
  swap(&x, &y);
  printf("the  reversed pair value (x,y) is: (%d,%d).\n", x, y);
  
  return 0;
}
