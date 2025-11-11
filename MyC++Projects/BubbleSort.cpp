#include <iostream>
#include <algorithm>

//Simple Algorithm for BubbleSort

using namespace std;

//Function Prototypes:
void BubbleSort(int[], int);
void DisplayArray(int[], int s);
void BubbleSortV2(int[], int);

int main()
{
	int size;

	cout << "Enter size for the array: ";
	cin >> size;
	while (size < 0)
	{
		cout << "Size can't be negative! Try again: ";
		cin >> size;
	}

	int* array = new int[size];

	cout << "Now enter the numbers for the the array: ";
	{
		for (int i = 0; i < size; i++)
		{
			cout << "Enter number #" << i + 1 << ": ";
			cin >> array[i];
			while (array[i] < 0)
			{
				cout << "Number can't be negative! Try again: ";
				cin >> array[i];
			}
		}
	}
	
	//Calling BubbleSort Function:
	cout << "Sorting array..." << endl << endl;
	//BubbleSort(array, size);
	BubbleSortV2(array, size);
	DisplayArray(array, size);

	delete[] array;
}

void BubbleSort(int arr[], int s)
{
	for (int pass = 0; pass < s - 1; pass++) //Counts the amount the passes
	{
		for (int index = 0; index < s - pass - 1; index++) //C
		{
			if (arr[index] > arr[index + 1])
			{
				int temp = arr[index];
				arr[index] = arr[index + 1];
				arr[index + 1] = temp;
			}
		}
	}
}

void DisplayArray(int arr[], int s)
{
	cout << "*************************" << endl;
	cout << "Displaying ordered array:" << endl;
	cout << "*************************" << endl << endl;

	for (int i = 0; i < s; i++)
	{
		cout << arr[i] << ", ";
	}
}

void BubbleSortV2(int arr[], int s)
{
	for (int pass = 0; pass < s - 1; pass++)
	{
		for (int index = 0; index < s - pass - 1; index++)
		{
			if (arr[index] > arr[index + 1])
			{
				swap(arr[index], arr[index + 1]);
			}
		}
	}
}