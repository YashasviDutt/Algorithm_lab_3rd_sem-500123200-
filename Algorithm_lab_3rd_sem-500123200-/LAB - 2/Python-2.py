# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pTdZ8Tvn7GUagkIRS-qTEXiwV-Mn_NY8
"""

import time
import random
import matplotlib.pyplot as plt

# Partition function for QuickSort
def partition(arr, lb, ub):
    pivot = arr[ub]  # Pivot element
    i = lb - 1  # Index of smaller element
    for j in range(lb, ub):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[ub] = arr[ub], arr[i + 1]
    return i + 1

# Quick Sort function
def quickSort(arr, lb, ub):
    if lb < ub:
        m = partition(arr, lb, ub)
        quickSort(arr, lb, m - 1)
        quickSort(arr, m + 1, ub)

# Function to generate a random array
def generate_random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

# Function to measure execution time for quickSort
def measure_quick_sort_time(n):
    arr = generate_random_array(n)
    start_time = time.time()  # Start time before sorting
    quickSort(arr, 0, len(arr) - 1)  # Perform QuickSort
    end_time = time.time()  # End time after sorting
    return end_time - start_time  # Return the time taken

# Array sizes for testing (you can adjust this range)
array_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
execution_times = []

# Measure execution time for each array size
for size in array_sizes:
    exec_time = measure_quick_sort_time(size)
    execution_times.append(exec_time)

# Plotting the results
plt.plot(array_sizes, execution_times, marker='o', linestyle='-', color='b')

# Adding labels and title to the graph
plt.xlabel('Array Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Quick Sort Execution Time vs Array Size')
plt.grid(True)

# Show the graph
plt.show()