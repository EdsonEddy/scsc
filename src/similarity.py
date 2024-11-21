from utils import UnionFind, Tokenizer, get_method, get_similarity_coefficient

def simple_similarity_checker(file_contents, method):
    tokenizer = Tokenizer()
    token_table = tokenizer.get_token_table()
    tokenized_file1 = tokenizer.get_tokenized_code(file_contents[0], token_table, True)
    tokenized_file2 = tokenizer.get_tokenized_code(file_contents[1], token_table, True)
    len_a = len(tokenized_file1)
    len_b = len(tokenized_file2)
    similarity_method = get_method(method)
    edit_distance = similarity_method.get_edit_distance(tokenized_file1, tokenized_file2)
    similarity_percentage = get_similarity_coefficient(edit_distance, len_a, len_b, method)
    changes_with_add, changes_with_delete = similarity_method.get_changes()
    return changes_with_add, changes_with_delete, similarity_percentage

def similarity_grouper(file_names, file_contents, threshold, method):
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
    tokenizer = Tokenizer()
    similarity_method = get_method(method)

    token_table = tokenizer.get_token_table()
    tokenized_files = [tokenizer.get_tokenized_code(file, token_table) for file in file_contents]
    percentage_file = [0.00] * file_number

    for i in range(file_number - 1):
        if uf.find(i) == i:
            seq_a = tokenized_files[i]
            len_a = len(tokenized_files[i])
            for j in range(i + 1, file_number):
                if uf.find(j) == j:
                    seq_b = tokenized_files[j]
                    len_b = len(tokenized_files[j])
                    edit_distance = similarity_method.get_fast_edit_distance(seq_a, seq_b)
                    similarity_percentage = get_similarity_coefficient(edit_distance, len_a, len_b, method)
                    if similarity_percentage > threshold:
                        uf.union(i, j)
                        percentage_file[j] = similarity_percentage
    
    groups = {}
    percentage_groups = {}
    for i in range(file_number):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(file_names[i])
        if root not in percentage_groups:
            percentage_groups[root] = []
        percentage_groups[root].append(percentage_file[i])

    return list(groups.values()), list(percentage_groups.values())