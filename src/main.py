import argparse
from file_utils import process_files
from similarity import similarity_grouper
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
    
    # Add the 'window-percentage' argument with range validation (0.0 - 1.0)
    parser.add_argument('--window-percentage', '-w', type=get_window_percentage, default=1.0, help='The window percentage (default: 1.0, range: 0.0 - 1.0)')

    # Parse the arguments
    args = parser.parse_args()
    
    # Process the files
    file_names, file_contents = process_files(args)

    if len(file_names) > 1:
        # Group the files based on similarity
        groups = similarity_grouper(file_names, file_contents, args.threshold, args.window_percentage)

        # Display the grouped files
        for group_index, file_group in enumerate(groups):
            print(f"Group {group_index + 1}:")
            for file in file_group:
                print(file)
    else:
        print("No files to compare.")

if __name__ == "__main__":
    main()