import unittest
from binary_t import BinaryT

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        # Create an instance of the BinaryTree for testing
        self.tree = BinaryT()

    def test_insert(self):
        # Test the insert method of the BinaryTree class
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        # Check if the tree structure is as expected after insertion
        self.assertEqual(self.tree.root.data, 10)
        self.assertEqual(self.tree.root.left.data, 5)
        self.assertEqual(self.tree.root.right.data, 15)

    def test_find(self):
        # Test the find method of the BinaryTree class
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        # Check if the method correctly identifies existing and non-existing nodes
        self.assertTrue(self.tree.find(10))
        self.assertTrue(self.tree.find(5))
        self.assertTrue(self.tree.find(15))
        self.assertFalse(self.tree.find(20))

    def test_delete(self):
        # Test the delete method of the BinaryTree class
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.delete(15)
        # Check if the deleted node is no longer present in the tree
        self.assertFalse(self.tree.find(15))

    def test_preorder_traversal(self):
        # Test the preorder_traversal method of the BinaryTree class
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        expected_output = [10, 5, 15]
        output = []
        def print_node_data(data):
            output.append(data)
        # Use a callback to capture the traversal order
        self.tree._preorder_traversal(self.tree.root, print_node_data)
        # Check if the traversal order matches the expected output
        self.assertEqual(output, expected_output)

    def test_inorder_traversal(self):
        # Test the inorder_traversal method of the BinaryTree class
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        expected_output = [5, 10, 15]
        output = []
        def print_node_data(data):
            output.append(data)
        # Use a callback to capture the traversal order
        self.tree._inorder_traversal(self.tree.root, print_node_data)
        # Check if the traversal order matches the expected output
        self.assertEqual(output, expected_output)

    def test_postorder_traversal(self):
        # Test the postorder_traversal method of the BinaryTree class
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        expected_output = [5, 15, 10]
        output = []
        def print_node_data(data):
            output.append(data)
        # Use a callback to capture the traversal order
        self.tree._postorder_traversal(self.tree.root, print_node_data)
        # Check if the traversal order matches the expected output
        self.assertEqual(output, expected_output)

    def test_max_depth(self):
        # Test the max_depth method of the BinaryTree class
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(12)
        self.tree.insert(18)
        # Check if the calculated maximum depth matches the expected value
        self.assertEqual(self.tree.max_depth(self.tree.root), 3)
    
    def test_empty_tree(self):
        # Test various methods on an empty tree
        self.assertFalse(self.tree.find(10))
        self.assertEqual(self.tree.max_depth(self.tree.root), 0)
        self.assertEqual(self.tree.level_order_traversal(), [])

    def test_delete_nonexistent_node(self):
        # Test deleting a node that doesn't exist
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.delete(20)  # Try deleting a node that doesn't exist
        # Check if the tree structure is still valid
        self.assertTrue(self.tree.find(10))
        self.assertTrue(self.tree.find(5))
        self.assertTrue(self.tree.find(15))



if __name__ == '__main__':
    unittest.main()
