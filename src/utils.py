from collections import namedtuple
from constants import ADD_HIGHLIGHT_COLOR, DELETE_HIGHLIGHT_COLOR, END_COLOR, IRRELEVANT_TOKENS, TOKENS_WITHOUT_TRANSFORMATION
from pygments import lex
from pygments.token import STANDARD_TYPES
from pygments.lexers import guess_lexer

# Utility functions for similarity detection

def get_method(method):
    """
    Returns the method to use for similarity detection.
    """
    if method == 'myers':
        return MyersDiff()
    elif method == 'lev':
        return Levenshtein()
    # Default method is MyersDiff
    return MyersDiff()

def get_similarity_coefficient(edit_distance, len_seq_a, len_seq_b, method):
    """
    Calculate the similarity percentage between two sequences based on their edit distance.
    Args:
        edit_distance (int): The edit distance between the two sequences.
        len_seq_a (int): The length of the first sequence.
        len_seq_b (int): The length of the second sequence.
        method (str): The method used for similarity detection.
    Returns:
        float: The similarity percentage between the two sequences.
    """
    if method == 'myers':
        return (1 - edit_distance / (len_seq_a + len_seq_b))
    elif method == 'lev':
        return (1 - edit_distance / max(len_seq_a, len_seq_b))
    # Default method is myers
    return (1 - edit_distance / (len_seq_a + len_seq_b))

# Algorithms and Data Structures

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
    
class Tokenizer:
    def get_tokenized_code(self, code_string, token_table, withTokenText=False):
        """
        Tokenizes the given code string and filters out irrelevant tokens.

        Args:
            code_string (str): The source code as a string.

        Returns:
            list: A list of relevant token types from the tokenized code.
        """

        lexer = guess_lexer(code_string)
        tokens = []
        for token in lex(code_string, lexer):
            token_type = token[0]
            if token_type not in IRRELEVANT_TOKENS:
                if token_type in TOKENS_WITHOUT_TRANSFORMATION:
                    token_content = [token[1]]
                else:
                    token_content = [token_table[token_type]]
                if withTokenText:
                    token_content.append(token[1])
                tokens.append(token_content)
        return tokens
    
    def get_token_table(self):
        """
        Create a token table for the standard token types.
        Returns:
            dict: A dictionary mapping token types to unique integer identifiers.
        """
        token_table = {}
        
        for type_key in STANDARD_TYPES.keys():
            token_table[type_key] = len(token_table)
        return token_table

class MyersDiff:
    Keep = namedtuple('Keep', ['item'])
    Insert = namedtuple('Insert', ['item'])
    Remove = namedtuple('Remove', ['item'])
    Frontier = namedtuple('Frontier', ['x', 'history'])

    def __init__(self):
        self.frontier = {}
        self.history = []

    def compare(self, element_a, element_b):
        # Compare the token identifiers of two elements
        return element_a[0] == element_b[0]

    def get_fast_edit_distance(self, sequence_a, sequence_b):
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
                while x < len_a and y < len_b and self.compare(sequence_a[x], sequence_b[y]):
                    x += 1
                    y += 1
                v[k] = x
                if x >= len_a and y >= len_b:
                    return d
        return max_length

    def get_edit_distance(self, sequence_a, sequence_b):
        """
        Calculate the difference between two sequences.

        This method computes the differences between `sequence_a` and `sequence_b` using a variation of the Myers diff algorithm.
        It tracks the changes required to transform `sequence_a` into `sequence_b` and stores the history of these changes.

        Args:
            sequence_a (list): The first sequence to compare.
            sequence_b (list): The second sequence to compare.

        Returns:
            None: The result is stored in `self.history`.

        Attributes:
            self.frontier (dict): A dictionary that keeps track of the furthest reaching points in the edit graph.
            self.history (list): A list that stores the sequence of operations to transform `sequence_a` into `sequence_b`.

        Internal Classes:
            self.Frontier: A helper class to store the current position and history of operations.
            self.Insert: A helper class to represent an insert operation.
            self.Remove: A helper class to represent a remove operation.
            self.Keep: A helper class to represent a keep (no-op) operation.
        """
        a_max = len(sequence_a)
        b_max = len(sequence_b)
        max_length = a_max + b_max
        self.frontier = {1: self.Frontier(0, [])}

        for d in range(a_max + b_max + 1):
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

                if 1 <= y <= b_max and go_down:
                    # Insert the text of token from sequence_b
                    current_history.append(self.Insert(sequence_b[y - 1][1]))
                elif 1 <= x <= a_max:
                    # Remove the text of token from sequence_a
                    current_history.append(self.Remove(sequence_a[x - 1][1]))

                while x < a_max and y < b_max and self.compare(sequence_a[x], sequence_b[y]):
                    x += 1
                    y += 1
                    current_history.append(self.Keep(sequence_a[x - 1][1]))

                self.frontier[k] = self.Frontier(x, current_history)

                if x >= a_max and y >= b_max:
                    self.history = current_history
                    return d
        return max_length

    def get_changes(self):
        """
        Generate a list of changes based on the history of operations.

        This method iterates over the `self.history` attribute, which contains a 
        sequence of operations. Depending on the type of operation (Keep, Insert, 
        or Remove), it appends a formatted string to the `changes` list:
        - [KEEP] followed by the item for Keep operations
        - [ADD] followed by the item for Insert operations
        - [DELETE] followed by the item for Remove operations

        Returns:
            list: A list of strings representing the changes.
        """
        changes_with_add = []
        changes_with_delete = []
        for elem in self.history:
            if isinstance(elem, self.Keep):
                changes_with_add.append(str(elem.item))
                changes_with_delete.append(str(elem.item))
            elif isinstance(elem, self.Insert):
                changes_with_add.append(f'{ADD_HIGHLIGHT_COLOR}{str(elem.item)}{END_COLOR}')
            elif isinstance(elem, self.Remove):
                changes_with_delete.append(f'{DELETE_HIGHLIGHT_COLOR}{str(elem.item)}{END_COLOR}')
        return ''.join(token for token in changes_with_add), ''.join(token for token in changes_with_delete)

class Levenshtein:

    def compare(self, element_a, element_b):
        # Compare the token identifiers of two elements
        return element_a[0] == element_b[0]

    def get_fast_edit_distance(self, sequence_a, sequence_b):
        """
        Calculate the edit distance between two sequences using a window of a specified percentage.
        Args:
            sequence_a (list): The first sequence.
            sequence_b (list): The second sequence.
                
        Returns:
            int: The minimum cost to transform sequence_a into sequence_b.
        
        Description:
            This optimized version of the edit distance algorithm uses a 
            memory-efficient approach to store only the necessary information.
        """
        # Swap the sequences for memory efficiency
        if len(sequence_b) > len(sequence_a):
            sequence_a, sequence_b = sequence_b, sequence_a

        len_a = len(sequence_a) + 1
        len_b = len(sequence_b) + 1

        # Create a dynamic programming table with dimensions 2 x len_b
        dp = [[0] * len_b for _ in range(2)]

        for i in range(1, len_a):
            # Swap the rows for the current and previous iterations
            dp[0], dp[1] = dp[1], dp[0]
            dp[1][0] = i
            
            for j in range(1, len_b):
                # Calculate the cost of different operations: insert, delete, and replace
                insert = dp[1][j - 1] + 1
                delete = dp[0][j] + 1
                replace = dp[0][j - 1] + (not self.compare(sequence_a[i - 1], sequence_b[j - 1]))
                
                # Choose the minimum cost among the three operations
                dp[1][j] = min(insert, delete, replace)

        # Return the minimum cost to transform sequence_a into sequence_b    
        return dp[1][len_b - 1]
    
    def get_edit_distance(self, sequence_a, sequence_b):
        # TODO: Implement the Levenshtein edit distance algorithm
        return self.get_fast_edit_distance(sequence_a, sequence_b)
    
    def get_changes(self):
        # TODO: Implement the method to get the changes between two sequences
        return '', ''