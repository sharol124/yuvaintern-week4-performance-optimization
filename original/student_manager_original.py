
"""
Student Records Management System
Original Version - Before Performance Optimization

This application manages student records and performs
searching, sorting, and performance analysis operations.
"""

import random


class StudentManager:
    """Manages student records using basic Python operations."""

    def __init__(self):
        self.students = []

    def generate_students(self, count):
        """Generate sample student records."""

        random.seed(42)

        self.students = []

        for i in range(count):
            student = {
                "id": i + 1,
                "name": f"Student_{i + 1}",
                "marks": random.randint(35, 100)
            }

            self.students.append(student)

        return self.students

    def search_student(self, student_id):
        """Search for a student using linear search."""

        for student in self.students:
            if student["id"] == student_id:
                return student

        return None

    def calculate_average(self):
        """Calculate average marks using repeated iteration."""

        total = 0

        for student in self.students:
            total += student["marks"]

        if len(self.students) == 0:
            return 0

        return total / len(self.students)

    def find_top_students(self, limit=10):
        """Find top students using a simple sorting approach."""

        sorted_students = sorted(
            self.students,
            key=lambda student: student["marks"],
            reverse=True
        )

        return sorted_students[:limit]

    def sort_students_by_marks(self):
        """Sort students based on their marks."""

        sorted_students = []

        for student in self.students:
            sorted_students.append(student)

        for i in range(len(sorted_students)):
            for j in range(0, len(sorted_students) - i - 1):

                if (
                    sorted_students[j]["marks"]
                    < sorted_students[j + 1]["marks"]
                ):
                    sorted_students[j], sorted_students[j + 1] = (
                        sorted_students[j + 1],
                        sorted_students[j]
                    )

        return sorted_students

    def generate_report(self):
        """Generate a summary report of student performance."""

        average = self.calculate_average()
        top_students = self.find_top_students(5)

        print("\n========== STUDENT PERFORMANCE REPORT ==========")

        print(f"Total Students: {len(self.students)}")
        print(f"Average Marks: {average:.2f}")

        print("\nTop 5 Students:")

        for student in top_students:
            print(
                f"ID: {student['id']} | "
                f"Name: {student['name']} | "
                f"Marks: {student['marks']}"
            )

        print("================================================")


def main():
    """Main function to execute the application."""

    manager = StudentManager()

    print("STUDENT RECORDS MANAGEMENT SYSTEM")
    print("---------------------------------")

    count = 1000

    manager.generate_students(count)

    print(f"\nGenerated {count} student records successfully.")

    # Search operation
    search_id = 500
    result = manager.search_student(search_id)

    print("\nStudent Search:")

    if result:
        print("Student Found:", result)
    else:
        print("Student Not Found")

    # Average calculation
    print(
        "\nAverage Marks:",
        round(manager.calculate_average(), 2)
    )

    # Sorting operation
    print("\nSorting student records...")

    sorted_students = manager.sort_students_by_marks()

    print("Sorting completed successfully.")

    print("\nTop 5 Students After Sorting:")

    for student in sorted_students[:5]:
        print(student)

    # Performance report
    manager.generate_report()


if __name__ == "__main__":
    main()
