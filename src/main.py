import argparse
from file_utils import process_files
from similarity import similarity_grouper
from similarity import simple_similarity_checker
from utils import *

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
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Process the files
    file_names, file_contents = process_files(args)

    if args.files:
        changes, similarity_percentage = simple_similarity_checker(file_contents)
        print("Changes between the files:")
        print(changes)
        print(f"Similarity Percentage: {similarity_percentage * 100:.2f}%")
        print(file_names[0])
        print(file_names[1])
    else:
        if len(file_names) > 1:
            # Group the files based on similarity
            groups = similarity_grouper(file_names, file_contents, args.threshold)
            unique_files = []
            # Display the grouped files
            for file_group in groups:
                if len(file_group) > 1:
                    print("Files that are similar")
                    for file in file_group:
                        print(file)
                else:
                    unique_files.append(file_group[0])
            if len(unique_files) > 0:
                for file in unique_files:
                    print("File that is unique", file)
        else:
            print("No files to compare.")

if __name__ == "__main__":
    main()