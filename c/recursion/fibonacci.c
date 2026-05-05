#include <stdio.h>
/* Reviewer: Mr. Braunstain */

int FibonacciRecursive(int element_index)
{
	if(element_index < 0)
	{
		return -1;
	}	
	if(element_index == 0)
	{
		return 0;
	}
	if(element_index == 1)
	{
		return 1;
	}
	
	return FibonacciRecursive(element_index - 1) + FibonacciRecursive(element_index - 2);
}

int FibonacciIterative(int element_index)
{
	int i;
    int num_previous_previous, num_previous = 0, num_current = 1;
    
    if(element_index < 0)
    {
    	return -1;
    }
    if(element_index == 0)
    {
    	return 0;
    }    

    for (i = 1; i < element_index ; i++)
    {

        num_previous_previous = num_previous;

        num_previous = num_current;

        num_current = num_previous_previous + num_previous;
    }

	return num_current;
}

int main()
{
	int i;
	int iteration = 42;
	
	for(i = 0; i < iteration; i++)
	{
		printf("The Fibonacci value at index %d, is: %d.\n", i, FibonacciRecursive(i));	
	}
	
	for(i = 0; i < iteration; i++)
	{
		printf("The Fibonacci value at index %d, is: %d.\n", i, FibonacciIterative(i));	
	}
	
	
	return 0;
}
