#include <iostream>

using namespace std;

template <typename T>
class StackArray
{
private:
	T* array;
	int capacity;
	int topIndex;
	int currentSize;
public:
	StackArray(int a = 6)
	{
		capacity = a;
		topIndex = -1; //Starts at index -1, because array is empty
		array = new T[a];
		currentSize = 0;
	}
	~StackArray()
	{
		delete[] array;
	}
	void size()
	{
		currentSize = topIndex + 1;
		cout << "The size of stack is currently: " << currentSize << endl << endl;
	}
	bool isFull()
	{
		if (topIndex == capacity - 1)
			return true;
		else
			return false;
	}
	bool isEmpty()
	{
		if (topIndex == -1)
			return true;
		else
			return false;
	}
	void topElement()
	{
		if (isEmpty())
		{
			cout << "The stack is empty! No items to retrieve!" << endl;
			return;
		}

		cout << "Top Element: " << array[topIndex] << endl;
		
	}
	void push(const T& element)
	{
		if (isFull())
		{
			cout << "ERROR! The function is Full!!" << endl;
			return;
		}

		array[++topIndex] = element;
	}
	void pop()
	{
		if (isEmpty())
		{
			cout << "ERROR! The array is Empty!!" << endl;
			return;
		}
		
		--topIndex;
	}
};

int main()
{
	StackArray<int> a(5);

	a.size();

	a.push(1);
	a.push(2);
	a.push(3);
	a.push(4);
	a.topElement();
	a.push(5);
	a.push(6);
	a.topElement();

	cout << "--------------------------" << endl << endl;

	a.size();

	a.pop();
	a.size();

	a.pop();
	a.pop();
	a.pop();
	a.pop();
	a.pop();

	a.size();

	return 0;
}
