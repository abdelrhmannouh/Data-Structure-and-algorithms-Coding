# Data Structures and Algorithms in Python

A comprehensive implementation of fundamental data structures and algorithms using Python. This repository contains educational implementations designed to understand how common data structures work under the hood.

## 📁 Project Structure

```
data Algorithms/
├── ReadMe.md                  # Project documentation
├── linked_List/
│   ├── DoubleLinkedList.py   # Doubly Linked List implementation
│   ├── main.py               # Examples and usage
│   └── __pycache__/          # Python cache files
├── Stack/
│   ├── stack.py              # Stack implementation
│   ├── main.py               # Examples and usage
│   └── __pycache__/          # Python cache files
├── Queue/
│   ├── queue.py              # Queue implementation
│   └── __pycache__/          # Python cache files
```

## 📚 Data Structures

### Linked List
Located in the `linked_List/` directory

- **DoubleLinkedList.py**: Implementation of a doubly linked list data structure
  - Nodes with forward and backward pointers
  - Support for insertion, deletion, and traversal operations
  - Bidirectional navigation through the list

#### Key Operations:
- Insert at head/tail
- Delete from any position
- Traverse forward and backward
- Search for elements
- Display list contents

### Stack
Located in the `Stack/` directory

- **stack.py**: Implementation of a stack data structure (LIFO - Last In First Out)
  - Node-based implementation with pointer manipulation
  - Support for push, pop, and peek operations
  - Stack size calculation

#### Key Operations:
- Push: Add elements to the top of the stack
- Pop: Remove and return the top element
- Peek: View the top element without removing
- is_empty: Check if stack is empty
- Size: Get the current number of elements

### Queue
Located in the `Queue/` directory

- **queue.py**: Implementation of a queue data structure (FIFO - First In First Out)
  - Array-based implementation with front and rear pointers
  - Support for enqueue, dequeue, and size operations
  - Fixed capacity initialization

#### Key Operations:
- Enqueue: Add elements to the rear of the queue
- Dequeue: Remove and return the front element
- isEmpty: Check if queue is empty
- Size: Get the current number of elements
- Front: Get the front index of the queue

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- No external dependencies required

### Running Examples

Navigate to the linked list directory and run the main file:

```bash
cd "linked_List"
python main.py
```

Navigate to the stack directory and run the main file:

```bash
cd Stack
python main.py
```

Navigate to the queue directory and run the queue file:

```bash
cd Queue
python queue.py
```

## 💡 Usage Examples

### Doubly Linked List Example
```python
from DoubleLinkedList import DoubleLinkedList

# Create a new doubly linked list
dll = DoubleLinkedList()

# Add elements
dll.insert_at_head(10)
dll.insert_at_tail(20)
dll.insert_at_tail(30)

# Display the list
dll.display()
```

## 🔄 Supported Operations

### DoubleLinkedList Operations
- **Insert**: Add elements at head, tail, or specific positions
- **Delete**: Remove elements from any position
- **Search**: Find elements in the list
- **Traverse**: Navigate forward and backward through the list
- **Display**: Print the list contents

### Stack Operations
- **Push**: Add elements to the stack
- **Pop**: Remove and return the top element
- **Peek**: View the top element without removing it
- **is_empty**: Check if the stack is empty
- **size**: Get the total number of elements

### Queue Operations
- **Enqueue**: Add elements to the queue
- **Dequeue**: Remove and return the front element
- **isEmpty**: Check if the queue is empty
- **size**: Get the total number of elements
- **front**: Get the front index of the queue

## 📝 Implementation Details

All implementations follow standard Python conventions:
- Classes for data structure representation
- Clear method naming conventions
- Comments and docstrings for clarity
- Time and space complexity considerations

## 🎯 Learning Objectives

This project helps understand:
- How linked lists work internally
- Pointer manipulation and node relationships
- Time complexity of various operations (O(n), O(1))
- Python object-oriented programming
- Memory management in data structures

## 🛠️ Future Enhancements

Planned additions to this repository:
- Single Linked List
- Circular Linked List
- Advanced Queue implementations (Priority Queue, Circular Queue)
- Tree data structures (Binary Tree, BST, AVL Tree)
- Graph implementations
- Sorting algorithms (Bubble, Quick, Merge, Heap)
- Searching algorithms (Binary Search, DFS, BFS)
- Dynamic Programming examples

## 📖 References

- Data Structures and Algorithms fundamentals
- Python 3 documentation
- Common interview preparation

## 💻 System Requirements

- **OS**: Windows, macOS, Linux
- **Language**: Python 3.x
- **Memory**: Minimal
- **Disk Space**: Less than 1 MB

---

**Author**: Abdelrhman Nouh  
**Last Updated**: January 2026  
**Status**: In Development
