import argparse
from .file_utils import process_files, get_file, get_threshold
from .similarity import similarity_checker

def main():
    """
    Main function to parse command-line arguments and execute the similarity checker.
    Arguments:
        --path, -p (str): Path to the directory containing the source code files.
        --files, -f (str, nargs=2): The input two files to compare.
        --recursive, -r (bool): Recursively search through directories.
        --threshold, -t (float): The similarity threshold (default: 0.75, range: 0.0 - 1.0).
        --method, -m (str): The method to use for similarity detection (default: pysimchecker).
        --verbose, -v (bool): Display verbose output
    Returns:
        None
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description='PySimChecker: Detect similarity between source codes.')
    
    # Create a mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)
    
    # Add the 'path' argument to the group
    group.add_argument('--path', '-p', type=str, help='Path to the directory containing the source code files')
    
    # Add the 'files' argument to the group
    group.add_argument('--files', '-f', type=get_file, nargs=2, help='The input two files to compare')
    
    # Add the 'recursive' argument
    parser.add_argument('--recursive', '-r', action='store_true', help='Recursively search through directories')

    # Add the 'threshold' argument with range validation (0.0 - 1.0)
    parser.add_argument('--threshold', '-t', type=get_threshold, default=0.75, help='The similarity threshold (default: 0.75, range: 0.0 - 1.0)')
    
    # Add the 'method' argument
    parser.add_argument('--method', '-m', type=str, choices=['pysimchecker', 'pycode_similar', 'locmoss'], default='pysimchecker', help='The method to use for similarity detection (default: pysimchecker)')

    # Add the 'verbose' argument
    parser.add_argument('--verbose', '-v', action='store_true', help='Display verbose output')

    # Parse the arguments
    args = parser.parse_args()
    
    # Process the files
    file_names, file_contents = process_files(args)

    if len(file_names) > 1:
        results = similarity_checker(file_names, file_contents, args.threshold, args.method, args.verbose)
        print(results)
    else:
        print("No files to compare.")

if __name__ == "__main__":
    main()