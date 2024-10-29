#Modify the iterative function to return a list of Fibonacci numbers up to n, instead of just the nth number:
def fibonacci_list(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]
print(fibonacci_list(10)) 

#Implement a function that finds the index of the first Fibonacci number that exceeds a given value.
def first_fib_index_exceeding(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a, b = b, a + b  
        index += 1

    return index
value = 20
print(first_fib_index_exceeding(value)) 

#Create a function that determines if a given number is a Fibonacci number.
import math

def is_fibonacci(num):

    def is_perfect_square(n):
        root = int(math.sqrt(n))
        return root * root == n

    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

print(is_fibonacci(21))  
print(is_fibonacci(22))  


#Implement a function that calculates the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.
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
    print(f"Ratio of F({i})/F({i-1}) = {ratio:.6f}")





