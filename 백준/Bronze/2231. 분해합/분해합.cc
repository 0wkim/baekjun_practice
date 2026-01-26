#include <iostream>
using namespace std;

int main()
{
	int num;
	cin >> num;

	for (int i = 1; i <= num; ++i)
	{
		int b = i;
		int a = 0;

		while (b != 0)
		{
			a += b % 10;
			b = b / 10;
		}

		if ((a + i) == num)
		{
			cout << i;
			break;
		}
		if (i == num)
		{
			cout << 0;
		}
	}

	return 0;
}