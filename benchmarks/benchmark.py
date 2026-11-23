
"""
Performance Comparison and Benchmarking

Compares original and optimized student management
applications using identical datasets and operations.
"""

import time
import csv
import os
import sys
import tracemalloc

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from original.student_manager_original import StudentManager as OriginalManager
from optimized.student_manager_optimized import StudentManager as OptimizedManager


DATASET_SIZE = 10000
NUMBER_OF_RUNS = 3


def benchmark(manager_class):
    """Measure execution time and peak memory usage."""

    execution_times = []

    tracemalloc.start()

    for _ in range(NUMBER_OF_RUNS):

        manager = manager_class()

        start_time = time.perf_counter()

        manager.generate_students(DATASET_SIZE)
        manager.search_student(9500)
        manager.calculate_average()
        manager.find_top_students(10)
        manager.sort_students_by_marks()

        end_time = time.perf_counter()

        execution_times.append(end_time - start_time)

    current_memory, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    average_time = sum(execution_times) / NUMBER_OF_RUNS

    return average_time, peak_memory / (1024 * 1024)


def main():

    print("\n============================================")
    print(" STUDENT MANAGER PERFORMANCE COMPARISON")
    print("============================================")

    print(f"Dataset Size: {DATASET_SIZE}")
    print(f"Number of Runs: {NUMBER_OF_RUNS}")

    print("\nBenchmarking original application...")

    original_time, original_memory = benchmark(OriginalManager)

    print("Benchmarking optimized application...")

    optimized_time, optimized_memory = benchmark(OptimizedManager)

    improvement = (
        (original_time - optimized_time) / original_time
    ) * 100

    speedup = original_time / optimized_time

    print("\n========== PERFORMANCE RESULTS ==========")

    print(f"Original Execution Time: {original_time:.6f} seconds")
    print(f"Optimized Execution Time: {optimized_time:.6f} seconds")

    print(f"Original Peak Memory: {original_memory:.4f} MB")
    print(f"Optimized Peak Memory: {optimized_memory:.4f} MB")

    print(f"Execution Time Improvement: {improvement:.2f}%")
    print(f"Speedup: {speedup:.2f}x")

    print("==========================================")

    # Save actual benchmark results to CSV.

    output_path = os.path.join(
        os.path.dirname(__file__),
        "performance_results.csv"
    )

    with open(output_path, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Application",
            "Average Execution Time (seconds)",
            "Peak Memory (MB)"
        ])

        writer.writerow([
            "Original",
            round(original_time, 6),
            round(original_memory, 4)
        ])

        writer.writerow([
            "Optimized",
            round(optimized_time, 6),
            round(optimized_memory, 4)
        ])

    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    main()
