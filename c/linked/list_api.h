#ifndef __SLIST_H__
#define __SLIST_H__
#include<stdio.h>
#include<stdlib.h>

typedef int (*MatchFunc)(const void*, const void*, void* params);
typedef int (*ActionFunc)(void*, void*);

typedef struct slist_t slist_t;
typedef struct node_t node_t;
typedef node_t* iter_t;

int ListCreateTest();
int IterBeginTest();
int ListEmptyTest();
int ListInsertGetTest();
int ListNotEmptyTest();
int ListIterNextGetTest();
int SListCountTest();
int IterSetDataTest();
int SListFindTest();
int SListForEachTest();
int SListRemoveTest();
int SListIterIsEqualTest();

/**
*   ListCreate
*   ----------
*   Create a new slist_t - a dummy list node for a singly linke list.
*
*   Return
*   ------
*   list - a pointer to hold the dummy list node, NULL on failure
*/
slist_t* SListCreate();
/** 
*   ListDestroy
*   -----------
*   Clears the list from memory.
*   
*   Params
*   ------
*   list - pointer to the list node.
*
*/
void SListDestroy(slist_t* list);

/** 
*   ListInsertBefore
*   ----------------
*   Inserts data before specified iterator.
*
*   Params
*   ------
*   list - pointer to the singly linked list.
*   data- data to be inserted into the list.
*
*   Return
*   ------
*   0 on success, 1 on failure.
* 
*/
int SListInsert(slist_t* list, iter_t where, const void* data);

/** 
*   ListRemove
*   ----------
*   Removes an element pointed by a specified iterator.
*
*   Params
*   ------
*   list - pointer to the list node.  
*	iter  - the iterator to the data to be removed.
*   
*	Return
*   ------
*   0 on success, 1 on failure. TODO
*/
iter_t SListRemove(slist_t* list, iter_t iter);

/** 
*   ListCount
*   ---------
*   
*   Params
*   ------
*   list - pointer to the linked list.
*
*   Return
*   ------
*   Num of items in the list.
*/
size_t SListCount(const slist_t* list);

/** 
*   ListIsEmpty
*   -----------
*   Checks wether the list is empty. 
*
*   Params
*   ------
*   list - pointer to the linked list.  
*	Return
*   ------
*   0 on success(empty), 1 on failure (non-empty).
*/
int SListIsEmpty(const slist_t* list);


/** 
*   ListFind
*   --------
*   Searches through the list for matching data using the recieved match function. 
*
*   Params
*   ------
*   list - pointer to the linked list.  
*	data - pointer for the sought data.
*   MatchFunc - a comparing function that recieves two void pointers and return 0 if the data is considered
*   equal.
* 
*	Return
*   ------
*   An iterator starting at the element containing the matching data if it exists in the list, NULL otherwise. 
*/
iter_t SListFind(const slist_t* list, const void* data, MatchFunc match, void* params);

/** 
*   ListForEach
*   -----------
*   Executes Func on each of the list items 
*
*   Params
*   ------
*   list - pointer to the list node.  
*	Func  - user-managed function.
*   
*	Return
*   ------
*   0 on success, 1 on failure.
*/
int SListForEach(slist_t* list, ActionFunc action, void* params);

/** 
*   SListIterBegin
*   -----------
*   Creates an iterator.
*   
*	Return
*   ------
*   An iterator pointer. TODO What happens if the list is empty??
*/
iter_t SListIterBegin(const slist_t* list);

/** 
*   ListIterEnd
*   -----------
*   Returns an iterator to the end of the list.
*
*   Params
*   ------
*   list - pointer to the list node.
*
*   Return
*   ------
*   returns iterator. TODO What happens if the list is empty??
* 
*/
iter_t SListIterEnd(const slist_t* list);

/** 
*   ListIterNext
*   ------------
*   Returns a pointer to the next iteration.
*
*   Params
*   ------
*   iter - pointer to the current iteration.   TODO - what happens at end??
*/
iter_t SListIterNext(const iter_t iter);

/** 
*   ListIterIsEqual
*   ---------------
*   Compares two iterators.
*
*   Params
*   ------
*   iter1 - pointer to the iterator.  
*	iter2 - pointer to the iterator.  
*   
*	Return
*   ------
*   Returns equal (0) or not equal (1).
*/
int SListIterIsEqual(const iter_t iter1, const iter_t iter2);

/** 
*   ListIterGetData
*   ---------------
*   get the data pointed to by the iter.
*
*   Params
*   ------
*   iter - iterator
*   
*	Return
*   ------
*   data pointed to by the iter. 
*/
void* SListIterGetData(const iter_t iter);

/** 
*   ListIterSetData
*   ---------------
*   Sets the data pointed to by the iter to the new data.
*
*   Params
*   ------
*   iter - iterator.  
*	new_data  - data to be set.
*   
*	Return
*   ------
*   0 on success, 1 on failure.
*/
int SListIterSetData(iter_t iter, const void* new_data);

#endif
