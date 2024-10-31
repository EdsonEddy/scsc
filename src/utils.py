import argparse
from pathlib import Path
from pygments.token import STANDARD_TYPES

# Utility functions for argument parsing

def get_file(file_path):
    if not Path(file_path).is_file():
        raise argparse.ArgumentTypeError(f"File '{file_path}' does not exist.")
    return file_path

def get_threshold(value):
    try:
        fvalue = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid threshold value: {value}")
    if fvalue < 0.0 or fvalue > 1.0:
        raise argparse.ArgumentTypeError(f"Threshold must be between 0.0 and 1.0")
    return fvalue

def get_window_percentage(value):
    fvalue = float(value)
    if fvalue < 0.0 or fvalue > 1.0:
        raise argparse.ArgumentTypeError(f"Window percentage must be between 0.0 and 1.0")
    return fvalue

# Algorithms, Data Structures and utility functions

class UnionFind:
    def __init__(self, n):
        """
        Initialize Union-Find Disjoint Set (UFDS) with n elements.
        """
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        """
        Find the representative of the set containing x with path compression.
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])  # Path compression
        return self.parents[x]

    def union(self, a, b):
        """
        Union the sets containing a and b.
        """
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return

        # Union by rank
        if self.ranks[root_a] < self.ranks[root_b]:
            self.parents[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]
        else:
            self.parents[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
            if self.ranks[root_a] == self.ranks[root_b]:
                self.ranks[root_a] += 1

        self.numdisjoint -= 1

    def size(self, x):
        """
        Return the size of the set containing x.
        """
        return self.sizes[self.find(x)]
    
    def is_same_set(self, a, b):
        """
        Check if a and b are in the same set.
        """
        return self.find(a) == self.find(b)
    
from math import ceil

def optimized_edit_distance(sequence_a, sequence_b, window_percentage):
    """
    Calculate the edit distance between two sequences using a window of a specified percentage.
    Args:
        sequence_a (list): The first sequence.
        sequence_b (list): The second sequence.
        window_percentage (int): The window size as a percentage of the shorter sequence.
    
    Returns:
        int: The minimum cost to transform sequence_a into sequence_b.
    
    Description:
        This optimized version of the edit distance algorithm uses a window to reduce the time complexity,
        and a memory-efficient approach to store only the necessary information.
    """
    # Swap the sequences for memory efficiency
    if len(sequence_b) > len(sequence_a):
        sequence_a, sequence_b = sequence_b, sequence_a

    len_a = len(sequence_a) + 1
    len_b = len(sequence_b) + 1

    # Calculate the window size based on the window percentage
    window_size = ceil(len(sequence_b) * window_percentage)

    # Create a dynamic programming table with dimensions 2 x len_b
    dp = [[0] * len_b for _ in range(2)]

    for i in range(1, len_a):
        # Swap the rows for the current and previous iterations
        dp[0], dp[1] = dp[1], dp[0]
        dp[1][0] = i

        # Calculate the left and right bounds of the window
        left_bound = max(1, i - window_size)
        right_bound = min(len_b, i + window_size + 1)
        
        for j in range(left_bound, right_bound):
            # Get the element from the sequences
            element_a = sequence_a[i - 1][1]
            element_b = sequence_b[j - 1][1]
            # Calculate the cost of different operations: insert, delete, and replace
            insert = dp[1][j - 1] + 1
            delete = dp[0][j] + 1
            replace = dp[0][j - 1] + (element_a != element_b)
            
            # Choose the minimum cost among the three operations
            dp[1][j] = min(insert, delete, replace)

    # Return the minimum cost to transform sequence_a into sequence_b    
    return dp[1][len_b - 1]

def get_similarity_coefficient(method_type, edit_distance, len_seq_a, len_seq_b):
    """
    Calculate the similarity percentage between two sequences based on their edit distance.
    Args:
        edit_distance (int): The edit distance between the two sequences.
        len_seq_a (int): The length of the first sequence.
        len_seq_b (int): The length of the second sequence.
    Returns:
        float: The similarity percentage between the two sequences.
    """

    result = 0
    if method_type == "levenshtein":
        max_length = max(len_seq_a, len_seq_b)
        result = (1 - edit_distance / max_length)
    elif method_type == "myers":
        result = (1 - edit_distance / (len_seq_a + len_seq_b))
    return result

def get_token_table():
    """
    Generates a token table mapping type keys to their corresponding index values.
    This function iterates over the keys in the STANDARD_TYPES dictionary, splits each key
    by periods, and assigns an index to each unique key part. It then creates a token table
    where each type key is mapped to a tuple containing the index of the first and last part
    of the key.
    Returns:
        dict: A dictionary where each key is a type key from STANDARD_TYPES and each value
              is a tuple of two integers representing the index of the first and last part
              of the key.
    """
    type_indexes = {}
    token_table = {}
    
    for type_key in STANDARD_TYPES.keys():
        keys = str(type_key).split(".")
        value = [type_indexes.setdefault(key, len(type_indexes)) for key in keys]
        token_table[type_key] = (value[0], value[-1])
        
    return token_table

def myers_diff(sequence_a, sequence_b):
    """
    Calculate the edit distance between two sequences using the Myers diff algorithm.
    Args:
        sequence_a (list): The first sequence.
        sequence_b (list): The second sequence.
    Returns:
        int: The minimum cost to transform sequence_a into sequence_b.
    Description:
        This function implements the Myers diff algorithm to calculate the edit distance between
        two sequences. The algorithm uses a linear space complexity and a time complexity of O((N+M)D)
        where N and M are the lengths of the sequences and D is the edit distance.
    """
    len_a = len(sequence_a)
    len_b = len(sequence_b)
    max_length = len_a + len_b
    v = [0] * (2 * max_length + 1)
    v[1] = 0
    for d in range(max_length + 1):
        for k in range(-d, d + 1, 2):
            if k == -d or (k != d and v[k - 1] < v[k + 1]):
                x = v[k + 1]
            else:
                x = v[k - 1] + 1
            y = x - k
            while x < len_a and y < len_b and sequence_a[x][1] == sequence_b[y][1]:
                x += 1
                y += 1
            v[k] = x
            if x >= len_a and y >= len_b:
                return d
    return max_length

def similarity_method(method_type, sequence_a, sequence_b, window_percentage):
    if method_type == "levenshtein":
        return optimized_edit_distance(sequence_a, sequence_b, window_percentage)
    elif method_type == "myers":
        return myers_diff(sequence_a, sequence_b)
    return None