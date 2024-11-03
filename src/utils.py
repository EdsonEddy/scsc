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
    
def get_similarity_coefficient(edit_distance, len_seq_a, len_seq_b):
    """
    Calculate the similarity percentage between two sequences based on their edit distance.
    Args:
        edit_distance (int): The edit distance between the two sequences.
        len_seq_a (int): The length of the first sequence.
        len_seq_b (int): The length of the second sequence.
    Returns:
        float: The similarity percentage between the two sequences.
    """
    return (1 - edit_distance / (len_seq_a + len_seq_b))

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
