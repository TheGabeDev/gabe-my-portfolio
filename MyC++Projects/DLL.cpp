#include <iostream>

using namespace std;

class Node
{
public: 
	int value;
	Node* next;
	Node* prev;
	Node()
	{
		value = 0;
		next = NULL;
		prev = NULL;
	}
	Node(int data)
	{
		value = data;
		next = NULL;
		prev = NULL;
	}

};

class DLL
{
private:
	Node* head;
	Node* tail;
public:
	DLL()
	{
		head = NULL;
		tail = NULL;
	}
	~DLL() //This destructor will delete all the nodes when the program is finished
	{
		Node* current = head;
		while (current != NULL)
		{
			Node* temp = current;
			current = current->next;
			delete temp;
		}
	}
	void insertNodeAtHead(int a)
	{
		Node* newNode = new Node(a);

		if (head == NULL)
		{
			head = newNode;
			tail = newNode;
		}
		else
		{
			newNode->next = head;
			head->prev = newNode;
			head = newNode;
		}
	}
	void insertNodeAtTail(int a)
	{
		Node* newNode = new Node(a);

		if (head == NULL)
		{
			head = newNode;
			tail = newNode;
		}
		else
		{
			tail->next = newNode;
			newNode->prev = tail;
			tail = newNode;
		}

	}
	void printAll()
	{
		Node* nodeIterator;
		nodeIterator = head;

		if (head == NULL)
		{
			cout << "The list is empty! There is nothing to be printed!" << endl;
			return;
		}
		else
		{
			while (nodeIterator != NULL)
			{
				cout << nodeIterator->value << "->";
				nodeIterator = nodeIterator->next;
			}
			cout << "NULL" << endl;
		}
	}
	void deleteAtHead()
	{
		if (head == NULL)
		{
			cout << "The list is already empty! No items to be deleted!" << endl;
			return;
		}
		Node* temp = head;
		
		if (head == tail)
		{
			head = NULL;
			tail = NULL;
		}
		else
		{
			head = head->next;
			head->prev = NULL;
		}

		delete temp;
	}
	void deleteAtTail()
	{
		if (head == NULL)
		{
			cout << "The list is empty! No items to be deleted!" << endl;
			return;
		}

		Node* temp;
		temp = tail;

		if (head == tail)
		{
			head = NULL;
			tail = NULL;
		}
		else
		{
			tail = tail->prev;
			tail->next = NULL;
		}
		delete temp;
	}
};
int main()
{
	DLL dList;

	dList.insertNodeAtHead(40);
	dList.insertNodeAtHead(30);
	dList.insertNodeAtHead(20);
	dList.insertNodeAtHead(10);
	dList.insertNodeAtHead(0);
	dList.insertNodeAtTail(50);
	dList.insertNodeAtTail(60);
	dList.insertNodeAtTail(70);
	dList.deleteAtHead();
	dList.deleteAtTail();

	dList.printAll();

	return 0;
}