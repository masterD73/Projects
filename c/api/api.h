#ifndef __VECTOR_H__
#define __VECTOR_H__
#include <stddef.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

struct dynamic_vector;
typedef struct dynamic_vector vector_t;
 
/*TODO: declare vector_t in headerfile without revealing the struct */
 
/** 
*   VectorCreate
*   ------------
*   Create a new vector_t - a dynamic vector that changes capacity as needed.
*   
*   Params
*   ------
*   init_capacity - num of elements vector can contain.
*   sizeof_elem - size in bytes of the element the vector should contain.
*
*   Return
*   ------
*   A new allocated vector_t. If it fails, return NULL.
*/
vector_t* VectorCreate(size_t init_capacity, size_t sizeof_elem);

/** 
*   VectorDestroy
*   ------------
*   Clears vector from memory.
*   
*   Params
*   ------
*   vector - pointer to the vector.
*
*/
void VectorDestroy(vector_t* vector);

/** 
*   VectorSize
*   ------------
*   
*   Params
*   ------
*   vector - pointer to the vector.
*
*   Return
*   ------
*   Num of currently stored elements
*/
size_t VectorSize(const vector_t* vector);

/** 
*   VectorCapacity
*   ------------
*   
*   Params
*   ------
*   vector - pointer to the vector.
*
*   Return
*   ------
*   Total number of elements vector may currently contain. 
*/
size_t VectorCapacity(const vector_t* vector);

/** 
*   VectorGetElem
*   -------------
*   Get access to the element at a given index (same as array indexing).
*   
*   Params
*   ------
*   vector - pointer to the vector.
*   index  - the index of the wanted element. First is 0.
*
*   Return
*   ------
*   Returns a pointer to the element. Returns NULL if fails.
*/
void* VectorGetElem(const vector_t* vector, size_t index);


/** 
*   VecrotPushEnd
*   ------------
*   Adds an element at the end of vector, resizes if needed.=
*
*   Params
*   ------
*   vector - pointer to the vector.
*   elem - elem to store at the end of the vector.
*
*   Return
*   ------
*   0 on success, non-zero value on failure
*/
int VectorPushEnd(vector_t* vector, const void* elem);

/** 
*   VectorPopEnd
*   ------------
*   removes an element from the end of the vector 
*
*   Params
*   ------
*   vector - pointer to the vector.
*   elem - buffer to store the popped element
*
*   Return
*   ------
*   0 on success, non-zero value on failure
*/
int VectorPopEnd(vector_t* vector, void* elem);

/** 
*   VectorResize
*   ------------
*   Changes the capacity of exisiting vector.
*   Elements exceeding the new capacity will be lost.
*   
*   Params
*   ------
*   vector - pointer to the vector.
*   num_capacity - number of elements the vector may contain.
*
*   Return
*   ------
*   0 on success, else failure.
*/
int VectorResize(vector_t* vector, size_t num_capacity);


#endif
