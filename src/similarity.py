from utils import UnionFind
from utils import get_similarity_coefficient
from utils import similarity_method
from utils import get_token_table

from pygments import lex
from pygments.lexers import guess_lexer

from constants import IRRELEVANT_TOKENS

def get_tokenized_code(code_string, token_table):
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
            tokens.append(token_table[token_type])
    return tokens

def similarity_grouper(file_names, file_contents, threshold, window_percentage):
    """
    Groups files based on their similarity.

    Args:
        file_names (list): A list of file names.
        file_contents (list): A list of file contents corresponding to the file names.
        threshold (float): The similarity threshold for grouping.
        window_percentage (float): The window percentage for the edit distance calculation.

    Returns:
        list: A list of groups, where each group is a list of file names that are similar.
    """
    file_number = len(file_names)
    uf = UnionFind(file_number)

    token_table = get_token_table()
    tokenized_files = [get_tokenized_code(file, token_table) for file in file_contents]

    for i in range(file_number - 1):
        if uf.find(i) == i:
            seq_a = tokenized_files[i]
            len_a = len(tokenized_files[i])
            for j in range(i + 1, file_number):
                if uf.find(j) == j:
                    seq_b = tokenized_files[j]
                    len_b = len(tokenized_files[j])
                    edit_distance = similarity_method('myers', seq_a, seq_b, window_percentage)
                    similarity_percentage = get_similarity_coefficient('myers', edit_distance, len_a, len_b)
                    if similarity_percentage > threshold:
                        uf.union(i, j)

    groups = {}
    for i in range(file_number):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(file_names[i])

    return list(groups.values())