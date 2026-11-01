 """
PROG211 Object-Oriented Programming 1
Project: Student Record System
Purpose: Demonstrate classes, objects, attributes, methods, a list, and a class method.
Note: This beginner-friendly example stores sample student records in memory only.
"""

class Student:
    """Represents one student."""

    school_name = "Limkokwing University of Creative Technology"
    student_count = 0

    def __init__(self, student_id, name, programme):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        Student.student_count += 1

    def display_info(self):
        """Instance method: display this student's details."""
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Programme: {self.programme}")
        print(f"School: {Student.school_name}")
        print("-" * 30)

    @classmethod
    def display_student_count(cls):
        """Class method: display how many Student objects were created."""
        print(f"Total student objects created: {cls.student_count}")


def add_student(students):
    """Ask for details and add a Student object to the list."""
    print("\n--- Add a Student ---")
    student_id = input("Enter student ID: ").strip()

    # Prevent duplicate student IDs.
    for student in students:
        if student.student_id == student_id:
            print("That student ID already exists. Please use a unique ID.")
            return

    name = input("Enter student name: ").strip()
    programme = input("Enter programme: ").strip()

    if not student_id or not name or not programme:
        print("All fields are required. Student was not added.")
        return

    student = Student(student_id, name, programme)
    students.append(student)
    print(f"Student {name} was added successfully.")


def display_students(students):
    """Display all records stored in the list."""
    print("\n--- Student Records ---")
    if not students:
        print("No student records have been added yet.")
        return

    for student in students:
        student.display_info()


def find_student(students):
    """Find and display a student using their student ID."""
    search_id = input("Enter the student ID to find: ").strip()
    for student in students:
        if student.student_id == search_id:
            print("\nStudent found:")
            student.display_info()
            return
    print("No student with that ID was found.")


def main():
    # A list is used to store multiple Student objects.
    students = []

    # Sample records make it easy to test the program.
    students.append(Student("ICT001", "John Kamara", "Information Communication Technology"))
    students.append(Student("ICT002", "Mary Sesay", "Information Communication Technology"))

    while True:
        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Find student by ID")
        print("4. Display number of student objects created")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            Student.display_student_count()
        elif choice == "5":
            print("Thank you for using the Student Record System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
