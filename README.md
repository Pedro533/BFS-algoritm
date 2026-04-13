# Breadth-First Search (BFS) - Linear Puzzle

This project shows a simple example of how **Breadth-First Search (BFS)** works using a small puzzle.

The goal is to transform an initial list into a target list by swapping elements.

---

## 🧠 What is BFS?

Breadth-First Search (BFS) is a way to explore all possible solutions step by step.

Think of it like this:

> First, try all possible moves with 1 step.  
> Then try all moves with 2 steps.  
> Then 3 steps, and so on.

It explores **level by level**, not going too deep too fast.

---

## 🎯 Problem

We start with:
[4, 2, 3, 1]

And we want to reach:

[1, 2, 3, 4]

---

## 🔧 Allowed Moves

At each step, we can only swap:

1. Left → swap first two elements  
   `[A, B, C, D] → [B, A, C, D]`

2. Middle → swap middle elements  
   `[A, B, C, D] → [A, C, B, D]`

3. Right → swap last two elements  
   `[A, B, C, D] → [A, B, D, C]`

---

## 🌳 How it works

Each state of the puzzle is represented as a **Node**.

Each node:
- stores the current list
- knows its parent (where it came from)
- can generate children (new states)

---

## 🔄 BFS Algorithm (Simple Explanation)

1. Start with the initial state
2. Put it in a queue (called "frontier")
3. Repeat:
   - Take the first element from the queue
   - Check if it's the solution
   - If not:
     - generate all possible moves
     - add new states to the queue (if not already seen)
4. Stop when solution is found

---

## 📦 Data Structures Used

- **Queue (list)** → to store nodes to explore (FIFO)
- **Visited list** → to avoid repeating states
- **Node class** → to store state and relationships

---

## 🧪 Example Output

[[4, 2, 3, 1],
[2, 4, 3, 1],
[2, 3, 4, 1],
[2, 3, 1, 4],
[2, 1, 3, 4],
[1, 2, 3, 4]]


This shows the path from start to solution.

---

## 🔙 How the Path is Built

Each node stores its **parent**.

Once the solution is found:
- we go backwards using parent references
- then reverse the list

---

## 📁 Files

- `tree.py` → contains the `Node` class
- `Breadth-First-Search.py` → main BFS algorithm

---

## 🚀 Why BFS is Important

- Guarantees the **shortest path** (if all moves cost the same)
- Used in:
  - AI
  - robotics
  - pathfinding
  - games

---

## ⚠️ Limitations

- Uses more memory than DFS
- Can be slow if the state space is large

---

## 🧠 Simple Analogy

Imagine you're looking for a house:

- First, check all houses in your street  
- Then all houses in nearby streets  
- Then farther away  

That’s BFS.

---

## 👨‍💻 Author

Simple educational implementation for understanding BFS.
