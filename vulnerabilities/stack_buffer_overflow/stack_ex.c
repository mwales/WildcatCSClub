#include <stdio.h>
#include <string.h>

void functionWithStringsOnStack()
{
	char firstName[0x18];
	char lastName[0x18];

	memset(firstName, 0, 0x18);
	memset(lastName, 0, 0x18);

	printf("Enter first name\n");
	scanf("%s", firstName);

	printf("What is %s's last name?\n", firstName);
	scanf("%s", lastName);

	printf("Nice knowing you %s %s\n", firstName, lastName);
}

void functionWithArrayOfIntsOnStack()
{
	int numList[10];
	int menuChoice = 0;
	int secretFlagVar = 0;
	int indexTemp = 0;

	for(int i = 0; i < 10; i++)
	{
		numList[i] = 0;
	}

	while(1)
	{
		printf("Menu:\n");
		printf(" (1) Print list\n");
		printf(" (2) Set a value\n");
		printf(" (3) Exit\n");

		scanf("%d", &menuChoice);

		if (menuChoice == 1)
		{
			for(int i = 0; i < 10; i ++)
			{
				printf("%d ", numList[i]);
			}
			printf("\n");
		}
		else if (menuChoice == 2)
		{
			printf("Which index?\n");
			scanf("%d", &indexTemp);

			scanf("%d", numList + indexTemp);
			
			printf("Set index %d to %d\n", indexTemp, numList[indexTemp]);
		}
		else
		{
			break;
		}
	}

	if (secretFlagVar)
	{
		printf("Reveal the secret!\n");
	}
}

int main(int argc, char** argv)
{
	printf("Stack Examples\n");
	functionWithStringsOnStack();

	functionWithArrayOfIntsOnStack();

	return 0;
}
