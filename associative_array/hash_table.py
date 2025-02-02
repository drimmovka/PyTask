'''
HashTable Module

This module provides an abstract base implementation of a hash table (also known as a hash map) in Python.
The HashTable class serves as a parent class for specific hash table implementations, such as separate chaining
and open addressing. It defines the basic structure and common methods that must be implemented by subclasses.

Key Features:
- Defines a nested Pair class to represent key-value pairs.
- Provides method signatures for adding, retrieving, and removing key-value pairs, which must be implemented in subclasses.
- Supports dynamic resizing based on load factor to maintain performance.
- Allows iteration over keys and items stored in the hash table through defined methods.

Usage:
    This class is not intended for direct instantiation. Instead, you should create a subclass that implements
    the required methods. For example, you can create a HashTableSeparateChaining or HashTableOpenAddressing class
    that inherits from HashTable and provides concrete implementations of the abstract methods.

Classes:
    HashTable: An abstract class representing the base structure of a hash table.
        - Methods:
            __getitem__(key): Abstract method to retrieve the value associated with the given key.
            __setitem__(key, val): Abstract method to set the value for the given key.
            __contains__(key): Check if the hash table contains the specified key.
            remove(key): Abstract method to remove the key-value pair associated with the given key.
            clear(): Reset the state of the hash table to its initial values.
            keys(): Collect and return a list of keys in the hash table.
            items(): Collect and return a list of (key, value) pairs in the hash table.
            __len__(): Return the number of elements in the hash table.
            __iter__(): Prepare the hash table for iteration.
            __next__(): Retrieve the next item in the iteration.
            __pos(key): Calculate the position of the given key in the hash table.
            __load_factor(): Calculate the current load factor of the hash table.
            __rehash(reduce=False): Rehash the hash table to accommodate more or fewer elements.

    Pair: A class representing a key-value pair stored in the hash table.
        - Attributes:
            key: The key of the pair.
            val: The value of the pair.
'''

from typing import Any

class HashTable:
    
    class Pair:
        def __init__(self, key: Any, val: Any) -> None:
            '''Initialize a key-value pair.

            Args:
                key (Any): The key of the pair.
                val (Any): The value of the pair.
            '''
            self.key: Any = key
            self.val: Any = val

        def __str__(self) -> str:
            '''Return a string representation of the key-value pair.

            Returns:
                str: A string in the format 'key: value'.
            '''
            return f'{self.key}: {self.val}'
    
    def __init__(self) -> None:
        '''Initialize the hash table.'''
        self._len: int = 0  # Current length (number of elements)
    
    def __str__(self) -> str:
        '''Return a string representation of the hash table.'''
        pass
    
    def __repr__(self) -> str:
        '''Return a string representation of the hash table for debugging.'''
        pass
    
    def __len__(self) -> int:
        '''Return the number of elements in the hash table.

        Returns:
            int: The number of elements in the hash table.
        '''
        return self._len
    
    def __getitem__(self, key: Any) -> Any:
        '''Retrieve the value associated with the given key.'''
        pass

    def __setitem__(self, key: Any, val: Any) -> None:
        '''Set the value for the given key in the hash table.'''
        pass
    
    def __contains__(self, key: Any) -> bool:
        '''Check if the hash table contains the specified key.'''
        pass

    def __iter__(self):
        '''Resets the index to 0 for starting a new iteration.'''
        pass

    def __next__(self) -> object:
        '''Retrieves the next item in the iteration that is not None.'''
        pass
        
    def keys(self) -> list:
        '''Collects and returns a list of keys from the items in the iterable.'''
        pass
    
    def items(self) -> list:
        '''Collects and returns a list of (key, value) pairs from the items in the iterable.'''
        pass
    
    def remove(self, key: Any) -> None:
        '''Remove the key-value pair associated with the given key.'''
        pass
    
    def clear(self):
        '''Reset the state of the object to its initial values.'''
        pass
    
    def __pos(self, key: Any) -> int:
        '''Calculate the position of the given key in the hash table.'''
        pass

    def __load_factor(self) -> float:
        '''Calculate the current load factor of the hash table.'''
        pass

    def __rehash(self, reduce: bool = False) -> None:
        '''Rehash the hash table to accommodate more or fewer elements.'''
        pass