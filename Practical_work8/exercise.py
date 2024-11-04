##EXERCISES

# 1.Implement an in-place version of Quick Sort to improve its space efficiency.
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)

# 2.Modifying Bubble Sort to stop early if the list becomes sorted before all passes are complete
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)

# 3.Implement a hybrid sorting algorithm that uses Insertion Sort for small subarrays in Merge Sort
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr, left, right):
    if right - left <= 10:
        insertion_sort(arr, left, right)
    elif left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)

#4.Create a visualization of how each sorting algorithm works using a library like Matplotlib.
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.animation as animation

def plot_sorting_algorithm(sort_func, arr, title):
    arr_copy = arr.copy()
    n = len(arr_copy)
    states = []
    
    def callback():
        states.append(arr_copy.copy())
    
    sort_func(arr_copy, callback)
    
    fig, ax = plt.subplots()
    bar_rects = ax.bar(np.arange(n), arr_copy, align="edge")

    def update(frame):
        for rect, height in zip(bar_rects, states[frame]):
            rect.set_height(height)
        ax.set_title(title)
        return bar_rects
    
    ani = animation.FuncAnimation(fig, update, frames=range(len(states)), repeat=False, blit=False)
    plt.show()

def bubble_sort_visual(arr, callback):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                callback()
                swapped = True
        if not swapped:
            break

# Generate random array
arr = [random.randint(1, 100) for _ in range(20)]

plot_sorting_algorithm(bubble_sort_visual, arr, "Bubble Sort")


