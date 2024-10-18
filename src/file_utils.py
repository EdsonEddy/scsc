import os

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return file_path, content
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return file_path, None

def process_files(args):
    # Storage for file names and contents
    file_names = []
    file_contents = []

    # Process the files based on the provided arguments
    if args.path:
        path = args.path
        
        # Check if the path is a valid directory
        if not os.path.isdir(path):
            print(f"Error: The path '{path}' is not a valid directory.")
            return
        
        # Process the files in the directory
        if args.recursive:
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        # print(f"Processing file: {file_path}")
                        file_name, content = read_file(file_path)
                        # Store the file name and content
                        file_names.append(file_name)
                        file_contents.append(content)
        else:
            for file in os.listdir(path):
                file_path = os.path.join(path, file)
                if os.path.isfile(file_path) and file.endswith('.py'):
                    # print(f"Processing file: {file_path}")
                    file_name, content = read_file(file_path)
                    # Store the file name and content
                    file_names.append(file_name)
                    file_contents.append(content)
    elif args.files:
        file1, file2 = args.files
        # print(f"Processing files: {file1} and {file2}")
        file_name1, content1 = read_file(file1)
        file_name2, content2 = read_file(file2)
        # Store the file name and content
        file_names.extend([file_name1, file_name2])
        file_contents.extend([content1, content2])
    
    return file_names, file_contents