In this lab, i've implemented both linear and binary search algorithms in Python. I've learned about their differences, time complexities, and when to use each one. The modular approach we've taken allows for easy testing and comparison of these algorithms.
While binary search is generally faster for large sorted lists, it requires the list to be sorted first. Linear search, although slower for large lists, works on unsorted lists and can be more efficient for small lists or when searching for multiple occurrences of an element.

EXPLANATION:

# Modify the linear search function to return all indices where the target appears, not just the first one.
ans.

Function Definition: linear_search_all_indices(arr, target) initializes an empty list indices to store the indices of the target.

Loop Through List: Uses enumerate to loop through each index and value in the list arr.

Check for Target: If the current value matches the target, append the index to the indices list.

Return: Returns the list of indices where the target appears.

# Implement a function that uses binary search to find the insertion point for a target value in a sorted list.
ans.
Function Definition: find_insertion_point(sorted_list, target) initializes two pointers, low and high, to the start and end of the list.

Binary Search Loop: Uses a while loop to repeatedly divide the search interval in half:

Calculate Midpoint: mid = (low + high) // 2 calculates the midpoint of the current interval.

Adjust Pointers:
If sorted_list[mid] is less than target, move the low pointer to mid + 1.
Otherwise, move the high pointer to mid.

Return Insertion Point: Returns the low pointer, which will be the correct insertion point for the target value.

Example: For a sorted list [1, 3, 5, 7, 9] and target 6, the insertion point is 3.


# Create a function that counts the number of comparisons made in each search algorithm.
ans.

Linear Search:
Function Definition: linear_search_with_count(arr, target) initializes a counter comparisons.

Loop Through List: Uses enumerate to loop through each index and value in the list arr.

Check for Target: If the current value matches the target, append the index to the indices list.

Increment Counter: Increment the comparisons counter for each iteration.

Return: Returns the list of indices and the number of comparisons.

Binary Search:
Function Definition: binary_search_with_count(sorted_list, target) initializes two pointers low and high, and a counter comparisons.

Binary Search Loop: Uses a while loop to repeatedly divide the search interval in half, adjusting the low and high pointers based on the comparison.

Increment Counter: Increment the comparisons counter for each iteration.

Return: Returns the index where the target is found (or -1 if not found) and the number of comparisons.

# Implement a jump search algorithm and compare its performance with linear and binary search.
ans.
1. Implementing Jump Search
ans.
Import Math Module: Import the math module for calculating the square root.

Initialize Variables: Set the length of the array n, the step size as the square root of n, and prev to 0.

Jump Search:
Loop Through Blocks: Jump through the array in blocks of step size until the value at the current block's end is greater than or equal to the target.

Update Pointers: Set prev to the current step, and increment step.

Check Bounds: If prev exceeds or equals n, return -1 indicating the target is not found.

Linear Search:
Search Within Block: Perform a linear search within the identified block.

Update Pointer: Increment prev to move within the block.

Check Target: If the target is found, return its index.

Return: Return the index of the target if found, otherwise -1.

2. Performance Comparison with Linear Search
ans.
Initialize Variables: Set comparisons to 0 and indices as an empty list.

Loop Through Array: Use enumerate to loop through each element in the array.

Check Target: If the current value matches the target, append the index to indices.

Return: Return the list of indices and the number of comparisons made.
 
 3. Performance Comparison with Binary Search
 ans.
 Initialize Variables: Set low and high pointers, and comparisons counter.

Binary Search Loop:
Calculate Midpoint: Compute mid as the average of low and high.

Compare with Target:
If mid value matches the target, return mid and comparisons.
If mid value is less than target, adjust low.
If mid value is greater than target, adjust high.

Return: Index of target or -1 if not found, with the number of comparisons made.

4. Jump Search with Comparison Count
Initialization:
Import Math: Import the math module for mathematical operations.

Calculate Step: Determine the jump step size as the square root of the array length.

Set Pointers and Counters: Initialize prev to 0 and comparisons to count the number of comparisons.

Jump in Blocks:
Loop: Jump through the array in blocks of size step until arr[min(step, n) - 1] is not less than the target.

Increment Counters: Update prev to step, increment step by the square root of the array length, and increment comparisons.

Check Bounds: If prev exceeds the array length, return -1 and the number of comparisons.

Linear Search within Block:
Loop: Perform a linear search within the identified block by incrementing prev.

Increment Counters: Increment comparisons for each comparison.

Check Bounds: If prev reaches the end of the block, return -1 and the number of comparisons.

Final Check:

Check Target: Compare the element at prev with the target.

Return: If they match, return the index prev and the number of comparisons. If not, return -1 and the number of comparisons.

Example Usage
Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Target: 13
Output:
Index of target: 6
Number of comparisons: 4