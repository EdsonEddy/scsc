from utils import UnionFind
from utils import get_similarity_coefficient
from utils import get_token_table
from utils import MyersDiff

from pygments import lex
from pygments.lexers import guess_lexer

from constants import IRRELEVANT_TOKENS, TOKENS_WITHOUT_TRANSFORMATION

def get_tokenized_code(code_string, token_table, withTokenText=False):
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

def simple_similarity_checker(file_contents):
    token_table = get_token_table()
    tokenized_file1 = get_tokenized_code(file_contents[0], token_table, True)
    tokenized_file2 = get_tokenized_code(file_contents[1], token_table, True)
    len_a = len(tokenized_file1)
    len_b = len(tokenized_file2)
    diff = MyersDiff()
    edit_distance = diff.calculate_diff(tokenized_file1, tokenized_file2)
    similarity_percentage = get_similarity_coefficient(edit_distance, len_a, len_b)
    changes_with_add, changes_with_delete = diff.get_changes()
    return changes_with_add, changes_with_delete, similarity_percentage

def similarity_grouper(file_names, file_contents, threshold):
    """
    Groups files based on their similarity.

    Args:
        file_names (list): A list of file names.
        file_contents (list): A list of file contents corresponding to the file names.
        threshold (float): The similarity threshold for grouping.

    Returns:
        list: A list of groups, where each group is a list of file names that are similar.
    """
    file_number = len(file_names)
    uf = UnionFind(file_number)
    diff = MyersDiff()

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
                    edit_distance = diff.calculate_fast_diff(seq_a, seq_b)
                    similarity_percentage = get_similarity_coefficient(edit_distance, len_a, len_b)
                    if similarity_percentage > threshold:
                        uf.union(i, j)

    groups = {}
    for i in range(file_number):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(file_names[i])

    return list(groups.values())