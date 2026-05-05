#include "g.h"
#include <stdio.h>

int main()
{
	printf("The value of g_s is: %d\n", g_s);
	
	Foo();
	
	printf("The updated value of g_s us: %d\n", g_s);
}
