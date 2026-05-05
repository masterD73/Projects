#include <stdio.h>

int reverse(int num)
{
  int reversed;
  reversed = 0;
  
  while (num != 0)
  {
    reversed = reversed * 10 + num % 10;
    num /= 10;
  }
  printf("The reversed number is: %d\n", reversed);
  
  return reversed;
}
int main(void)
{
  int x;
  printf("Insert the number you wish to reverse: \n");
  sscanf("%d", &x);
  reverse(x);
  
  return 0;
}
