#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
int *arr_copy(const int arr[], unsigned int size)
{
  int i = 0;
  int *arr_cp = (int *) malloc(size * sizeof(int));

  for (i = 0; i < size; i++)
  {
    arr_cp[i] = arr[i];
  }
  free(arr_cp);
  return arr_cp;
}

