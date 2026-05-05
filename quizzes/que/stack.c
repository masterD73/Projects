#include <assert.h>    /* assert */
#include <string.h>    /* memcpy */
#include <stdlib.h>    /* malloc, free */

#include "stack.h"

struct stack
{
    size_t capacity;
    size_t size;
    size_t size_of_element;
    char *buffer;
};

stack_t *StackCreate(size_t capacity, size_t size_of_element)
{
    stack_t *new_stack = NULL;

	assert(capacity > 0);
    assert(size_of_element > 0);

    new_stack = malloc(sizeof(*new_stack));
    if (!new_stack)
    {
        return NULL;
    }

    new_stack->buffer = malloc(capacity * size_of_element);
    if (!new_stack->buffer)
    {
        free(new_stack);
        return NULL;
    }

    new_stack->capacity = capacity;
    new_stack->size = 0;
    new_stack->size_of_element = size_of_element;

    return new_stack;
}


void StackDestroy(stack_t *stack)
{
    /* It is legal to destroy NULL, just like `free(NULL)` and C++ `delete NULL` are legal.*/
    if (stack == NULL)
    {
        return;
    }

	free(stack->buffer); stack->buffer = NULL;
    stack->capacity = 0;
    stack->size = 0;
    stack->size_of_element = 0;

    free(stack);
}




void StackPush(stack_t *stack, const void *element)
{
    assert(stack);
    assert(element);

    memcpy(
        &stack->buffer[stack->size * stack->size_of_element],
        element,
        stack->size_of_element
    );

    ++stack->size;
}


void StackPop(stack_t *stack)
{
	assert(stack);

    --stack->size;
}


const void *StackPeek(const stack_t *stack)
{
    assert(stack);
    
	return &stack->buffer[(stack->size - 1) * stack->size_of_element];
}


size_t StackSize(const stack_t *stack)
{
    assert(stack);
    
	return stack->size;
}

size_t StackCapacity(const stack_t *stack)
{
    assert(stack);

	return stack->capacity;
}

int StackIsEmpty(const stack_t *stack)
{
    assert(stack);
    
    return stack->size == 0;
}


