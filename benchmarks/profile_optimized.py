import cProfile
import pstats
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from optimized.student_manager_optimized import StudentManager


def run_operations():
    manager = StudentManager()

    manager.generate_students(10000)
    manager.search_student("9500")
    manager.calculate_average()
    manager.find_top_students(10)
    manager.sort_students_by_marks()


def profile_execution():
    profiler = cProfile.Profile()

    profiler.enable()
    run_operations()
    profiler.disable()

    output_file = os.path.join(
        PROJECT_ROOT,
        "benchmarks",
        "optimized_profile.prof"
    )

    profiler.dump_stats(output_file)

    print("\nOPTIMIZED APPLICATION PROFILING RESULTS")
    print("=" * 50)

    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats("cumulative")
    stats.print_stats(15)

    print("\nProfile saved to:", output_file)


if __name__ == "__main__":
    profile_execution()