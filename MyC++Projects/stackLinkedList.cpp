#include <iostream>

using namespace std;

template <typename T>
class Node
{
private:
	Node<T>* next;
	T data;
public:
	Node(T a)
	{
		next = NULL;
		data = a;
	}

	template <typename T>
	friend class StackLinkedList;
};

template <typename T>
class StackLinkedList
{
private:
	Node<T>* top;
	int size;

public:
	StackLinkedList()
	{
		top = NULL;
		size = 0;
	}
	~StackLinkedList()
	{
		Node<T>* temp;

		temp = top;

		while (top != NULL)
		{
			top = top->next;
			delete temp;
			temp = top;
		}
	}
	void push(const T &a)
	{
		Node<T>* newNode = new Node<T>(a);

		if (top == NULL)
			top = newNode;
		else
		{
			newNode->next = top;
			top = newNode;
		}
		++size;
	}
	void pop()
	{
		Node<T>* temp;
		temp = top;

		if (top == NULL)
			cout << "The stack is empty!" << endl;
		else
		{
			top = top->next;
			delete temp;
			--size;
		}
	

	}
	int getSize()
	{
		return size;
	}
	bool isEmpty()
	{
		if (top == NULL)
			return true;
		else
			return false;
	}
	void topElement()
	{
		cout << "The top element is: " << top->data << endl;
	}

};

int main()
{
	StackLinkedList<string> stack1;

	stack1.push("Gabe");
	stack1.push("John");
	stack1.push("Lucas");
	stack1.push("Terry");

	stack1.topElement();

	stack1.pop();

	stack1.topElement();

	if (stack1.isEmpty())
		cout << "The stack is empty!" << endl;

	cout << stack1.getSize();
	
	return 0;
}