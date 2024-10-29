#EXERCISES

# 1. Implement a function that uses a stack to evaluate postfix expressions.
def evaluate_postfix(expression):
    stack = []
    
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
    
    return stack[0]

# Example usage
expression = "3 4 + 2 * 7 /"
result = evaluate_postfix(expression)
print(f"The result of the postfix expression '{expression}' is: {result}")

# 2.Create a function that uses two stacks to implement a queue.
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        return self.stack2.pop()

# Example usage
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue()) 
print(queue.dequeue())  
queue.enqueue(4)
print(queue.dequeue())  
print(queue.dequeue())  

# 3. Use a queue to implement a basic task scheduler that processes tasks in the order they were added.
from collections import deque

class TaskScheduler:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)
        print(f"Task added: {task}")

    def process_tasks(self):
        while self.queue:
            task = self.queue.popleft()
            print(f"Processing task: {task}")

# Example usage
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
scheduler.process_tasks()

# 4. Implement a function that uses a stack to convert infix expressions to postfix.
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for char in expression:
        if char.isalnum():  
            output.append(char)
        elif char == '(':  
            stack.append(char)
        elif char == ')':  
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:  
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Example usage
expression = "A+B*(C^D-E)"
result = infix_to_postfix(expression)
print(f"Infix: {expression}")
print(f"Postfix: {result}")
