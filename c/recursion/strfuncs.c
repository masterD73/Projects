#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int StrLenRecursive(const char* str)
{
	
	if(*str == '\0')
	{
		return 0;
	}
	else
	{
		return 1 + StrLenRecursive(str + 1);
	}

}

int StrCmpRecursive(const char* str1, const char* str2)
{
	
	if(*str1 - *str2 != 0 || *str1 == '\0')
	{
		return *str1 - *str2;
	}
	
	return StrCmpRecursive(str1 + 1, str2 + 1);
}
char* StrCpyRecursive(char* dest, const char* src)
{
	*dest = *src;
	
	if(*src == '\0')
	{
		return dest;
	}

	StrCpyRecursive(dest + 1, src + 1);
	
	return dest;
}

char* StrCatRecursive(char* dest, const char* src)
{
	if (*dest != '\0')
	{
	  StrCatRecursive(dest + 1, src);
	}
	else if((*dest = *src) != '\0')
	{
		StrCatRecursive(dest + 1, src + 1);
	}
	else 
	{
		return dest; 
	}
	
	  return dest; 
}

char* StrStrRecursive(const char* haystack, const char* needle)
{
	if(*needle == '\0')
	{
		return (char*)haystack;
	}
	
	if(*haystack == '\0')
	{
		return NULL;
	}
	
	if(*haystack == *needle && StrStrRecursive(haystack + 1, needle + 1) == haystack + 1)
	{
		return (char*) haystack;
	}
	
	return StrStrRecursive(haystack + 1, needle);
}

int main()
{
	char * str1 = "hel";
	char* str2 = "worlworlworlworlworld";
	int expected = strlen(str1);
	int tested = StrLenRecursive(str1);
	char *str3 = malloc(StrLenRecursive(str1) + 1);
	char *str4 = malloc((StrLenRecursive(str1) + 1) * 200);
	char *str5 = "world";
	
	StrCpyRecursive(str3, str1);
	
	printf("Length of str4: %d\n%s.", StrLenRecursive(str4), str4);
	StrCatRecursive(str4, str1);
	StrCatRecursive(str4, str2);
	
	
	printf("Tested: %d.\nExpected: %d.\n", tested, expected);	
	printf("Equal? Expected non zero: %d\n", StrCmpRecursive(str1, str2));	
	printf("The string is: %s.\nThe copied string is: %s.\n", str1, str3);
	printf("The combined string is: %s.\n", str4);
	printf("the substring is: %s\n",StrStrRecursive(str1, str5));
	free(str3);
	
	
	return 0;
}

