
##EXERCISES
#Modify the linear search function to return all indices where the target appears, not just the first one.
def linear_search_all_indices(arr, target):
    indices = []
    for index, value in enumerate(arr):
        if value == target:
            indices.append(index)
    return indices

arr = [1, 3, 5, 7, 3, 9, 3]
target = 3
print(f"Indices where {target} appears: {linear_search_all_indices(arr, target)}")

#Implement a function that uses binary search to find the insertion point for a target value in a sorted list.
def find_insertion_point(sorted_list, target):
    low, high = 0, len(sorted_list)
    
    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid
    
    return low

# Example usage
sorted_list = [1, 3, 5, 7, 9]
target = 6
print(f"Insertion point for {target}: {find_insertion_point(sorted_list, target)}")

#Create a function that counts the number of comparisons made in each search algorithm.
#Linear Search with Comparison Count
def linear_search_with_count(arr, target):
    comparisons = 0
    indices = []
    for index, value in enumerate(arr):
        comparisons += 1
        if value == target:
            indices.append(index)
    return indices, comparisons

# Example usage
arr = [1, 3, 5, 7, 3, 9, 3]
target = 3
indices, comparisons = linear_search_with_count(arr, target)
print(f"Indices where {target} appears: {indices}")
print(f"Number of comparisons: {comparisons}")

#Binary Search with Comparison Count
def binary_search_with_count(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid, comparisons
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

# Example usage
sorted_list = [1, 3, 5, 7, 9]
target = 5
index, comparisons = binary_search_with_count(sorted_list, target)
print(f"Index where {target} is found: {index}")
print(f"Number of comparisons: {comparisons}")

#Implement a jump search algorithm and compare its performance with linear and binary search.
#Implementation of Jump Search
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev

    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
index = jump_search(arr, target)
print(f"Index of {target}: {index}")

#Performance Comparison
def linear_search_with_count(arr, target):
    comparisons = 0
    indices = []
    for index, value in enumerate(arr):
        comparisons += 1
        if value == target:
            indices.append(index)
    return indices, comparisons

# Example usage
arr = [1, 3, 5, 7, 3, 9, 3]
target = 3
indices, comparisons = linear_search_with_count(arr, target)
print(f"Indices where {target} appears: {indices}")
print(f"Number of comparisons: {comparisons}")

#Binary Search with Comparison Count
def binary_search_with_count(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid, comparisons
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

# Example usage
sorted_list = [1, 3, 5, 7, 9]
target = 5
index, comparisons = binary_search_with_count(sorted_list, target)
print(f"Index where {target} is found: {index}")
print(f"Number of comparisons: {comparisons}")

#Jump Search with Comparison Count
def jump_search_with_count(arr, target):
    import math

    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    comparisons = 0

    while arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons

    while arr[prev] < target:
        comparisons += 1
        prev += 1
        if prev == min(step, n):
            return -1, comparisons

    comparisons += 1
    if arr[prev] == target:
        return prev, comparisons

    return -1, comparisons

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
index, comparisons = jump_search_with_count(arr, target)
print(f"Index of {target}: {index}")
print(f"Number of comparisons: {comparisons}")
