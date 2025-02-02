'''
HashTableOpenAddressing Module

This module provides an implementation of a hash table (also known as a hash map) in Python.
The hash table allows for efficient storage and retrieval of key-value pairs using a hashing
function to compute the index for each key.

Key Features:
- Supports dynamic resizing of the hash table to accommodate more elements or reduce size.
- Implements open addressing with linear probing for collision resolution.
- Provides methods for adding, retrieving, and removing key-value pairs.
- Automatically rehashes when the load factor exceeds a specified threshold.

Usage:
    To use this hash table implementation, you can create an instance of the HashTableOpenAddressing class
    and use the provided methods to manipulate key-value pairs.

Example:
    from hash_table import HashTableOpenAddressing

    # Create a new hash table
    ht = HashTableOpenAddressing()
    
    # Add key-value pairs
    ht['key1'] = 'value1'
    ht['key2'] = 'value2'

    # Retrieve a value
    value = ht['key1']  # Returns 'value1'

    # Check if a key exists
    exists = 'key2' in ht  # Returns True

    # Remove a key-value pair
    ht.remove('key1')

    # Print the hash table
    print(ht)

Classes:
    HashTableOpenAddressing: A class representing the hash table data structure.
        - Methods:
            __getitem__(key): Retrieve the value associated with the given key.
            __setitem__(key, val): Set the value for the given key.
            __contains__(key): Check if the hash table contains the specified key.
            remove(key): Remove the key-value pair associated with the given key.
            __rehash(reduce=False): Rehash the hash table to accommodate more or fewer elements.

    Pair: A class representing a key-value pair stored in the hash table.
        - Attributes:
            key: The key of the pair.
            val: The value of the pair.
'''

from .hash_table import HashTable
from typing import Any

class HashTableOpenAddressing(HashTable):
    MAX_LOAD_FACTOR = 0.75  # Maximum load factor
    MIN_LOAD_FACTOR = 0.25  # Minimum load factor
    MIN_BUCKETS_COUNT = 8  # Minimum buckets count
    
    def __init__(self) -> None:
        '''Initialize the hash table.

        Creates an empty hash table with the specified minimum bucket size.
        '''
        super().__init__()
        self.__m: int = self.MIN_BUCKETS_COUNT  # Number of buckets
        self.__buckets: list[HashTableOpenAddressing.Pair] = [None] * self.__m  # Buckets
        self.__deleted: list[bool] = [False] * self.__m  # Flags for deleted buckets
    
    def __str__(self) -> str:
        '''Return a string representation of the hash table.

        Returns:
            str: A string representing the hash table in the format '{key: value, ...}'.
        '''
        retstr: str = ''
        for i in self:
            retstr += str(i) + ', '
        return '{' + retstr[:-2] + '}'
    
    def __repr__(self) -> str:
        '''Return a string representation of the hash table for debugging.

        Returns:
            str: A string with information about length, bucket count, and load factor.
        '''
        retstr: str = ''
        retstr += f'len: {len(self)}\n'
        retstr += f'buckets count: {self.__m}\n'
        retstr += f'load factor: {self.__load_factor()}\n'
        
        for i in self.__buckets:
            retstr += str(i) + '\n'
        return retstr.rstrip()
    
    def __len__(self) -> int:
        '''Return the number of elements in the hash table.'''
        return super().__len__()
    
    def __getitem__(self, key: Any) -> Any:
        '''Retrieve the value associated with the given key.

        Args:
            key (Any): The key for which to retrieve the value.

        Returns:
            Any: The value associated with the key, or None if the key does not exist.
        '''
        pos = self.__pos(key)  # Get the position for the key
        
        # Continue searching until we find an empty bucket and not deleted bucket
        while self.__buckets[pos] is not None or self.__deleted[pos]:
            if self.__buckets[pos] is not None:
                if self.__buckets[pos].key == key:
                    return self.__buckets[pos].val  # Return the value if the key matches
            
            pos = self.__probe_next(pos)  # Move to the next position

        raise KeyError(key)  # Raise error if the key is not found

    def __setitem__(self, key: Any, val: Any) -> None:
        '''Set the value for the given key in the hash table.

        If the key already exists, update its value. If the load factor exceeds
        the maximum, rehash the table.

        Args:
            key (Any): The key to set.
            val (Any): The value to associate with the key.
        '''
        if self.__load_factor() > self.MAX_LOAD_FACTOR:
            self.__rehash()  # Rehash if the load factor exceeds the maximum

        pos = self.__pos(key)  # Get the position for the key
        
        # Continue searching until we find an empty bucket
        while self.__buckets[pos] is not None:
            if self.__buckets[pos].key == key:  # If the key already exists
                self.__buckets[pos].val = val  # Update the value
                return
            
            pos = self.__probe_next(pos)  # Move to the next position
        
        # Insert a new key-value pair
        self.__buckets[pos] = self.Pair(key, val)
        self.__deleted[pos] = False  # Mark the bucket as not deleted
        self._len += 1  # Increment the length of the hash table

    def __contains__(self, key: Any) -> bool:
        '''Check if the hash table contains the specified key.

        Args:
            key (Any): The key to check for existence.

        Returns:
            bool: True if the key exists, False otherwise.
        '''
        try:
            self[key]  # Attempt to access the value using the key.
            return True  # Key exists.
        except KeyError:
            return False  # Key does not exist.

    def __iter__(self):
        '''
        Resets the index to 0 for starting a new iteration.
        
        Returns:
            CustomIterable: The iterator object itself.
        '''
        self.__index = 0
        return self

    def __next__(self) -> object:
        '''
        Retrieves the next item in the iteration that is not None.
        
        Returns:
            object: The next item that is not None.
        
        Raises:
            StopIteration: When there are no more items to iterate over.
        '''
        while self.__index < self.__m:  # self.__m is the total number of buckets
            item = self.__buckets[self.__index]
            self.__index += 1
            if item is not None:
                return item  # Return the found item
        raise StopIteration  # If all items have been iterated over, raise StopIteration

    def keys(self) -> list:
        '''
        Collects and returns a list of keys from the items in the iterable.
        
        Returns:
            list: A list of keys from the items.
        '''
        keys = []
        for i in self:
            keys.append(i.key)
        return keys  # Return the list of keys
    
    def items(self) -> list:
        '''
        Collects and returns a list of (key, value) pairs from the items in the iterable.
        
        Returns:
            list: A list of tuples, each containing a key and its corresponding value.
        '''
        items = []
        for i in self:
            items.append((i.key, i.val))
        return items  # Return the list of (key, value) pairs
    
    def remove(self, key: Any) -> None:
        '''Remove the key-value pair associated with the given key.

        If the key exists, mark the bucket as deleted and decrement the length.

        Args:
            key (Any): The key to remove.
        '''
        pos = self.__pos(key)  # Get the position for the key
        
        # Continue searching until we find an empty bucket or a deleted bucket
        while self.__buckets[pos] is not None or self.__deleted[pos]:
            if self.__buckets[pos] is not None and self.__buckets[pos].key == key:
                self.__buckets[pos] = None  # Remove the key-value pair
                self.__deleted[pos] = True  # Mark the bucket as deleted
                self._len -= 1  # Decrement the length
                break    
                    
            pos = self.__probe_next(pos)  # Move to the next position
        
        if self.__load_factor() < self.MIN_LOAD_FACTOR:
            self.__rehash(True)
    
    def clear(self):
        '''Reset the state of the object to its initial values.'''
        self._len = 0
        self.__m = self.MIN_BUCKETS_COUNT
        self.__buckets = [None] * self.__m
        self.__deleted = [False] * self.__m
    
    def __pos(self, key: Any) -> int:
        '''Calculate the position of the given key in the hash table.

        This method uses the hash of the key to determine the initial position
        in the buckets array.

        Args:
            key (Any): The key for which to calculate the position.

        Returns:
            int: The calculated position in the buckets array.
        '''
        return hash(key) % len(self.__buckets)  # Return the hash modulo the number of buckets

    def __probe_next(self, pos: int) -> int:
        '''Get the next position in the buckets array for probing.

        This method calculates the next position by incrementing the current
        position and wrapping around if necessary.

        Args:
            pos (int): The current position in the buckets array.

        Returns:
            int: The next position in the buckets array.
        '''
        return (pos + 1) % len(self.__buckets)  # Return the next position, wrapping around

    def __load_factor(self) -> float:
        '''Calculate the current load factor of the hash table.

        The load factor is defined as the ratio of the number of elements
        to the number of buckets.

        Returns:
            float: The current load factor of the hash table.
        '''
        return self._len / len(self.__buckets)  # Return the load factor

    def __rehash(self, reduce: bool = False) -> None:
        '''Rehash the hash table to accommodate more or fewer elements.

        This method can either double the size of the buckets array to
        accommodate more elements or halve the size if the reduce parameter
        is set to True, ensuring that the size does not go below the minimum.

        Args:
            reduce (bool): If True, reduce the size of the hash table.
        '''
        tmp = self.__buckets  # Store the current buckets
        
        if reduce:
            # Halve the number of buckets, ensuring it does not go below MIN_BUCKETS_COUNT
            self.__m = max(self.MIN_BUCKETS_COUNT, self.__m // 2)
        else:
            # Double the number of buckets
            self.__m = self.__m * 2
        
        self.__buckets = [None] * self.__m  # Create a new buckets array
        self.__deleted = [False] * self.__m  # Reset the deleted flags
        
        for i in tmp:
            if i is not None:  # Check if the bucket is not empty
                pos = self.__pos(i.key)  # Calculate the new position for the key
                while self.__buckets[pos] is not None:  # Find an empty bucket
                    pos = self.__probe_next(pos)  # Probe to the next position
                self.__buckets[pos] = i  # Place the key-value pair in the new bucket