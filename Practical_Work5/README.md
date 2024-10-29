In this lab, i've implemented stack and queue data structures in Python and used them to solve practical problems. These fundamental data structures are crucial in computer science and are used in various applications, from algorithm implementation to system design.

EXERCISES Explanation:

# 2. Implement a function that uses a stack to evaluate postfix expressions.

Initialize Stack: Create an empty stack to store operands.

Iterate Through Tokens: Split the expression by spaces and process each token.

Check for Digits: If the token is a digit, push it onto the stack.

Evaluate Operators:
Pop the top two operands from the stack.
Perform the operation (+, -, *, /).
Push the result back onto the stack.
Return Result: The final result will be the only element left in the stack.

Example:
Expression: "3 4 + 2 * 7 /"

Steps:
Push 3 and 4 onto the stack.
Pop 3 and 4, add them (3 + 4 = 7), push 7 onto the stack.
Push 2 onto the stack.
Pop 7 and 2, multiply (7 * 2 = 14), push 14 onto the stack.
Push 7 onto the stack.
Pop 14 and 7, divide (14 / 7 = 2), push 2 onto the stack.

Result: 2

# 2. Create a function that uses two stacks to implement a queue.

Class Definition: QueueUsingStacks initializes two empty stacks, stack1 and stack2.

Enqueue Operation: enqueue appends items to stack1.

Dequeue Operation:
If stack2 is empty, transfer all items from stack1 to stack2 by popping from stack1 and pushing to stack2.

This reverses the order of elements, making the last inserted element of stack1 the first one in stack2.

Finally, pop the top of stack2 to get the front of the queue.

Error Handling: If both stacks are empty, raise an IndexError.

Example
Enqueue: Add 1, 2, and 3 to the queue.

Dequeue: Remove and return elements in FIFO order (1, 2, then 3).

Enqueue and Dequeue: Add 4 and then remove elements in FIFO order.

# 3. Use a queue to implement a basic task scheduler that processes tasks in the order they were added.

Import Deque: Use deque from the collections module for an efficient queue implementation.

TaskScheduler Class:
Initialization: The __init__ method initializes an empty deque queue.

Add Task: The add_task method appends a task to the queue and prints a confirmation.

Process Tasks: The process_tasks method processes tasks in the order they were added. It removes each task from the queue and prints it.

Example Usage:
Create Scheduler: Instantiate the TaskScheduler.

Add Tasks: Add tasks "Task 1", "Task 2", and "Task 3" to the queue.

Process Tasks: Process and print each task in the order it was added.

# 4. Implement a function that uses a stack to convert infix expressions to postfix.

Precedence: Define operator precedence to handle the order of operations.

Initialize: Create an empty stack and output list.

Iterate through Expression:
Operands: Directly append to output.

Left Parenthesis: Push onto stack.

Right Parenthesis: Pop from stack to output until left parenthesis is found.

Operators: Pop from stack to output while the precedence of the top stack operator is higher or equal. Push the current operator onto the stack.

Remaining Stack: Pop all remaining operators in the stack to the output.

Return: Join the output list into a string.

Example
Infix: "A+B*(C^D-E)"
Postfix: "ABCD^E-*+"
