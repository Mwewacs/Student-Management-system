Student Management System

Overview
This repository contains a refactored version of a Student Management System implemented in Python. The system manages student records and provides a simple text-based menu interface for interacting with the data.

Changes Made
Refactoring Details
1. Single Responsibility Principle (SRP)
-Student Class: Now only handles student data and related methods (update, display).
-StudentService Class: Handles student operations (add, update, delete) and interacts with the repository.
-StudentRepository Class: Manages data storage and retrieval, separating data access logic from business logic.

2. Open/Closed Principle (OCP)
-Added an interface (IStudentRepository) for the repository to allow easy extension or replacement of the data storage mechanism.

3. DRY (Don’t Repeat Yourself)
-Removed redundant code in updating student attributes by centralizing the update logic in the Student class and using the StudentService class to handle operations.

4. KISS (Keep It Simple, Stupid)
-Simplified design by clearly separating concerns into different classes and ensuring each class has a single responsibility.
-Added a text-based menu system to simplify user interactions.

5. YAGNI (You Ain’t Gonna Need It)
-Focused on core functionalities without overcomplicating the design. Added only necessary features for managing students.
Running the System

Prerequisites
-Python 3.x installed on your machine.

Steps to Run
Clone the Repository

git clone https://github.com/mwewacs/student-management-system.git
cd student-management-system
Run the System

Execute the following command to start the system:

python student_management_system.py
Interacting with the System

You will be presented with a menu to:

Add a student
Delete a student
Update student information
View all students
Exit the system
Follow the prompts to manage student records.

Example Usage
After running the system, you will see a menu like this:

sql
Copy code
Student Management System
1. Add Student
2. Delete Student
3. Update Student Information
4. View All Students
5. Exit