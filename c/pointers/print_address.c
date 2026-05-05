#include <stdio.h>

void print_address()
{
  static int s_i = 7;
  int i = 7;
  iunt *ptr = &i;
  int *ptr2 = (int *) malloc(sizeof(int));

  if(ptr)
  {
    int **ptr = &ptr;
  }
  printf("%x\n", &i);
  printf("%x\n", ptr);
  printf("%x\n", ptr2);
  printf("%x\n", ptr3);
  free(ptr2);
}

