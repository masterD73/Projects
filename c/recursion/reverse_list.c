#include "list_api.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

int ListFlip(list)
{
	
	
	
	ListFlip(list->head->next);
	
	return 0;
}

int main()
{
	int i = 0;
	int data[] = {1, 2, 3, 4};
  	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	
	while(i < sizeof(data) / sizeof(int))
	{
		SListInsert(list, iter, &data[i]);
		printf(i != sizeof(data) / sizeof(int) -1 ? "%d->" : "%d\n", *(int*)SListIterGetData(iter));
		iter = SListIterNext(iter);
		i++;
	}
	
	printf("Expected result: 4->3->2->1\n");
	
	
	
	
	
	
    return 0;
}

