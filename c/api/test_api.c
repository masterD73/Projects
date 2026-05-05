#include "api.h"
#include <stdio.h>
int main()
{
	int i = 1;
	int x = 10;
	int y = 66;
	int capacity = 0;
	int arr[] = {1, 2, 3, 4, 5};
	char c = 'a';
	char c_2 = 'b';
	char c_3 = 'c';
	char c_4 = 'd';
	int* first_elem;
	int* last_elem;
	int* destroyed_elem;

	/* Testing VectorCreate */

	vector_t* vector = VectorCreate(capacity, sizeof(int));
	printf("Was the vector created? - %p\n", (void*)vector);
	/* Testing VectorCapacity */
	
	printf("the capcity is:%ld \n", VectorCapacity(vector));
	
	/* Testing VectorCapacity */
	
	printf("The vector size is: %ld\n", VectorSize(vector));
	
	/* Testing VectorPushEnd & VectorPopEnd */
	
	printf("\nPush test. Inserting %d\n\n", arr[1]);
	assert(VectorPushEnd(vector, arr + 4) == 0 && "Push failed");
	printf("The vector size is: %ld\n", VectorSize(vector));
	printf("the capcity is:%ld \n", VectorCapacity(vector));
	last_elem = VectorGetElem(vector, VectorSize(vector) - 1);
	printf("The lastly pushed element (%ld) is: %d\n",VectorSize(vector), *last_elem);
	
	printf("\nPush test. Inserting %d\n\n", x);
	VectorPushEnd(vector, &x);
	printf("The vector size is: %ld\n", VectorSize(vector));
	printf("the capcity is:%ld \n", VectorCapacity(vector));
	last_elem = VectorGetElem(vector, VectorSize(vector) - 1);
	printf("The lastly pushed element (%ld) is: %d\n",VectorSize(vector), *last_elem);
	
	printf("\nPush test. Inserting %d\n\n", y);
	assert(VectorPushEnd(vector, &y) == 0 && "Push failed");
	printf("The vector size is: %ld\n", VectorSize(vector));
	printf("the capcity is:%ld \n", VectorCapacity(vector));
	last_elem = VectorGetElem(vector, VectorSize(vector) - 1);
	printf("The lastly pushed element (%ld) is: %d\n",VectorSize(vector), *last_elem);
	
	printf("\nPush test. Inserting %c\n\n", c);
	assert(VectorPushEnd(vector, &c) == 0 && "Push failed");
	printf("The vector size is: %ld\n", VectorSize(vector));
	printf("the capcity is:%ld \n", VectorCapacity(vector));
	last_elem = VectorGetElem(vector, VectorSize(vector) - 1);
	printf("The lastly pushed element (%ld) is: %c\n",VectorSize(vector), *last_elem);
	
	printf("\nPush test. Inserting %c\n\n", c_3);
	assert(VectorPushEnd(vector, &c_3) == 0 && "Push failed");
	printf("The vector size is: %ld\n", VectorSize(vector));
	printf("the capcity is:%ld \n", VectorCapacity(vector));
	last_elem = VectorGetElem(vector, VectorSize(vector) - 1);
	printf("The lastly pushed element (%ld) is: %c\n",VectorSize(vector), *last_elem);
	
	
	assert(VectorPopEnd(vector, &c_2) == 0 && "Pop failed");
	printf("The vector size after pop is: %ld\n", VectorSize(vector));
	printf("The element poped was: %c\n", c_2);
	
	assert(VectorPopEnd(vector, &c_4) == 0 && "Pop failed");
	printf("The vector size after pop is: %ld\n", VectorSize(vector));
	printf("The element poped was: %c\n", c_4);
	
	/* Testing VectorGetElem */
	
	first_elem = VectorGetElem(vector, i);
	last_elem = VectorGetElem(vector, VectorSize(vector) - 1);
	
	printf("The %dth element is: %d\n", i + 1, *first_elem);
	printf("The last element (%ld) is: %d\n",VectorSize(vector), *last_elem);
	
	/* Testing VectorResize */
	assert(VectorResize(vector,111) == 0 && "Capacity cannot be zero");
	printf("The vector size is: %ld\n", VectorSize(vector));
	printf("the capcity is:%ld \n", VectorCapacity(vector));
	
	assert(VectorResize(vector,2) == 0 && "Capacity cannot be zero");
	printf("The vector size is: %ld\n", VectorSize(vector));
	printf("the capcity is:%ld \n", VectorCapacity(vector));
	
	/* assert(VectorResize(vector, 0) == 0 && "Capacity cannot be zero");
	printf("The vector size is: %ld\n", VectorSize(vector));
	printf("the capcity is:%ld \n", VectorCapacity(vector));
	*/
	
	
	/* Testing Destroy */
	
	VectorDestroy(vector);
	assert(VectorGetElem(vector, 0) != NULL);
	printf("Was the vector destroyed? Address: %p\n", (void*)vector);
	destroyed_elem = VectorGetElem(vector, 0);
	printf("Was the vector destroyed? Element: %d\n", *destroyed_elem);
	
	
	
	return 0;
}

