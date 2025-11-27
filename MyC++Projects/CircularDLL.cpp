#include <iostream>

//Implementing a circular DLL

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
	Node(int a)
	{
		value = a;
		next = NULL;
		prev = NULL;
	}

};

class CircularDLL
{
private:
	Node* head;
	Node* tail;
	int size;
public:
	CircularDLL()
	{
		head = NULL;
		tail = NULL;
		size = 0;
	}
	~CircularDLL()
	{
		Node* current;
		Node* temp;
		current = head;
		
		for(int i = 0; i < size; i++)
		{
			temp = current;
			current = current->next;
			delete temp;
		}
	}
	void isEmpty()
	{
		if (head == NULL)
		{
			cout << "The list is empty! (BY ISEMPTY() FUNCTION)" << endl;
		}
	}
	void insertAtHead(int data)
	{
		Node* newNode = new Node(data);

		if (head == NULL)
		{
			head = newNode;
			tail = newNode;
			tail->next = head; //This makes the tail point back to the head, making our DLL circular
			head->prev = tail;
		}
		else
		{
			newNode->next = head;
			newNode->prev = tail;
			head->prev = newNode;
			head = newNode;
			tail->next = newNode;
		}
		size++;
	}
	void insertAtTail(int data)
	{
		Node* newNode = new Node(data);

		if (head == NULL)
		{
			head = newNode;
			tail = newNode;
			head->prev = tail;
			tail->next = head;
		}
		else
		{
			newNode->prev = tail;
			tail->next = newNode;
			newNode->next = head;
			head->prev = newNode;
			tail = newNode;
		}
		size++;
	}
	void deleteAtHead()
	{
		Node* temp;
		temp = head;

		if (head == NULL)
		{
			cout << "The list is empty!" << endl;
			return;
		}
		
		if (head == tail)
		{
			head = NULL;
			tail = NULL;
		}
		else
		{
			head = head->next;
			head->prev = tail;
			tail->next = head;
		}

		delete temp;
		size--;
	
	}
	void deleteAtTail()
	{
		Node* temp;

		temp = tail;

		if (head == NULL)
		{
			cout << "The list is empty!" << endl;
			return;
		}
		
		if (head == tail)
		{
			head = NULL;
			tail = NULL;
		}
		else
		{
			tail = tail->prev;
			tail->next = head;
			head->prev = tail;
		}
		delete temp;

		size--;
	}
	void printAll()
	{
		Node* nodeIterator;
		nodeIterator = head;

		if (head == NULL)
		{
			cout << "The list is empty!" << endl;
			return;
		}
		else
		{
			for (int i = 0; i < size; i++)
			{
				cout << nodeIterator->value << "->";
				nodeIterator = nodeIterator->next;
			}
		}
		cout << "NULL" << endl;
	}
	void search(int a)
	{
		Node* current;
		current = head;
		bool found = false;

		if (head == NULL)
		{
			cout << "Search cannot be done! List is empty!" << endl;
			return;
		}

		for (int i = 0; i < size; i++)
		{
			if (current->value == a)
			{
				cout << "[" << current->value << "]" << endl;
				cout << "Search is completed!" << endl;
				found = true;
				break;
			}
			
			current = current->next;

		}

		if (found == false)
			cout << "Item was not found on the list!" << endl;

	}
};
int main()
{
	CircularDLL circularList;

	circularList.isEmpty();
	cout << endl << endl;

	circularList.insertAtHead(50);
	circularList.insertAtHead(40);
	circularList.insertAtHead(30);
	circularList.insertAtHead(20);
	circularList.insertAtTail(60);
	circularList.insertAtHead(10);
	circularList.deleteAtHead();
	circularList.deleteAtTail();

	circularList.isEmpty();

	circularList.printAll();

	circularList.search(10);
	circularList.search(60);
	circularList.search(30);

	return 0;
}