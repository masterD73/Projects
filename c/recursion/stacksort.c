#include "stack.h"
#include <stdio.h>


void InsertSorted(stack_t* stack, int num) 
{
    int temp;

    if (StackIsEmpty(stack) || num <= *(int*)StackPeek(stack)) 
    {
        StackPush(stack, &num);
        
        return;
    }

    temp = *(int*)StackPeek(stack);
    
    StackPop(stack);
    InsertSorted(stack, num);
    StackPush(stack, &temp);
}

void SortStack(stack_t* stack) 
{
    int num;

    if (!StackIsEmpty(stack))
    {
        num = *(int*)StackPeek(stack);
        
        StackPop(stack);
        SortStack(stack);
        InsertSorted(stack, num);
    }
}

void TestSortStack() 
{
    stack_t* stack;
    int i;
    int elements[] = {3, 1, 4, 2, 8 , 4, 10, 0, 0, 0, 1, 2, 3, 5, 8, 666, 616, 999, 1000};
    int arr_size = sizeof(elements) / sizeof(int);
	
    stack = StackCreate(arr_size, sizeof(int));
    if (!stack) 
    {
        printf("Failed to create stack\n");
        return;
    }

    for (i = 0; i < arr_size; i++) 
    {
        StackPush(stack, &elements[i]);
    }

    printf("Original stack elements: ");
    for (i = 0; i < arr_size; i++) 
    {
        printf("%d ", elements[i]);
    }

    SortStack(stack);
    printf("\nSorted stack elements: ");
    
    while (!StackIsEmpty(stack)) 
    {
        printf("%d ", *(int*) StackPeek(stack));
        StackPop(stack);
    }
    printf("\n");

    StackDestroy(stack);
}

int main() 
{
    TestSortStack();
    return 0;
}
