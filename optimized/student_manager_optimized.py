
"""
Student Records Management System
Optimized Version - After Performance Optimization

This application uses efficient data structures and
algorithms to improve execution performance.
"""

import random


class StudentManager:
    """Manages student records using optimized operations."""

    def __init__(self):
        self.students = []
        self.student_index = {}

    def generate_students(self, count):
        """Generate student records and build a search index."""

        random.seed(42)

        self.students = []
        self.student_index = {}

        for i in range(count):

            student = {
                "id": i + 1,
                "name": f"Student_{i + 1}",
                "marks": random.randint(35, 100)
            }

            self.students.append(student)

            # Dictionary indexing enables faster student searching.
            self.student_index[student["id"]] = student

        return self.students

    def search_student(self, student_id):
        """Search using dictionary-based lookup."""

        return self.student_index.get(student_id)

    def calculate_average(self):
        """Calculate average marks efficiently."""

        if not self.students:
            return 0

        total = sum(student["marks"] for student in self.students)

        return total / len(self.students)

    def find_top_students(self, limit=10):
        """Find top students using Python's optimized sorting."""

        return sorted(
            self.students,
            key=lambda student: student["marks"],
            reverse=True
        )[:limit]

    def sort_students_by_marks(self):
        """Sort records using Python's built-in Timsort algorithm."""

        return sorted(
            self.students,
            key=lambda student: student["marks"],
            reverse=True
        )

    def generate_report(self):
        """Generate a summary of student performance."""

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
    """Main function to execute the optimized application."""

    manager = StudentManager()

    print("OPTIMIZED STUDENT RECORDS MANAGEMENT SYSTEM")
    print("-------------------------------------------")

    count = 1000

    manager.generate_students(count)

    print(f"\nGenerated {count} student records successfully.")

    # Dictionary-based search
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

    # Optimized sorting
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
