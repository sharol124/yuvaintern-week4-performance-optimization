import sys
import os
import unittest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from original.student_manager_original import StudentManager as OriginalManager
from optimized.student_manager_optimized import StudentManager as OptimizedManager


class TestStudentManager(unittest.TestCase):

    def check_manager(self, manager_class):

        manager = manager_class()
        manager.generate_students(100)

        # Test 1: Student generation
        self.assertEqual(len(manager.students), 100)

        # Test 2: Student search
        first_student = manager.students[0]
        student_id = first_student["id"]

        result = manager.search_student(student_id)

        self.assertIsNotNone(result)
        self.assertEqual(result["id"], student_id)

        # Test 3: Average calculation
        average = manager.calculate_average()

        self.assertIsInstance(average, (int, float))
        self.assertGreaterEqual(average, 0)
        self.assertLessEqual(average, 100)

        # Test 4: Top students
        top_students = manager.find_top_students(5)

        self.assertEqual(len(top_students), 5)

        marks = [student["marks"] for student in top_students]

        self.assertEqual(marks, sorted(marks, reverse=True))

        # Test 5: Sorting
        sorted_students = manager.sort_students_by_marks()

        if sorted_students is None:
            sorted_students = manager.students

        sorted_marks = [student["marks"] for student in sorted_students]

        self.assertEqual(
            sorted_marks,
            sorted(sorted_marks, reverse=True)
        )

    def test_original_manager(self):
        self.check_manager(OriginalManager)

    def test_optimized_manager(self):
        self.check_manager(OptimizedManager)


if __name__ == "__main__":
    unittest.main(verbosity=2)