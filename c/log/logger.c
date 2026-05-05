	#include <stdio.h>
	#include <stdlib.h>
	#include <string.h>
	#include <assert.h>
	#define MAX_LIMIT 1000

	typedef enum state_e
	{
		SUCCESS,
		FALIURE
	} state;

	typedef struct funcs {
	char *special_string;
	state (*compare)(const char *,const char *);
	state (*operation)(const char *, const char *);
	} function;

	state cmp(const char * s1,const char *s2)
	{
		return strcmp(s1, s2);
	}
	state CmpAppend(const char * command,const char *string)
	{
		if(string[0] == '<')
		{
			return SUCCESS;
		}
		else
		{
			return FALIURE;
		}

	}

	state Removefile(const char *fp, const char *str)
	{
		if(remove(fp) == 0)
		{
			printf("file has been removed successfully.\n");
			exit(SUCCESS);
		}
		else
		{
			printf("file was not found, program terminated.\n");
			exit(FALIURE);
		}
	}

	state ExitProgram(const char *fp, const char *str)
	{
		printf("Exited successfully without changing %s.\n", fp);

		exit(SUCCESS);
			
	}
	state CountLines(const char *fp, const char *str)
	{
		char chr;
		FILE *file =fopen(fp, "r");
		size_t count = 0;

		while((chr = fgetc(file)) != EOF)
		{
			if(chr == '\n')
			{
				count++;
			}
		}
		printf("\nThe number of lines in file is: %zu\n", count);
		fclose(file);
		return SUCCESS;
}

	state prepend(const char *fp, const char *str)
	{
		char c;
		FILE * file = fopen(fp, "r+");
		FILE *temp = fopen("temp", "a+");
		
		++str;
		fputs(str, temp);

		while ((c = fgetc(file)) != EOF)
		{
			fputc(c, temp);
		}

		rewind(file);
		rewind(temp);

		while ((c = fgetc(temp)) != EOF)
		{
			fputc(c, file);
		}

		fclose(temp);
		assert(remove("temp") == 0 && "Temporary file not removed.");
		fclose(file);

		return SUCCESS;
	}

	void logger(char *fp)
	{
		int i;
		char str[MAX_LIMIT];
		FILE *file;
		function arr[4] = {{"-remove\n", cmp, Removefile},
						{"-exit\n", cmp, ExitProgram}, 
						{"-count\n", cmp, CountLines}, 
						{"<", CmpAppend, prepend}};
		
		printf("Please insert the requested strings: \n");
		while(1)
		{
			file = fopen(fp, "a+");
			assert((file != NULL && "File name not given."));
			fgets(str, MAX_LIMIT, stdin);

			for(i = 0; i < 4; i++)
			{
				if(arr[i].compare(arr[i].special_string, str) == 0)
				{
					arr[i].operation(fp, str);
					break; 
				}
			}
			if(i == 4)
			{
				fputs(str, file);
			}
			fclose(file);
		}		
	}

	int main()
	{
		char string[MAX_LIMIT];
		
		printf("Enter file name:\n");
		fgets(string, MAX_LIMIT, stdin);
		string[strcspn(string, "\n")] = 0;

		logger(string);

		return 0;
	}
