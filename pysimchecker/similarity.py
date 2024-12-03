from .union_find import UnionFind
from .code_preprocessor import CodePreprocessor
from .pysimchecker import PySimChecker
from .pycode_similar import PyCodeSimilar
from .locmoss import Locmoss
from .codesight import Codesight
from .constants import END_COLOR, DELETE_TEXT_COLOR, ADD_TEXT_COLOR
import csv

def get_similarity_method(method, verbose):
    if method == 'pycode_similar':
        return PyCodeSimilar(verbose)
    elif method == 'pysimchecker':
        return PySimChecker(verbose)
    elif method == 'locmoss':
        return Locmoss(verbose)
    elif method == 'codesight':
        return Codesight(verbose)
    # Default method is PySimChecker
    return PySimChecker(verbose)

def generate_output(file_names, groups, percentage_groups, verbose_groups):
    output = ""
    unique_files = []

    for file_group in groups:
        if len(file_group) > 1:
            file_name_src = file_names[file_group[0]]
            for file in file_group[1:]:
                file_name = file_names[file]
                percentage = percentage_groups[file]
                verbose = verbose_groups[file]
                output += (
                    f"{DELETE_TEXT_COLOR}{file_name_src} is similar to {file_name} with similarity percentage: {percentage * 100:.2f}%{END_COLOR}\n"
                )
                if verbose:
                    output += (
                        f"{verbose}\n"
                    )
        else:
            unique_files.append(file_names[file_group[0]])

    if unique_files:
        for file in unique_files:
            output += (f"\n{ADD_TEXT_COLOR}File that is unique: {file}{END_COLOR}")

    return output

def efficient_comparison_output(file_names, file_contents, threshold, method, verbose):
    file_number = len(file_names)
    
    grouper = UnionFind(file_number)
    processor = CodePreprocessor(method)
    similarity_method = get_similarity_method(method, verbose)

    proccesed_files = [processor.preprocess_code(file_content, file_name) for file_content, file_name in zip(file_contents, file_names)]
    percentage_file = [0.00] * file_number
    verbose_file = [""] * file_number

    for i in range(file_number - 1):
        if grouper.find(i) == i:
            file_a = proccesed_files[i]
            for j in range(i + 1, file_number):
                if grouper.find(j) == j:
                    file_b = proccesed_files[j]
                    similarity_percentage = similarity_method.get_similarity_coefficient(file_a, file_b)
                    if similarity_percentage > threshold:
                        grouper.union(i, j)
                        percentage_file[j] = similarity_percentage
                        if verbose:
                            verbose_file[j] = similarity_method.get_extra_info()
    
    groups = {}
    
    for i in range(file_number):
        root = grouper.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    groups = list(groups.values())
    
    return generate_output(file_names, groups, percentage_file, verbose_file)

def full_comparison_output(file_names, file_contents, method, verbose, csv_file):
    # Add .csv extension if not present
    if not csv_file.endswith(".csv"):
        csv_file += ".csv"

    file_number = len(file_names)
    processor = CodePreprocessor(method)
    similarity_method = get_similarity_method(method, verbose)

    proccesed_files = [processor.preprocess_code(file_content, file_name) for file_content, file_name in zip(file_contents, file_names)]
    
    # Create a matrix to store similarity percentages
    similarity_matrix = [["" for _ in range(file_number + 1)] for _ in range(file_number + 1)]
    
    # Fill the first row and first column with file names
    for i in range(file_number):
        similarity_matrix[0][i + 1] = file_names[i]
        similarity_matrix[i + 1][0] = file_names[i]
    
    # Calculate similarity percentages and fill the matrix
    for i in range(file_number):
        file_a = proccesed_files[i]
        for j in range(file_number):
            if i == j:
                similarity_matrix[i + 1][j + 1] = "100.00%"
            else:
                file_b = proccesed_files[j]
                similarity_percentage = similarity_method.get_similarity_coefficient(file_a, file_b)
                similarity_matrix[i + 1][j + 1] = f"{similarity_percentage * 100:.2f}%"
    
    # Write the matrix to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(similarity_matrix)
    
    return f"Full comparison report generated: {csv_file}"

def similarity_checker(file_names, file_contents, threshold, method, verbose, full_comparison):
    similarity_output = ""
    if full_comparison:
        similarity_output = full_comparison_output(file_names, file_contents, method, verbose, full_comparison)
    else:
        similarity_output = efficient_comparison_output(file_names, file_contents, threshold, method, verbose)
    return similarity_output