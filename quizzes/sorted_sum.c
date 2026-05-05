#include <stdio.h>

int IsSumFound(int arr[], int sum, int arr_length, int *arr_index)
{
	int low, high;
	low = 0;
	high = arr_length -  1;
	
	while(low != high)
	{
	if(sum < arr[low] + arr[high])
	{
		high--;
	}
	else if(sum > arr[low] + arr[high])
	{
		low++;
	}
	else
	{
		arr_index[0] = low;
		arr_index[1] = high;
		return 1;
	}
	}
	return -1;
}

int main()
{
	int arr_index[2] = {0};
	int size = 10;
	int sum = 28;
	int arr[10] = {1, 2, 3, 13, 14 , 14, 15, 17, 18, 20};
	IsSumFound(arr, sum, size , arr_index);
	printf("The indexes of the sum %d are: low - %d, high - %d.\n", sum, arr_index[0], arr_index[1]);
	
	return 0;
}
