#include <stdio.h>

int starter(const char* str1,const char* str2)
{
	int i, j, k;
	i = j = 0;
	k = -1;
	while(str1[i] && str2[i])
	{
		if(str1[0] - str2[i] == 0)
		{
			k = i;
			break;
		}
		
		i++;
	}
	
	return k;
}

int ReverseCompare(const char* str1,const char* str2, int start)
{
	int i,j;
	
	for(
	
	return 0;
}

/*	
	for(i = 0; str1[i] && str2[j]; i++)
	{
		for(j = 0; str2[j] && str1[j]; i++)
		{
			if(str1[i] - str2[j] == 0)
			{
			k = j;
			break;
			}
		}
		
		if(str2[j] == 0)
		{
			break;
		}
	}
	
	for(i = k + 1; str1[i] && str2[i]; i++)
	{
		if(str1[i] - str2[++j] != 0)
		{
			return 1;
		}
	}
	
	return 0;
}
*/
int main()
{
	char* str1 = "1234";
	char* str2 = "3412";
	
	printf("Are the strings a rotation? - %d", ReverseCompare(str1, str2, starter(str1,str2)));

	return 0;
}


	
