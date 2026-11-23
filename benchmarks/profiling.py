
"""
Performance Profiling - Original Student Manager

This script measures the execution time of the original
student management application and identifies bottlenecks.
"""

import cProfile
import pstats
import timeit
import os
import sys

# Add project root to Python path
sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from original.student_manager_original import StudentManager


def run_operations():
    """Execute all major student management operations."""

    manager = StudentManager()

    manager.generate_students(10000)

    manager.search_student(9500)

    manager.calculate_average()

    manager.find_top_students(10)

    manager.sort_students_by_marks()


def benchmark_execution():
    """Measure execution time using timeit."""

    execution_time = timeit.timeit(
        run_operations,
        number=3
    )

    average_time = execution_time / 3

    print("\n========== BASELINE PERFORMANCE ==========")

    print("Application: Original Student Manager")
    print("Dataset Size: 10,000 students")
    print("Number of Runs: 3")

    print(f"Total Execution Time: {execution_time:.6f} seconds")
    print(f"Average Execution Time: {average_time:.6f} seconds")

    print("==========================================")

    return average_time


def profile_execution():
    """Profile application using cProfile."""

    profiler = cProfile.Profile()

    profiler.enable()

    run_operations()

    profiler.disable()

    print("\n========== PROFILING RESULTS ==========")

    stats = pstats.Stats(profiler)

    stats.sort_stats("cumulative")

    stats.print_stats(15)

    # Save profiling results
    output_path = os.path.join(
        os.path.dirname(__file__),
        "original_profile.prof"
    )

    profiler.dump_stats(output_path)

    print(f"\nProfiling data saved to: {output_path}")


if __name__ == "__main__":

    benchmark_execution()

    profile_execution()
