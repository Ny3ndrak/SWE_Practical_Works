This project showcases multiple implementations and analyses of the Fibonacci sequence using Python. The project includes recursive, iterative, and memoized implementations, as well as generator functions and performance comparisons.

1. Modify the Iterative Function to Return a List of Fibonacci Numbers

def fibonacci_list(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

print(fibonacci_list(10))

Function Definition: fibonacci_list(n) initializes a list with the first two Fibonacci numbers, 0 and 1.
Loop: From the 3rd position (index 2) to n, it calculates each Fibonacci number and appends it to fib_sequence.
Return: The function returns the list of the first n Fibonacci numbers.
Example: Calling fibonacci_list(10) prints the first 10 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].

2. Implement a Function that Finds the Index of the First Fibonacci Number that Exceeds a Given Value

def first_fib_index_exceeding(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a, b = b, a + b
        index += 1
    return index

value = 20
print(first_fib_index_exceeding(value))

Function Definition: first_fib_index_exceeding(value) initializes two variables a and b to the first two Fibonacci numbers.
Loop: Continues to calculate Fibonacci numbers until b exceeds the given value.
Increment Index: For each loop iteration, the index counter is incremented.
Return: The function returns the index of the first Fibonacci number greater than value.
Example: first_fib_index_exceeding(20) prints the index of the first Fibonacci number greater than 20, which is 8 (corresponding to Fibonacci number 21).

3. Create a Function that Determines if a Given Number is a Fibonacci Number

import math

def is_fibonacci(num):
    def is_perfect_square(n):
        root = int(math.sqrt(n))
        return root * root == n
    
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

print(is_fibonacci(21))  # Output: True
print(is_fibonacci(22))  # Output: False

Import: math module is imported for mathematical operations.
Function Definition: is_fibonacci(num) checks if num is a Fibonacci number.
Helper Function: is_perfect_square(n) checks if a number is a perfect square.
Fibonacci Check: Uses mathematical properties to check if a number is a Fibonacci number.
Examples: is_fibonacci(21) returns True, is_fibonacci(22) returns False.

4. Implement a Function that Calculates the Ratio Between Consecutive Fibonacci Numbers

def fibonacci_ratios(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    ratios = []
    for i in range(2, n):
        ratio = fib_sequence[i] / fib_sequence[i - 1]
        ratios.append(ratio)
    return ratios

n = 20
ratios = fibonacci_ratios(n)
for i, ratio in enumerate(ratios, start=2):
    print(f"Ratio of F({i})/F({i-1}) = {ratio:.6f}")

Function Definition: fibonacci_ratios(n) generates Fibonacci numbers up to n and calculates ratios between consecutive numbers.
Initialization: Starts with the first two Fibonacci numbers in fib_sequence.
Loop: Calculates Fibonacci numbers and appends to fib_sequence.
Ratios: Calculates the ratio of each Fibonacci number to the previous one and appends to ratios.
Return: The function returns the list of ratios.

Discussion Questions:

1. What are the advantages and disadvantages of the recursive approach compared to the iterative approach?
ans. 

Recursive vs. Iterative Approach

Recursive:
Pros: Simpler, elegant.
Cons: Slower, can cause stack overflow.

Iterative:
Pros: Faster, stack safe.
Cons: More complex.

2.How does memoization improve the performance of the recursive function? Are there any drawbacks?
ans.
How Memoization Improves Performance:

Avoid Redundant Calculations: Memoization stores previously computed results, reducing the number of calculations by reusing them.
Efficiency: Transforms an exponential time complexity algorithm into a linear one for problems like the Fibonacci sequence.

Drawbacks of Memoization:

Space Overhead: Requires additional memory to store computed results, which may be significant for large input sizes.
Complexity: Adds an extra layer of complexity to the code with the need for a storage mechanism for the computed results.

3.In what scenarios might you prefer to use a generator function over other implementations?
ans.
Memory Efficiency: Generators yield values one at a time and do not store the entire sequence in memory, making them ideal for handling large datasets.

Lazy Evaluation: Useful when you need to process items on-the-fly without needing the entire sequence upfront.

Pipelines: Perfect for creating data processing pipelines where each item is processed as it is generated.

4. How does the space complexity differ between these implementations?
ans.
Recursive Implementation:
Space Complexity: O(n) due to the call stack depth, where n is the depth of recursion.

Memoized Recursive Implementation: Also O(n) for storing computed results.

Iterative Implementation:
Space Complexity: O(1) since it uses a constant amount of space regardless of the input size.

Fibonacci List Implementation: O(n) for storing the list of Fibonacci numbers up to n.

Generator Function:
Space Complexity: O(1) for generating each value on-the-fly without storing the entire sequence in memory.