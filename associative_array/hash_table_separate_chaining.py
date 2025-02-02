'''
HashTableSeparateChaining Module

This module provides an implementation of a hash table (also known as a hash map) in Python
using the separate chaining method for collision resolution. The hash table allows for efficient
storage and retrieval of key-value pairs by using a hashing function to compute the index for each key.

Key Features:
- Supports dynamic resizing of the hash table to accommodate more elements or reduce size.
- Implements separate chaining for collision resolution, allowing multiple key-value pairs to be stored in the same bucket.
- Provides methods for adding, retrieving, and removing key-value pairs.
- Automatically rehashes when the load factor exceeds a specified threshold.

Usage:
    To use this hash table implementation, you can create an instance of the HashTableSeparateChaining class
    and use the provided methods to manipulate key-value pairs.

Example:
    from hash_table import HashTableSeparateChaining

    # Create a new hash table
    ht = HashTableSeparateChaining()
    
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
    HashTableSeparateChaining: A class representing the hash table data structure.
        - Methods:
            __getitem__(key): Retrieve the value associated with the given key.
            __setitem__(key, val): Set the value for the given key.
            __contains__(key): Check if the hash table contains the specified key.
            remove(key): Remove the key-value pair associated with the given key.
            clear(): Reset the state of the hash table to its initial values.
            keys(): Return a list of keys in the hash table.
            items(): Return a list of (key, value) pairs in the hash table.
            __rehash(reduce=False): Rehash the hash table to accommodate more or fewer elements.

    Pair: A class representing a key-value pair stored in the hash table.
        - Attributes:
            key: The key of the pair.
            val: The value of the pair.
'''

from .hash_table import HashTable
from typing import Any
from collections import deque

class HashTableSeparateChaining(HashTable):
    MAX_LOAD_FACTOR = 0.75  # Maximum load factor
    MIN_LOAD_FACTOR = 0.25  # Minimum load factor
    MIN_BUCKETS_COUNT = 1  # Minimum buckets count
    
    def __init__(self) -> None:
        '''Initialize the hash table.

        Creates an empty hash table with the specified minimum bucket size.
        '''
        super().__init__()
        self.__m: int = self.MIN_BUCKETS_COUNT  # Number of buckets
        self.__buckets: list[deque[HashTable.Pair]] = [deque() for _ in range(self.__m)]  # Buckets
    
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
        
        for i in range(len(self.__buckets)):
            current_chain = ''
            for j in self.__buckets[i]:
                current_chain += str(j) + ', '
            retstr += f'{i}: [{current_chain[:-2]}]\n'
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
        pos = self.__pos(key)  # Get the position (bucket index) for the key using the hash function
        
        # Iterate through the items in the corresponding bucket
        for i in self.__buckets[pos]:
            if i.key == key:  # Check if the current item's key matches the requested key
                return i.val  # Return the associated value if found

        raise KeyError(key)  # Raise KeyError if the key is not found in the bucket

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
        
        # Iterate through the items in the corresponding bucket
        for i in self.__buckets[pos]:
            if i.key == key:  # If the key already exists
                i.val = val  # Update the value
                return
                
        # Insert a new key-value pair
        self.__buckets[pos].append(HashTable.Pair(key, val))
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
        self.__item_index = 0
        self.__bucket_index = 0
        return self

    def __next__(self) -> object:
        '''
        Retrieves the next item in the iteration that is not None.
        
        Returns:
            object: The next item that is not None.
        
        Raises:
            StopIteration: When there are no more items to iterate over.
        '''
        while self.__bucket_index < self.__m:
            if self.__item_index < len(self.__buckets[self.__bucket_index]):
                item = self.__buckets[self.__bucket_index][self.__item_index]
                self.__item_index += 1
                return item
            else:
                self.__bucket_index += 1
                self.__item_index = 0
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
        
        for i in range(len(self.__buckets[pos])):
            if self.__buckets[pos][i].key == key:
                del self.__buckets[pos][i]
                self._len -= 1
                break
        
        if self.__load_factor() < self.MIN_LOAD_FACTOR:
            self.__rehash(True)
    
    def clear(self):
        '''Reset the state of the object to its initial values.'''
        self._len = 0
        self.__m = self.MIN_BUCKETS_COUNT
        self.__buckets = [deque() for _ in range(self.__m)]
    
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
        
        self.__buckets = [deque() for _ in range(self.__m)]  # Create a new buckets array
        
        for i in tmp:
            for j in i:
                pos = self.__pos(j.key)  # Calculate the new position for the key
                self.__buckets[pos].append(j)