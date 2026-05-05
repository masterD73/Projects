#include "list_api.h"
#include <stdio.h>
#include<stdlib.h>
#include <assert.h>
#include <stddef.h>

int Match(const void* x, const void* y, void* params)
{
	return *(int*)x == *(int*)y;
}

int AddNum(void* data, void* num)
{
		*(int*) data += *(int*)num;
	
	return 1;
}

int ListCreateTest()
{
	slist_t* list = SListCreate();
	
	if(!list)
	{
		return 1;
	}
	
	SListDestroy(list);
	
	return 0;
}

int IterBeginTest()
{
	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	
	if(!iter)
	{
		SListDestroy(list);
		return 1;
	}
	
	SListDestroy(list);
	return 0;
}

int ListEmptyTest()
{
	int empty;
	slist_t* list = SListCreate();
	empty = SListIsEmpty(list);
	SListDestroy(list);
	
	return empty;
}

int ListInsertGetTest()
{
	int data;
	int num = 666;
	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	SListInsert(list, iter, &num);
	data = *(int*)SListIterGetData(iter);
	assert(data == num);
	SListDestroy(list);
	
	return 0;
}

int ListNotEmptyTest()
{
	int not_empty;
	int num = 100;
	
	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	SListInsert(list, iter, &num);
	not_empty = SListIsEmpty(list);
	SListDestroy(list);
	
	return not_empty;
}
/* add destroy test at the end */

int ListIterNextGetTest()
{
	int data;
	int num = 100;
	int num2 = 666;
	
	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	SListInsert(list, iter, &num);
	iter = SListIterNext(iter);
	SListInsert(list, iter, &num2);
	data = *(int*)SListIterGetData(iter);
	SListDestroy(list);
	
	if(data != num2)
	{
		return 1;
	}

	return 0;
}

int SListCountTest()
{
	int num = 100;
	int num2 = 666;
	int count = 0;
	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	SListInsert(list, iter, &num);
	iter = SListIterNext(iter);
	SListInsert(list, iter, &num2);
	count = SListCount(list);
	SListDestroy(list);
	
	if(count != 2)
	{
		return 1;
	}

	return 0;
}

int IterSetDataTest()
{	
	int num = 100;
	int num2 = 616;
	int num3 = 666;
	int changed_data;
	
	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	
	SListInsert(list, iter, &num);
	SListIterSetData(iter, &num3);	
	
	changed_data = *(int*)SListIterGetData(iter);
	SListDestroy(list);
	
	if(changed_data != num3)
	{
		return 1;
	}
	
	return 0;
}

int SListFindTest()
{
	int data;
	int num = 100;
	int num2 = 616;
	int num3 = 666;

	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	
	SListInsert(list, iter, &num);
	iter = SListIterNext(iter);
	
	SListInsert(list, iter, &num2);
	iter = SListIterNext(iter);
	
	SListInsert(list, iter, &num3);
	iter = SListIterNext(iter);
	
	iter = SListFind(list, &num2, Match, NULL);
	data = *(int*)SListIterGetData(iter);
	SListDestroy(list);
	
	if(data != num2)
	{
		return 1;
	}
	
	return 0;
}

int SListForEachTest()
{
	int i;
	int add = 34;
	int numbers[] = {100, 616, 666};
	int arr[3];
	
	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	
	for(i = 0; i < 3; i++)
	{
		arr[i] = numbers[i] + add;
	}
	
	SListInsert(list, iter, &numbers[0]);
	iter = SListIterNext(iter);
	
	SListInsert(list, iter, &numbers[1]);
	iter = SListIterNext(iter);
	
	SListInsert(list, iter, &numbers[2]);
	iter = SListIterNext(iter);
	
	SListForEach(list, AddNum, &add);
	
	iter = SListIterBegin(list);
	
	for(i = 0; i < 3; i++)
	{
		if(arr[i] != *(int*)SListIterGetData(iter))
		{
			SListDestroy(list);
			return 1;
		}
		
		iter = SListIterNext(iter);
	}
	SListDestroy(list);
	
	return 0;
}

int SListRemoveTest()
{
	int data;
	int numbers[] = {100, 616, 666};
	
	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	
	SListInsert(list, iter, &numbers[0]);
	iter = SListIterNext(iter);
	
	SListInsert(list, iter, &numbers[1]);
	iter = SListIterNext(iter);
	
	SListInsert(list, iter, &numbers[2]);
	iter = SListIterNext(iter);
	
	iter = SListFind(list, &numbers[1], Match, NULL);/*remove find*/
	
	SListRemove(list, iter);
	iter = SListIterBegin(list);
	iter = SListIterNext(iter);
	data = *(int*)SListIterGetData(iter);
	
	SListDestroy(list);
	
	if(data != numbers[2])
	{
		return 1;
	}
	
	return 0;
}

int SListIterIsEqualTest()
{
	int numbers[] = {100, 666};
	
	slist_t* list = SListCreate();
	iter_t iter = SListIterBegin(list);
	iter_t iter1 = SListIterEnd(list);
	
	SListInsert(list, iter, &numbers[0]);
	iter = SListIterNext(iter);
	
	SListInsert(list, iter, &numbers[1]);
	iter1 = SListIterNext(iter);
	
	
	if(SListIterIsEqual(iter, iter1))
	{
		SListDestroy(list);
		return 1;
	}
	SListDestroy(list);
	
	return 0;
}
