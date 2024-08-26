# Interface for data access
class StudentRepository:
    """
    Interface for student data repository operations.
    This abstraction allows different implementations of student data storage.
    """
    def add_student(self, student: 'Student'):
        """
        Add a new student to the repository.
        """
        pass
    
    def remove_student(self, student_id: int):
        """
        Remove a student by ID from the repository.
        """
        pass
    
    def get_student(self, student_id: int) -> Optional['Student']:
        """
        Retrieve a student by ID from the repository.
        """
        pass
    
    def get_all_students(self) -> List['Student']:
        """
        Retrieve all students from the repository.
        """
        pass

# Implementation of StudentRepository
class StudentRepository(IStudentRepository):
    """
    Concrete implementation of the student repository using an in-memory list.
    """
    def __init__(self):
        self.students = []
    
    def add_student(self, student: 'Student'):
        """
        Add a student to the internal list.
        """
        self.students.append(student)
    
    def remove_student(self, student_id: int):
        """
        Remove a student from the internal list by ID.
        """
        self.students = [student for student in self.students if student.id != student_id]
    
    def get_student(self, student_id: int) -> Optional['Student']:
        """
        Find a student by ID in the internal list.
        """
        for student in self.students:
            if student.id == student_id:
                return student
        return None
    
    def get_all_students(self) -> List['Student']:
        """
        Retrieve all students from the internal list.
        """
        return self.students

# Student class with single responsibility
class Student:
    """
    Represents a student with attributes and methods to update and display information.
    """
    def __init__(self, id: int, name: str, age: int, major: str):
        self.id = id
        self.name = name
        self.age = age
        self.major = major

    def update(self, name: Optional[str] = None, age: Optional[int] = None, major: Optional[str] = None):
        """
        Update student attributes.
        """
        if name:
            self.name = name
        if age:
            self.age = age
        if major:
            self.major = major

    def display(self):
        """
        Display student information in a formatted string.
        """
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

# Service for student operations
class StudentService:
    """
    Service class to handle operations related to students using a repository.
    """
    def __init__(self, repository: IStudentRepository):
        self.repository = repository
    
    def add_student(self, id: int, name: str, age: int, major: str):
        """
        Create and add a new student to the repository.
        """
        student = Student(id, name, age, major)
        self.repository.add_student(student)
    
    def delete_student(self, student_id: int):
        """
        Delete a student by ID from the repository.
        """
        self.repository.remove_student(student_id)
    
    def update_student(self, student_id: int, name: Optional[str] = None, age: Optional[int] = None, major: Optional[str] = None):
        """
        Update student information by ID.
        """
        student = self.repository.get_student(student_id)
        if student:
            student.update(name, age, major)
    
    def get_all_students(self) -> List[Student]:
        """
        Retrieve all students from the repository.
        """
        return self.repository.get_all_students()

# Menu System for user interaction
class StudentManagementSystem:
    """
    Main class to interact with users, providing a menu-driven interface for managing students.
    """
    def __init__(self):
        self.repository = StudentRepository()  # Initialize the repository
        self.service = StudentService(self.repository)  # Initialize the service with repository
    
    def display_menu(self):
        """
        Display the main menu options to the user.
        """
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student Information")
        print("4. View All Students")
        print("5. Exit")
    
    def run(self):
        """
        Run the menu-driven interface, allowing user interaction.
        """
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.delete_student()
            elif choice == '3':
                self.update_student_info()
            elif choice == '4':
                self.view_all_students()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_student(self):
        """
        Collect student details from the user and add a new student.
        """
        id = int(input("Enter student ID: ").strip())
        name = input("Enter student name: ").strip()
        age = int(input("Enter student age: ").strip())
        major = input("Enter student major: ").strip()
        self.service.add_student(id, name, age, major)
        print("Student added successfully.")
    
    def delete_student(self):
        """
        Collect student ID from the user and delete the student.
        """
        student_id = int(input("Enter student ID to delete: ").strip())
        self.service.delete_student(student_id)
        print("Student deleted successfully.")
    
    def update_student_info(self):
        """
        Collect student details from the user and update existing student information.
        """
        student_id = int(input("Enter student ID to update: ").strip())
        name = input("Enter new name (or leave blank): ").strip()
        age_str = input("Enter new age (or leave blank): ").strip()
        major = input("Enter new major (or leave blank): ").strip()
        age = int(age_str) if age_str else None
        self.service.update_student(student_id, name or None, age, major or None)
        print("Student information updated successfully.")
    
    def view_all_students(self):
        """
        Display all students' information.
        """
        students = self.service.get_all_students()
        if students:
            for student in students:
                print(student.display())
        else:
            print("No students found.")

# Example usage
if __name__ == "__main__":
    system = StudentManagementSystem()  # Initialize the system
    system.run()  # Run the menu-driven interface
