# Explanation

# 1. Implement an in-place version of Quick Sort to improve its space efficiency.
Quick Sort Function: Calls the partition function to get the pivot index, then recursively sorts the subarrays on both sides of the pivot.

Partition Function: Chooses a pivot element and rearranges the array such that elements less than the pivot are on the left and elements greater than the pivot are on the right. The pivot ends up in its correct position.

# 2. Modify Bubble Sort to stop early if the list becomes sorted before all passes are complete.
Bubble Sort Function: Iterates through the list, repeatedly swapping adjacent elements if they are in the wrong order.

Early Termination: If no elements were swapped in an iteration, the list is already sorted, and the loop breaks early, improving efficiency.

# 3. Implement a hybrid sorting algorithm that uses Insertion Sort for small subarrays in Merge Sort or Quick Sort.
Hybrid Approach: Uses Insertion Sort for small subarrays to optimize Merge Sort’s performance.

Insertion Sort: Efficient for small subarrays, improving overall sorting time.

Merge Sort: Divides the array into subarrays, sorts them, and merges them back together. Switches to Insertion Sort for subarrays of size 10 or less.

# 4. Create a visualization of how each sorting algorithm works using a library like Matplotlib.

Importing Modules:
matplotlib.pyplot and numpy are imported for plotting and numerical operations.

random is used to generate a random array.

matplotlib.animation is imported as animation for creating animations.

Plot Sorting Algorithm Function:
arr_copy is a copy of the input array to avoid modifying the original.

callback collects the array states after each update.

update function updates the heights of the bars in the plot.

Bubble Sort Visual Function:
Modified Bubble Sort that calls callback after each swap.