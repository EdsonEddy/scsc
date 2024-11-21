import argparse
from file_utils import process_files, get_file, get_threshold
from similarity import similarity_grouper, simple_similarity_checker
from constants import END_COLOR, DELETE_TEXT_COLOR, ADD_TEXT_COLOR

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='PySimChecker: Detect similarity between source codes.')
    
    # Create a mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)
    
    # Add the 'path' argument to the group
    group.add_argument('--path', '-p', type=str, help='Path to the directory containing the source code files')
    
    # Add the 'files' argument to the group
    group.add_argument('--files', '-f', type=get_file, nargs=2, help='The input files')
    
    # Add the 'recursive' argument
    parser.add_argument('--recursive', '-r', action='store_true', help='Recursively search through directories')

    # Add the 'threshold' argument with range validation (0.0 - 1.0)
    parser.add_argument('--threshold', '-t', type=get_threshold, default=0.75, help='The similarity threshold (default: 0.75, range: 0.0 - 1.0)')
    
     # Add the 'method' argument
    parser.add_argument('--method', '-m', type=str, choices=['myers', 'lev'], default='myers', help='The method to use for similarity detection (default: myers)')

    # Parse the arguments
    args = parser.parse_args()
    
    # Process the files
    file_names, file_contents = process_files(args)

    if args.files:
        changes_with_add, changes_with_delete, similarity_percentage = simple_similarity_checker(file_contents, args.method)
        separator = '---'
        output = (
            f"{changes_with_delete}\n"
            f"{separator}\n"
            f"{changes_with_add}\n"
            f"Similarity Percentage: {similarity_percentage * 100:.2f}%"
        )
        print(output)
    else:
        if len(file_names) > 1:
            # Group the files based on similarity
            groups, percentage_groups = similarity_grouper(file_names, file_contents, args.threshold, args.method)
            unique_files = []
            tabulation = "   "

            # Display the grouped files
            for file_group, per_group in zip(groups, percentage_groups):
                if len(file_group) > 1:
                    print(f"{DELETE_TEXT_COLOR}Files that are similar with {file_group[0]}{END_COLOR}")
                    for file, percentage in zip(file_group[1:], per_group[1:]):
                        print(f"{tabulation}{file} with similarity percentage: {percentage * 100:.2f}%")
                else:
                    unique_files.append(file_group[0])

            # Display unique files
            if unique_files:
                for file in unique_files:
                    print(f"{ADD_TEXT_COLOR}File that is unique: {file}{END_COLOR}")
        else:
            print("No files to compare.")

if __name__ == "__main__":
    main()