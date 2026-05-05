#include <stdio.h>
#include <stddef.h>

int AirportTwo(int lift[], int land[], size_t size_lift, size_t size_land)
{
	size_t i;
	int sum = 0;
	
	for(i = 0; i < size_land; i++)
	{
		sum += land[i];
		printf("land: %d\n", sum);
	}
	
	for(i = 0; i < size_lift; i++)
	{
		sum -= lift[i];
		printf("lift: %d\n", sum);
	}
	
	return sum;
}

int AirportOne(int list[], size_t length)
{
	size_t i;
	int sum = 0;
	
	for(i = 0; i < length; i++)
	{
		sum ^= list[i];
	}
	
	return sum;
}

int main()
{
	int lift[] = {47, 74, 42};
	int land[] = {46, 74, 47, 42};
	int united[] = {46, 74, 47, 42, 47, 74, 42};
	int size_lift = sizeof(lift) / sizeof(int);
	int size_land = sizeof(land) / sizeof(int);
	int size_one = sizeof(united) / sizeof(int);
	
	printf("The AirportTwo result is: %d\n", AirportTwo(lift, land, size_lift, size_land));
	printf("The AurportOne result is: %d\n", AirportOne(united, size_one));
	
	
	return 0;
}
	
