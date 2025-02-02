# README for AssociativeArray Package

## Overview

The `AssociativeArray` package provides an implementation of an associative array (also known as a map or dictionary) using different types of hash tables for storage. The `AssociativeArray` class allows users to choose between two methods of collision resolution: open addressing and separate chaining.

## Key Features
- Supports dynamic storage of key-value pairs with efficient retrieval.
- Allows the user to specify the type of hash table to use for managing the associative array.
- Provides standard dictionary-like operations such as adding, retrieving, and removing key-value pairs.
- Implements iteration over keys and items, enabling easy access to stored data.

## Installation
To use the `AssociativeArray` package, simply include it in your Python project. Ensure that you have Python 3.x installed.

## Usage

### Basic Operations

Here are some examples of how to use the `AssociativeArray` class:

```
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

# Traverse the associative array
print(array.keys())  # Returns a list of keys
print(array.items())  # Returns a list of (key, value) pairs
```

### Conclusion

The `AssociativeArray` package provides a flexible and efficient way to manage key-value pairs using hash tables. With support for different collision resolution methods, it ensures optimal performance for various use cases. Use the provided methods to manipulate and access the data as needed.
