/* reviewer: Anan */
#include "list_api.h"

struct node_t
{
    void* data;
    struct node_t* next;
};

struct slist_t
{
    node_t* head;
    node_t* tail;
};

slist_t* SListCreate(void)
{
	slist_t* list = (slist_t*) malloc(sizeof(slist_t));
	
	if(!list)
	{
		return NULL;
	}
	
	list->head = (node_t*) malloc(sizeof(node_t));
	
	if(!SListIterBegin(list))
	{
		free(list);
		return NULL;
	}
	
	list->head->data = NULL;
	list->head->next = NULL;
	list->tail->data = NULL;
	list->tail->data = NULL;
	
	return list;
}

void SListDestroy(slist_t* list)
{
	iter_t tmp = SListIterBegin(list);
	iter_t current = SListIterBegin(list);
	
	while(tmp)
	{
		tmp = SListIterNext(current);
		free(current);
		current = tmp;
	}
	
	free(list);
}

int SListInsert(slist_t* list, iter_t where, const void* data)
{	
	node_t* replace = malloc(sizeof(node_t));
	
	if(replace == NULL)
	{
		return 1;
	}
	
	*replace = *where;
	where->data = (void*)data;
	where->next = replace;
	
	if(replace->next == NULL)
	{
		list->tail = replace;
	}
	
	return 0;
}

iter_t SListRemove(slist_t* list, iter_t iter)
{
	iter_t tmp = iter->next;

	if(tmp == NULL)
	{
		return NULL;
	}
	
	*iter = *tmp;
	free(tmp);

	return iter;
}

int Count(void* data, void* params)
{
	*(int*)params += 1;
	return 1;
}

size_t SListCount(const slist_t* list)
{
	size_t cnt = 0;
	
	SListForEach((slist_t*)list, Count, &cnt);
	
	return cnt;
}

int SListIsEmpty(const slist_t* list)
{
	return !(list->head->next == NULL);
}

iter_t SListFind(const slist_t* list, const void* data, MatchFunc match, void* params)
{
	iter_t iter = list->head;
	
	while(iter != list->tail)
	{
		if(match(iter->data, data, params))
		{
			return iter;
		}
		
		iter = iter->next;
	}
	
	return NULL;
}

int SListForEach(slist_t* list, ActionFunc action, void* params)
{
	iter_t iter = list->head;
	
	while(iter != list->tail)
	{
		action(iter->data, params);
		iter = iter->next;
	}
	
	return 0;
}

iter_t SListIterBegin(const slist_t* list)
{
	return list->head;
}

iter_t SListIterEnd(const slist_t* list)
{
	if(list->tail == NULL)
	
	{
		return list->head;
	}
	
	return list->tail;
}

iter_t SListIterNext(const iter_t iter)
{
	if(iter == NULL)
	{
		return NULL;
	}
	return iter->next;
}

int SListIterIsEqual(const iter_t iter1, const iter_t iter2)
{
	return iter1 == iter2;
}

void* SListIterGetData(const iter_t iter)
{
	if(iter == NULL)
	{
		return NULL;
	}
		
	return iter->data;
}

int SListIterSetData(iter_t iter, const void* new_data)
{
	
	if(new_data == NULL)
	{
		return 1;
	}
	if(iter->next == NULL)
	{
		return 1;
	}
	
	iter->data = (void*)new_data;
	return 0;
}


