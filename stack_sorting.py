# Given a stack with some elements, sort the stack in increasing order.

# Initialize the stack
from collections import deque

stack = deque()
stack.append(34), stack.append(3), stack.append(21), stack.append(98), stack.append(92), stack.append(23)
# Expected Output: [3, 21, 23, 34, 92, 98]

# Solution
def sort_stack(stack: deque) -> deque:
    temp_stack = deque()
    while stack:
        curr = stack.pop()
        while temp_stack and temp_stack[-1] < curr:
            stack.append(temp_stack.pop())
        temp_stack.append(curr)

    return temp_stack

ans = sort_stack(stack)
while ans:
    print(ans.pop())