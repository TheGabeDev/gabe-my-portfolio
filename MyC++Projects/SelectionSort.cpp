#include <iostream>
#include <algorithm>

using namespace std;

template <typename T>
class Numbers
{
protected:
	T* array;
	int size;
public:
	Numbers(int a = 0)
	{
		size = a;
		array = new T[size];
	}
	~Numbers()
	{
		delete[] array;
	}
	void setSize(int a)
	{
		size = a;
	}
	int getSize() const
	{
		return size;
	}
	void printArray();
	void fillArray();
	void askSize()
	{
		int aSize;
		cout << "Input a size for your array of numbers: ";
		cin >> aSize;
		delete[] array;
		size = aSize;
		array = new T[size];
	}

	template <typename T>
	friend void SelectionSort(Numbers<T>&);
};

//Function Prototypes:
template<typename T>
void SelectionSort(Numbers<T>&);

template <typename T>
void Numbers<T>::printArray()
{
	cout << "Displaying array: " << endl;
	for (int i = 0; i < size; i++)
	{
		cout << array[i] << ", ";
	}
	cout << endl;
}

template <typename T>
void Numbers<T>::fillArray()
{
	cout << "Enter numbers for the array: " << endl;
	for (int i = 0; i < size; i++)
	{
		cin >> array[i];
	}
}


int main()
{
	Numbers<int> a;

	a.askSize();
	cout << endl << "Size is: " << a.getSize() << endl;
	a.fillArray();

	cout << "Unsorted Array: " << endl;
	a.printArray();

	SelectionSort(a);
	cout << "Sorted Array: " << endl;
	a.printArray();

	return 0;

}

template <typename T>
void SelectionSort(Numbers<T>& b)
{

	for (int pass = 0; pass < b.size - 1; pass++)
	{
		int minNum = pass;
		for (int index = pass + 1; index < b.size; index++)
		{
			if (b.array[index] < b.array[minNum])
				minNum = index;
	
		}
		swap(b.array[minNum], b.array[pass]);
	}
}



