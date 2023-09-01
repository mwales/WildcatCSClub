#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
	if (argc != 2)
	{
		printf("Invalid usage!\n");
		printf("Usage: %s number\n", argv[0]);
		return 1;
	}

	int userNumber = atoi(argv[1]);

	if (userNumber % 2)
		printf("%d is odd\n", userNumber);
	else
		printf("%d is even\n", userNumber);

	return 0;
}
