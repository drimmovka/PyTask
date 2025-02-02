'''
AVLTree Module

This module implements an AVL tree, a self-balancing binary search tree. 
An AVL tree maintains its balance by ensuring that the heights of the 
two child subtrees of any node differ by no more than one. This property 
ensures O(log n) time complexity for insertion, deletion and lookup operations.

Key Features:
- Insertion and deletion operations that maintain the AVL property.
- Methods for searching, traversing, and checking the tree's properties.
- Support for adding elements from an iterable collection.

Usage:
    from avl_tree import AVLTree

    tree = AVLTree()
    tree.add(10)
    tree.add(20)
    tree.add(5)
    print(tree.is_empty())  # Returns False
'''

class AVLTree:
    '''A class representing an AVL Tree, which is a self-balancing binary search tree.
    
    In an AVL tree, the heights of the two child subtrees of any node differ by at most one.
    '''

    class Node:
        '''A class representing a node in the AVL tree.
        
        Attributes:
            val (int): The value stored in the node.
            left (Node or None): A reference to the left child node.
            right (Node or None): A reference to the right child node.
            height (int): The height of the node in the tree.
        '''
        def __init__(self, val: int):
            '''Initializes a new node with the given value.
            
            Args:
                val (int): The value to be stored in the node.
            '''
            self.val: int = val
            self.left: AVLTree.Node | None = None 
            self.right: AVLTree.Node | None = None
            self.height: int = 1

    def __init__(self, collection=[]):
        '''Initializes an empty AVL tree. Optionally, an iterable can be provided to populate the tree.
        
        Attributes:
            __root (Node or None): The root node of the AVL tree.
            __len (int): The number of nodes in the AVL tree.
        '''            
        self.__root: AVLTree.Node | None = None
        self.__len: int = 0
        if hasattr(collection, '__iter__'):  # Check if collection is an iterable object
            for i in collection:
                self.add(i)
        else:
            raise ValueError(f'Cannot create AVL tree from type {type(collection)}. Expected an iterable.')
    
    def __str__(self) -> str:
        '''Returns a string representation of the AVL tree using inorder traversal.
        
        Returns:
            str: A string representation of the tree.
        '''
        return '{' + str(self.traverse())[1:-1] + '}'

    def __repr__(self) -> str:
        '''Returns a detailed string representation of the AVL tree, including its length and height.
        
        Returns:
            str: A detailed representation of the tree.
        '''
        return f'len: {len(self)}; height: {self.height}; {self.traverse()}'
    
    def __len__(self) -> int:
        '''Returns the number of nodes in the AVL tree.
        
        Returns:
            int: The number of nodes in the tree.
        '''
        return self.__len

    def __contains__(self, val: int) -> bool:
        '''Checks if a value is present in the AVL tree.
        
        Args:
            val (int): The value to search for in the tree.
        
        Returns:
            bool: True if the value is found, False otherwise.
        '''
        return self.__contains(self.__root, val)
    
    @property
    def height(self) -> int:
        '''Returns the height of the AVL tree.
        
        Returns:
            int: The height of the tree.
        '''
        return self.__height(self.__root)


    def clear(self) -> None:
        '''Clears the AVL tree.

        Sets the root to None and resets the node count to 0.
        The tree will be empty after this call.

        Returns:
            None
        '''
        self.__root = None  # Clear the root
        self.__len = 0      # Reset the node count
    
    def is_empty(self) -> bool:
        '''Checks if the AVL tree is empty.

        Returns:
            bool: True if the tree contains no nodes, False otherwise.
        '''
        return self.__root is None
    
    def __validate_natural_number(func):
        '''Decorator to validate that the input is a natural number.'''
        def wrapper(self, val):
            if not isinstance(val, int) or val <= 0:
                raise ValueError(f'{val} is not a natural number. Please provide a positive integer.')
            return func(self, val)
        return wrapper
    
    @__validate_natural_number
    def add(self, val: int) -> None:
        '''Adds a value to the AVL tree, maintaining the AVL property.
        
        Args:
            val (int): The value to be added to the tree.
        '''
        self.__root = self.__add(self.__root, val)

    @__validate_natural_number
    def remove(self, val: int) -> None:
        '''Removes a value from the AVL tree, maintaining the AVL property.
        
        Args:
            val (int): The value to be removed from the tree.
        '''
        self.__root = self.__remove(self.__root, val)

    def min(self) -> int:
        '''Returns the minimum value in the AVL tree.
        
        Returns:
            int: The minimum value in the tree, or None if the tree is empty.
        '''
        if self.is_empty():
            raise ValueError('The tree is empty')
        return self.__min(self.__root).val

    def max(self) -> int:
        '''Returns the maximum value in the AVL tree.
        
        Returns:
            int: The maximum value in the tree, or None if the tree is empty.
        '''
        if self.is_empty():
            raise ValueError('The tree is empty')
        return self.__max(self.__root).val
    
    def traverse(self, type: str = 'inorder') -> list:
        '''Traverses the AVL tree and returns the values in a specified order.
        
        Args:
            type (str): The type of traversal ('inorder', 'preorder', 'postorder').
        
        Returns:
            list: A list of values in the order of traversal.
        '''
        if type == 'inorder':
            return self.__inorder_traversal(self.__root)
        elif type == 'preorder':
            return self.__preorder_traversal(self.__root)
        elif type == 'postorder':
            return self.__postorder_traversal(self.__root)
        else:
            raise ValueError('Unknown traversal type')  # Raise an error for invalid traversal type

    def merge(self, tree: 'AVLTree') -> None:
        '''Merges another AVL tree into this AVL tree.
        
        Args:
            tree (AVLTree): The AVL tree to be merged with this tree.
        
        This method is not yet implemented.
        '''
        pass # admin dopishet zavtra, potomuchto hochet kyshat
    
    def split(self) -> None:
        '''Splits the AVL tree into two trees based on a specified value.
        
        This method is not yet implemented.
        '''
        pass # admin dopishet zavtra, potomuchto hochet kyshat
    
    def check_validity(self) -> bool:
        '''Checks the validity of the AVL tree to ensure it maintains the AVL properties.
        
        Returns:
            bool: True if the tree is valid, False otherwise.
        '''
        is_valid, _ = self.__check_node(self.__root)
        return is_valid
    
    def __check_node(self, x: Node) -> tuple[bool, int]:
        '''Helper function to check the validity of the AVL tree properties for a given node.
        
        Returns:
            A tuple (is_valid, height) where is_valid is a boolean indicating if the subtree
            is valid, and height is the height of the subtree.
        '''
        if x is None:
            return True, 0  # An empty subtree is valid and has height 0

        left_valid, left_height = self.__check_node(x.left)
        right_valid, right_height = self.__check_node(x.right)

        if not left_valid or not right_valid:  # Check the BST property
            return False, 0  # If either subtree is invalid, the whole tree is invalid

        if (x.left is not None and x.left.val >= x.val) or \
            (x.right is not None and x.right.val <= x.val):
            return False, 0  # Violation of BST property

        if abs(left_height - right_height) > 1:  # Check the AVL property
            return False, 0  # Violation of AVL property

        return True, max(left_height, right_height) + 1 # Return validity and height of the current subtree
    
    def __min(self, x: Node) -> Node:
        '''Finds the node with the minimum value in the subtree rooted at x.
        
        Args:
            x (Node): The root node of the subtree.
        
        Returns:
            Node: The node with the minimum value.
        '''
        return x if x.left is None else self.__min(x.left)

    def __max(self, x: Node) -> Node:
        '''Finds the node with the maximum value in the subtree rooted at x.
        
        Args:
            x (Node): The root node of the subtree.
        
        Returns:
            Node: The node with the maximum value.
        '''
        return x if x.right is None else self.__max(x.right)
    
    def __inorder_traversal(self, x: Node) -> list:
        '''Performs an inorder traversal of the subtree rooted at x.
        
        Args:
            x (Node): The root node of the subtree.
        
        Returns:
            list: A list of values in the order of inorder traversal.
        '''
        if x is None:
            return []
        return self.__inorder_traversal(x.left) + [x.val] + self.__inorder_traversal(x.right)

    def __preorder_traversal(self, x: Node) -> list:
        '''Performs a preorder traversal of the subtree rooted at x.
        
        Args:
            x (Node): The root node of the subtree.
        
        Returns:
            list: A list of values in the order of preorder traversal.
        '''
        if x is None:
            return []
        return [x.val] + self.__preorder_traversal(x.left) + self.__preorder_traversal(x.right)

    def __postorder_traversal(self, x: Node, retlist: list = []) -> list:
        '''Performs a postorder traversal of the subtree rooted at x.
        
        Args:
            x (Node): The root node of the subtree.
            retlist (list): A list to accumulate the values during traversal (default is an empty list).
        
        Returns:
            list: A list of values in the order of postorder traversal.
        '''
        if x is None:
            return retlist
        return self.__postorder_traversal(x.left, retlist) + self.__postorder_traversal(x.right, retlist) + [x.val]

    def __contains(self, x: Node, val: int) -> bool:
        '''Checks if a value is present in the subtree rooted at x.
        
        Args:
            x (Node): The root node of the subtree.
            val (int): The value to search for in the subtree.
        
        Returns:
            bool: True if the value is found, False otherwise.
        '''
        if x is None:
            return False
        if x.val < val:
            return self.__contains(x.right, val)
        elif x.val > val:
            return self.__contains(x.left, val)
        return True
    
    def __add(self, x: Node, val: int) -> Node:
        '''Adds a value to the subtree rooted at x, maintaining the AVL property.
        
        Args:
            x (Node): The root node of the subtree.
            val (int): The value to be added to the subtree.
        
        Returns:
            Node: The new root of the subtree after insertion.
        '''
        if x is None:
            self.__len += 1  # Increment the count of nodes
            return self.Node(val)  # Create a new node with the given value
        if x.val < val:
            x.right = self.__add(x.right, val)  # Add to the right subtree
        elif x.val > val:
            x.left = self.__add(x.left, val)  # Add to the left subtree
        return self.__balance(x)  # Balance the subtree after insertion

    def __remove(self, x: Node, val: int) -> Node:
        '''Removes a value from the subtree rooted at x, maintaining the AVL property.
        
        Args:
            x (Node): The root node of the subtree.
            val (int): The value to be removed from the subtree.
        
        Returns:
            Node: The new root of the subtree after removal.
        '''
        if x is None:
            return x  # Value not found, return None
        if x.val < val:
            x.right = self.__remove(x.right, val)  # Remove from the right subtree
        elif x.val > val:
            x.left = self.__remove(x.left, val)  # Remove from the left subtree
        else:
            self.__len -= 1  # Decrement the count of nodes
            left = x.left
            right = x.right
            if right is None:
                return left  # If there is no right child, return the left child
            min_node = self.__min(right)  # Find the minimum node in the right subtree
            min_node.right = self.__remove_min(right)  # Remove the minimum node from the right subtree
            min_node.left = left  # Attach the left subtree
            return self.__balance(min_node)  # Balance the subtree after removal
        return self.__balance(x)  # Balance the subtree after removal

    def __height(self, x: Node) -> int:
        '''Returns the height of the node x.
        
        Args:
            x (Node): The node whose height is to be determined.
        
        Returns:
            int: The height of the node, or 0 if the node is None.
        '''
        return 0 if x is None else x.height  # Return 0 for None, otherwise return the node's height

    def __update_height(self, x: Node) -> None:
        '''Updates the height of the node x based on the heights of its children.
        
        Args:
            x (Node): The node whose height is to be updated.
        '''
        x.height = 1 + max(self.__height(x.left), self.__height(x.right))  # Set height to 1 + max height of children
    
    def __bfactor(self, x: Node) -> int:
        '''Calculates the balance factor of the node x.
        
        The balance factor is defined as the height of the left subtree minus the height of the right subtree.
        
        Args:
            x (Node): The node for which the balance factor is calculated.
        
        Returns:
            int: The balance factor of the node.
        '''
        return self.__height(x.left) - self.__height(x.right)

    def __balance(self, x: Node) -> Node:
        '''Balances the subtree rooted at x to maintain the AVL property.
        
        Args:
            x (Node): The root node of the subtree to be balanced.
        
        Returns:
            Node: The new root of the balanced subtree.
        '''
        self.__update_height(x)  # Update the height of the node
        if self.__bfactor(x) == 2:  # Left heavy
            if self.__bfactor(x.left) < 0:  # Left-Right case
                x.left = self.__rotate_left(x.left)
            return self.__rotate_right(x)  # Left-Left case
        elif self.__bfactor(x) == -2:  # Right heavy
            if self.__bfactor(x.right) > 0:  # Right-Left case
                x.right = self.__rotate_right(x.right)
            return self.__rotate_left(x)  # Right-Right case
        return x  # No balancing needed

    def __rotate_left(self, a: Node) -> Node:
        '''Performs a left rotation around the node a.
        
            A             B
           / \           / \
          p   B    =>   A   r
             / \       / \
            q   r     p   q
        
        Args:
            a (Node): The root node of the subtree to be rotated.
        
        Returns:
            Node: The new root of the subtree after rotation.
        '''
        b = a.right
        a.right = b.left
        b.left = a
        self.__update_height(a)
        self.__update_height(b)
        return b  # Return new root

    def __rotate_right(self, b: Node) -> Node:
        '''Performs a right rotation around the node b.
        
            B            A        
           / \          / \       
          A   r   =>   p   B
         / \          / \
        p   q        q   r
        
        Args:
            b (Node): The root node of the subtree to be rotated.
        
        Returns:
            Node: The new root of the subtree after rotation.
        '''
        a = b.left
        b.left = a.right
        a.right = b
        self.__update_height(b)
        self.__update_height(a)
        return a  # Return new root

    def __remove_min(self, x: Node) -> Node:
        '''Removes the node with the minimum value from the subtree rooted at x.
        
        Args:
            x (Node): The root node of the subtree.
        
        Returns:
            Node: The new root of the subtree after removing the minimum node.
        '''
        if x.left is None:
            return x.right  # If there is no left child, return the right child
        x.left = self.__remove_min(x.left)  # Recursively remove the minimum node
        return self.__balance(x)  # Balance the subtree after removal

    def __min_node(self, x: Node) -> Node:
        '''Finds the node with the minimum value in the subtree rooted at x.
        
        Args:
            x (Node): The root node of the subtree.
        
        Returns:
            Node: The node with the minimum value.
        '''
        return x if x.left is None else self.__min_node(x.left)  # Traverse left until the minimum node is found