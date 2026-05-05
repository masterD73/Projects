#include <stdio.h>
#include <typedef>
#include <string.h>

int main(int argc, char **argv, char **envp)
{
	char *str_tolower(const char *s) {
		size_t n = strlen(s) + 1;
		char *s2 = malloc(n);
		if(!s2) return NULL;
		for(size_t i = 0; i < n; i++)
		    s2[i] = tolower(s[i]);
    return s2;
}
	while (*envp != NULL)
	{
		printf("%s", *envp);
		*envp++;
	}
}
