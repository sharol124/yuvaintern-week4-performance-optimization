# Python Performance Optimization – Student Management System

## Project Overview

This project was completed as part of the YuvaIntern Junior Python Developer Internship – Week 4 task.

The objective was to analyze and optimize a Python-based Student Management System by identifying performance bottlenecks, applying efficient algorithms and data structures, and comparing execution time and memory usage.

## Technologies Used

- Python 3.10.11
- cProfile
- timeit
- time.perf_counter()
- tracemalloc
- unittest

## Project Structure

```text
YuvaIntern_Week4_Performance_Optimization/
│
├── original/
│   └── student_manager_original.py
│
├── optimized/
│   └── student_manager_optimized.py
│
├── benchmarks/
│   ├── profiling.py
│   ├── profile_optimized.py
│   ├── benchmark.py
│   ├── performance_results.csv
│   ├── original_profile.prof
│   └── optimized_profile.prof
│
├── tests/
│   └── test_performance_optimization.py
│
└── reports/
    ├── baseline_analysis.txt
    ├── performance_comparison.txt
    └── Week4_Performance_Optimization_Report.docx
```

## Optimizations Implemented

1. Replaced Bubble Sort with Python's built-in `sorted()` function.
2. Introduced a dictionary-based index for faster student searching.
3. Used Python's built-in `sum()` function for average calculation.
4. Used profiling to identify performance bottlenecks.

## Performance Results

Benchmark configuration:
- Dataset size: 10,000 student records
- Number of runs: 3

| Metric | Original | Optimized |
|---|---:|---:|
| Average Execution Time | 64.853479 seconds | 0.120483 seconds |
| Peak Memory Usage | 3.3664 MB | 3.6284 MB |

**Execution Time Improvement: 99.81%**

**Speedup: 538.28x**

The optimized implementation achieved significantly faster execution with a small increase in memory usage due to the additional dictionary index.

## Profiling

The original application was profiled using `cProfile`. Bubble Sort was identified as the primary performance bottleneck.

The optimized application was also profiled to verify the improvements.

## Testing

Automated tests were performed using Python's unittest framework.

Run the tests using:

```bash
python -m unittest discover -s tests -v
```

Result:
- Original manager: PASS
- Optimized manager: PASS
- Total tests: 2
- Failures: 0

## Running the Applications

Run the original implementation:

```bash
python original/student_manager_original.py
```

Run the optimized implementation:

```bash
python optimized/student_manager_optimized.py
```

Run the benchmark:

```bash
python benchmarks/benchmark.py
```

## Conclusion

The project demonstrates how profiling, efficient algorithms, and suitable data structures can improve Python application performance.

The optimized Student Management System achieved a measured execution-time improvement of approximately 99.81% while maintaining the functionality checked by the automated tests.