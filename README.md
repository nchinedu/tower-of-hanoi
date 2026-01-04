# Tower of Hanoi Solver 🗼

This Python script solves the classic Tower of Hanoi puzzle using recursion. It prints the sequence of moves required to transfer all disks from the first rod to the third rod, following the puzzle's rules.

## 🧩 Puzzle Rules

1\. Only one disk can be moved at a time.
2\. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
3\. No larger disk may be placed on top of a smaller disk.

## 🚀 How to Use

Run the script and call the `hanoi_solver(n)` function with the number of disks:

```python
from hanoi import hanoi_solver

print(hanoi_solver(3))
