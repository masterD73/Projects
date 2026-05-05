#include <stdio.h>

void swap(size_t *num1, size_t *num2)
{
  size_t temp;
  temp = *num1;
  *num1 = *num2;
  *num2 = temp;
}

void swap_pointers(size_t **ptr1, size_t **ptr2)
{
  swap((size_t*) ptr1, (size_t*) ptr2);
}

