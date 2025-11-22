#include <iostream>

using namespace std;

class Node 
{
public:
	int data;
	Node* next;
	Node()
	{
		data = 0;
		next = NULL;
	}
	Node(int a)
	{
		data = a;
		next = NULL;
	}
};

class SingleLinkedList
{
private:
	Node* head;
	Node* tail;
public:
	SingleLinkedList()
	{
		head = NULL;
		tail = NULL;
	}
	void insertAtHead(int value)
	{
		Node* newNode = new Node(value);
		newNode->next = head;
		head = newNode;

		if (newNode->next == NULL)
		{
			tail = newNode;
		}
	}
	void insertAtTail(int value)
	{
		Node* newNode = new Node(value);
		if (head == NULL)

		{
			tail = newNode;
			head = newNode;
		}
		else
		{
			tail->next = newNode;
			tail = newNode;
		}
	}

	void printAll()
	{
		Node* nodeIterator = new Node;

		if (head == NULL)
		{
			cout << "The list is empty!" << endl;
			return;
		}

		nodeIterator = head;

		while (nodeIterator != NULL)
		{
			cout << nodeIterator->data << "->";
			nodeIterator = nodeIterator->next;
		}

		cout << "NULL" << endl;
	}
	
	void removeAtHead()
	{
		Node* nodeTemp;

		if (head == NULL)
		{
			cout << "The list is empty! Node can't be removed!" << endl;
			return;
		}
		
		nodeTemp = head;
		
		head = head->next;
		delete nodeTemp;

		if (head == NULL)
		{
			tail = NULL;
		}

	}

	void removeAtTail()
	{
		Node* nodeTemp;

		nodeTemp = head;

		if (head == NULL)
		{
			cout << "The list is empty! Node can't be removed!" << endl;
			return;
		}

		if (head == tail)
		{
			delete head;
			head = NULL;
			tail = NULL;
			return;
		}

		while (nodeTemp->next != tail)
		{
			nodeTemp = nodeTemp->next;
		}
		delete tail;
		tail = nodeTemp;	
		tail->next = NULL;
		
	
	}
};

int main()
{
	SingleLinkedList listA;

	listA.insertAtHead(20);
	listA.insertAtHead(30);
	listA.insertAtHead(40);
	listA.insertAtHead(50);
	listA.insertAtTail(10);
	listA.insertAtTail(70);
	listA.insertAtHead(0);

	listA.printAll();

	listA.removeAtHead();
	listA.removeAtHead();
	listA.removeAtTail();

	listA.printAll();

	return 0;
}