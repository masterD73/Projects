#include "stack.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct que
{
	stack_t* in;
	stack_t* out;
} que_t;

void Enqueue(que_t* q, int elem)
{
	StackPush(q->in, &elem);
}

int Dequeue(que_t* q)
{
	int elem;
	
	if (StackIsEmpty(q->out))
	{
		while(!StackIsEmpty(q->in))
		{
			StackPush(q->out, StackPeek(q->in));
			StackPop(q->in);
		}
	}
	
	elem = *(int*) StackPeek(q->out);
	StackPop(q->out);
	
	return elem;
}

int main()
{
	que_t* q = malloc(sizeof(*q));
	q->out = StackCreate(10, sizeof(int));
	q->in = StackCreate(10, sizeof(int));
	
	Enqueue(q, 10);
	Enqueue(q, 66);
	Enqueue(q, 85);
	
	printf("the first element to be released: (10) %d.\n", Dequeue(q));
	
	return 0;
}


