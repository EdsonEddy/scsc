import argparse
from pathlib import Path
from pygments.token import STANDARD_TYPES
from collections import namedtuple

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

class MyersDiff:
    Keep = namedtuple('Keep', ['item'])
    Insert = namedtuple('Insert', ['item'])
    Remove = namedtuple('Remove', ['item'])
    Frontier = namedtuple('Frontier', ['x', 'history'])

    def __init__(self):
        self.frontier = {}
        self.history = []

    def calculate_diff(self, a_seq, b_seq):
        self.a_seq = a_seq
        self.b_seq = b_seq
        self.a_max = len(a_seq)
        self.b_max = len(b_seq)
        self.frontier = {1: self.Frontier(0, [])}

        for d in range(self.a_max + self.b_max + 1):
            for k in range(-d, d + 1, 2):
                go_down = (k == -d or (k != d and self.frontier[k - 1].x < self.frontier[k + 1].x))
                if go_down:
                    old_x, current_history = self.frontier[k + 1]
                    x = old_x
                else:
                    old_x, current_history = self.frontier[k - 1]
                    x = old_x + 1

                current_history = current_history[:]
                y = x - k

                if 1 <= y <= self.b_max and go_down:
                    current_history.append(self.Insert(self.b_seq[y - 1]))
                elif 1 <= x <= self.a_max:
                    current_history.append(self.Remove(self.a_seq[x - 1]))

                while x < self.a_max and y < self.b_max and self.a_seq[x] == self.b_seq[y]:
                    x += 1
                    y += 1
                    current_history.append(self.Keep(self.a_seq[x - 1]))

                self.frontier[k] = self.Frontier(x, current_history)

                if x >= self.a_max and y >= self.b_max:
                    self.history = current_history
                    return

    def get_diff(self):
        """
        Generate a list of changes based on the history of operations.

        This method iterates over the `self.history` attribute, which contains a 
        sequence of operations. Depending on the type of operation (Keep, Insert, 
        or Remove), it appends a formatted string to the `changes` list:
        - ' ' followed by the item for Keep operations
        - '+' followed by the item for Insert operations
        - '-' followed by the item for Remove operations

        Returns:
            list: A list of strings representing the changes.
        """
        changes = []
        for elem in self.history:
            if isinstance(elem, self.Keep):
                changes.append(' ' + str(elem.item))
            elif isinstance(elem, self.Insert):
                changes.append('+' + str(elem.item))
            elif isinstance(elem, self.Remove):
                changes.append('-' + str(elem.item))
        return changes
