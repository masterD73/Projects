#include <stdlib.h>
void Foo()
{
	char str1[20];
	char *str2 = malloc(sizeof(*str2) * 20);
	const char *str3 = "whatever";
	char str4[] = "whatever";
	
	str3[1] = 'a';
}

int main()
{
	Foo();
	return 0;
}
