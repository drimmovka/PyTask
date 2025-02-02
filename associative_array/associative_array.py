'''
AssociativeArray Module

This module provides an implementation of an associative array (also known as a map or dictionary)
using different types of hash tables for storage. The AssociativeArray class allows users to choose
between two methods of collision resolution: open addressing and separate chaining.

Key Features:
- Supports dynamic storage of key-value pairs with efficient retrieval.
- Allows the user to specify the type of hash table to use for managing the associative array.
- Provides standard dictionary-like operations such as adding, retrieving, and removing key-value pairs.
- Implements iteration over keys and items, enabling easy access to stored data.

Usage:
    To use this associative array implementation, create an instance of the AssociativeArray class
    with the desired hash table type. You can then use standard operations to manipulate the data.

Example:
    from associative_array import AssociativeArray

    # Create an associative array using open addressing
    array = AssociativeArray(type='open_addressing')
    
    # Add key-value pairs
    array['key1'] = 'value1'
    array['key2'] = 'value2'

    # Retrieve a value
    value = array['key1']  # Returns 'value1'

    # Check if a key exists
    exists = 'key2' in array  # Returns True

    # Remove a key-value pair
    array.remove('key1')

    # Print the associative array
    print(array)

Classes:
    AssociativeArray: A class representing an associative array that uses a hash table for storage.
        - Methods:
            __getitem__(key): Retrieve the value associated with the given key.
            __setitem__(key, value): Set the value for the given key.
            __contains__(key): Check if the associative array contains the specified key.
            remove(key): Remove the key-value pair associated with the given key.
            clear(): Reset the state of the associative array.
            keys(): Return a list of keys in the associative array.
            items(): Return a list of (key, value) pairs in the associative array.
            __len__(): Return the number of key-value pairs in the associative array.
            __iter__(): Initialize the iteration over the associative array.
            __next__(): Retrieve the next item in the iteration.
'''

from .hash_table_open_addressing import HashTableOpenAddressing
from .hash_table_separate_chaining import HashTableSeparateChaining

class AssociativeArray:
    def __init__(self, type='open_addressing'):
        '''Initialize the associative array with the specified map type.

        Args:
            type (str): The type of map to use ("open_addressing" or "separate_chaining").

        Raises:
            ValueError: If the specified type is not supported.
        '''
        if type == 'open_addressing':
            self.__map = HashTableOpenAddressing()
        elif type == 'separate_chaining':
            self.__map = HashTableSeparateChaining()
        else:
            raise ValueError(f'Unsupported map type: "{type}". Supported types are "open_addressing" and "separate_chaining".')
    
    def __str__(self) -> str:
        '''Return a string representation of the associative array.'''
        return str(self.__map)  # Delegate to the 

    def __repr__(self) -> str:
        '''Return a string representation of the associative array for debugging.'''
        return repr(self.__map)  # Delegate to the 

    def __len__(self) -> int:
        '''Return the number of key-value pairs in the associative array.'''
        return len(self.__map)  # Delegate to the 
    
    def __getitem__(self, key):
        '''Retrieve the value associated with the given key.'''
        return self.__map[key]  # Delegate to the underlying
    
    def __setitem__(self, key, value):
        '''Set the value for the given key in the associative array.'''
        self.__map[key] = value  # Delegate to the underlying

    def __contains__(self, key):
        '''Check if the associative array contains the specified key.'''
        return key in self.__map  # Delegate to the underlying

    def __iter__(self):
        '''Initialize the iteration over the associative array.'''
        return self.__map.__iter__()  # Delegate to the underlying

    def __next__(self):
        '''Retrieve the next item in the iteration.'''
        return self.__map.__next__()  # Delegate to the underlying
    
    def keys(self):
        '''Return a list of keys in the associative array.'''
        return self.__map.keys()  # Delegate to the underlying

    def items(self):
        '''Return a list of (key, value) pairs in the associative array.'''
        return self.__map.items()  # Delegate to the underlying
    
    def remove(self, key):
        '''Remove the key-value pair associated with the given key.'''
        self.__map.remove(key)  # Delegate to the underlying

    def clear(self):
        '''Reset the state of the associative array.'''
        self.__map.clear()  # Delegate to the underlying