#include "list_api.h"
#include <stdio.h>
#include<stdlib.h>
#include <stddef.h>
#ifdef NDEBUG
#undef NDEBUG
#define RETURN_NDEBUG
#endif
#include <assert.h>
#ifdef RETURN_NDEBUG
#define NDEBUG
#undef RETURN_NDEBUG
#endif

int main() 
{ 
	assert(ListCreateTest() == 0);
	assert(IterBeginTest() == 0);
	assert(ListEmptyTest() == 0);
	assert(ListInsertGetTest() == 0);
	assert(ListNotEmptyTest() == 1);
	assert(ListIterNextGetTest() == 0);
	assert(SListCountTest() == 0);
	assert(IterSetDataTest() == 0);
	assert(SListFindTest() == 0);
	assert(SListForEachTest() == 0);
	assert(SListRemoveTest() == 0);
	assert(SListIterIsEqualTest() == 0);
	
	printf("All tests passed successfully.\n");
	
	return 0;
}
