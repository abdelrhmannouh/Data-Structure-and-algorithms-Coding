# Data Structures and Algorithms in Python

A comprehensive implementation of fundamental data structures and algorithms using Python. This repository contains educational implementations designed to understand how common data structures work under the hood.

## 📁 Project Structure

```
data Algorithms/
├── ReadMe.md                  # Project documentation
├── linked List/
│   ├── DoubleLinkedList.py   # Doubly Linked List implementation
│   ├── main.py               # Examples and usage
│   └── __pycache__/          # Python cache files
```

## 📚 Data Structures

### Linked List
Located in the `linked List/` directory

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

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- No external dependencies required

### Running Examples

Navigate to the linked list directory and run the main file:

```bash
cd "linked List"
python main.py
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
- Stack and Queue implementations
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
