/* Ran reviewed */
#include "api.h"
#define VECTOR_INIT_CAPACITY 2

 struct dynamic_vector
{
    size_t size;      /* num of elements currently in vector */
    size_t capacity;    /* potential max num of elements */
    size_t sizeof_elem; /* amount of bytes per element */
    void* first_elem;   /* array containing the elements*/
} ;
 
 vector_t* VectorCreate(size_t init_capacity, size_t sizeof_elem)
 {
	vector_t* vector = malloc(sizeof(vector_t));
	
	if(vector == NULL)
	{
		return NULL;
	}
		
 	vector->size = 0;
 	vector->sizeof_elem = sizeof_elem;
 	vector->capacity = (init_capacity == 0 ? VECTOR_INIT_CAPACITY : init_capacity);
 	vector->first_elem = malloc(sizeof_elem * init_capacity);
 	
 	if(vector->first_elem == NULL)
	{
		return NULL;
	}
 	 	
 	return vector;
 }

void VectorDestroy(vector_t* vector)
{
	free(vector->first_elem);
	free(vector);
}

size_t VectorCapacity(const vector_t* vector)
{
	return vector->capacity;
}

void* VectorGetElem(const vector_t* vector, size_t index)
{
	if(vector->first_elem == NULL || index >= vector->size)
	{
		return NULL;
	}
	
	return (char*)vector->first_elem + (index * vector->sizeof_elem);
}


int VectorPushEnd(vector_t* vector, const void *elem)
{
	int static growth_rate = 2;
	
    if (vector->capacity == vector->size)
    {
    	VectorResize(vector, (vector->capacity) * growth_rate);
	}
	
	memcpy((char*) vector->first_elem + vector->size * vector->sizeof_elem, elem, vector->sizeof_elem);
	
	vector->size++;
	
	return 0;
}

int VectorPopEnd(vector_t* vector, void* elem)
{	
	if(vector->size == 0)
	{
		return 1;
	}	
	
	memcpy(elem, (char*)vector->first_elem + (vector->size - 1) * vector->sizeof_elem, vector->sizeof_elem);
	
	vector->size--;
	
	return 0;
}

int VectorResize(vector_t* vector, size_t num_capacity)
{
	if(num_capacity == 0)
	{
		return 1;
	}
	
	vector->first_elem = realloc(vector->first_elem, vector->sizeof_elem * num_capacity);
	
	if(vector->first_elem == NULL)
    {
    	return 1;
    }
    
    if(vector->size > num_capacity)
    {
    	vector->size = num_capacity;
    }

	vector->capacity = num_capacity;
    
	return 0;
}

size_t VectorSize(const vector_t* vector)
{
	return vector->size;
}

