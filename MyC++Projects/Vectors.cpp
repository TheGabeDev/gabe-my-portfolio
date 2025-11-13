#include <iostream>
#include <vector>

using namespace std;

class Student
{
protected:
	string name;
	int grade;
public:
	string getName() const;
	int getGrade() const;
	void setName(string);
	void setGrade(int);
	Student(string, int);
	~Student();
	void displayInfo();
};
string Student::getName() const
{
	return name;
}
int Student::getGrade() const
{
	return grade;
}
void Student::setName(string a)
{
	name = a;
}
void Student::setGrade(int a)
{
	grade = a;
}
Student::Student(string a = "NONE", int b = 0)
{
	name = a;
	grade = b;
}
Student::~Student()
{

}
void Student::displayInfo()
{
	cout << "Displaying student's information: " << endl;
	cout << "Name: " << name << endl;
	cout << "Grade: " << grade << endl;
}

class GradeManager
{
protected:
	vector<Student> a;
public:
	void addStudent(const Student& stu)
	{
		a.push_back(stu);
	}
	void removeStudent(int removeGrade)
	{
		for (int i = 0; i < a.size(); i++)
		{
			if (removeGrade == a[i].getGrade())
			{
				a.erase(a.begin() + i);
			}
		}
	}
	Student highestGradeStudent()
	{
		Student highestGradeStudent;
		int highestGrade = 0;
		for (int i = 0; i < a.size(); i++)
		{
			if (a[i].getGrade() > highestGrade)
			{
				highestGrade = a[i].getGrade();
				highestGradeStudent = a[i];
			}
			
		}
		return highestGradeStudent;
	}
	void displayAllStudents()
	{
		cout << "Displaying all Students: " << endl << endl;
		for (int i = 0; i < a.size(); i++)
		{
			a[i].displayInfo();
			cout << endl;
		}
	}
	
};



int main()
{
	Student a("Gabe", 10), b("Phoebe", 9), c("Aidan", 7), d("Lucas", 8);
	
	/*a.displayInfo();
	b.displayInfo();
	c.displayInfo();
	d.displayInfo();*/
	
	GradeManager u;

	u.addStudent(a);
	u.displayAllStudents();

	u.addStudent(b);
	u.addStudent(c);
	u.addStudent(d);

	Student topStudent = u.highestGradeStudent();
	cout << "Highest grade student: " << endl;
	topStudent.displayInfo();
	cout << endl;

	u.removeStudent(7);
	u.displayAllStudents();

	return 0;
}