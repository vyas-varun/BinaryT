# Python Implementation of a Simple Binary Tree

The code provided is a Python implementation of a binary tree data structure. It includes a Node class, a BinaryTree class that uses the Node class to create a binary tree, and several methods for manipulating and traversing the tree.

## Node Class

The Node class represents a single node in the binary tree and contains three attributes:

- `left`: a reference to the left child node (which is another instance of the Node class)
- `right`: a reference to the right child node (also an instance of the Node class)
- `data`: the value stored in the node (can be any type of data)

## BinaryTree Class

The BinaryTree class is the main class that creates the binary tree and provides methods for manipulating and traversing it. Its attributes include:

- `root`: a reference to the root node of the binary tree (which is an instance of the Node class)

### Methods

1. **insert(value):** Inserts a new node into the binary tree with the given value.
2. **find(value):** Searches for a node with the given value and returns True if found, False otherwise.
3. **delete(value):** Deletes a node with the given value from the binary tree.
4. **preorder_traversal(callback):** Performs a preorder traversal of the binary tree and applies a callback function to each node's value.
5. **inorder_traversal(callback):** Performs an inorder traversal of the binary tree and applies a callback function to each node's value.
6. **postorder_traversal(callback):** Performs a postorder traversal of the binary tree and applies a callback function to each node's value.
7. **max_depth():** Returns the maximum depth (height) of the binary tree.
8. **level_order_traversal():** Performs a level-order traversal of the binary tree and returns a list of lists, where each inner list represents a level of the tree.

## Installation

The `setup.py` file is provided to package the BinaryTree class and its dependencies so that it can be easily installed and used by other Python programs.

To install, run:

```bash
python setup.py install
```

The above command might not work on some devices because of the permission issues (you might use `sudo` keyword on linux devices) and in such cases, one might install this library in a custom location. 

Refer to the code below for installing the package in the same directory. 

```python
python setup.py install --prefix .
```

## Testing

The `unit_test.py` file contains unit tests for the BinaryTree class to ensure that it behaves as expected.

```bash
python unit_test.py
```

You can add or modify the content according to your specific requirements.

