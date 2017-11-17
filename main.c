#include <stdio.h>

long i = 0, j = 0;

int main(void)
{
	while(1)
	{
		i++;
		if (i == 300000000)
		{
			printf("%ld\n",j);
			j++;
			i =0;
		}
	}
}