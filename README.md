# PySimChecker

PySimChecker is a tool designed to detect similarity between source codes, even when they have been obfuscated using various techniques. It is ideal for programming teachers and students who want to verify the originality of the code.

## Key Features

- **Similarity Detection:** Detects similarity between source codes, even if they contain obfuscation techniques.
- **Advanced Analysis:** Utilizes tokenization, and edit distance to perform the analysis.

## Technologies Used

- **Python:** Main programming language.
- **Tokenization:** Breaks down the source code into tokens for detailed analysis.
- **Edit Distance:** To measure the similarity between different code fragments.

## Installation

No additional dependencies are required. You only need to have Python installed on your system.

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/pysimchecker.git
    ```
2. Navigate to the project directory:
    ```sh
    cd pysimchecker
    ```
3. Install the package:
    ```sh
    pip install .
    ```

## Arguments

- `--path`, `-p`: Path to the directory containing the source code files.
- `--files`, `-f`: Specific input files to compare.
- `--recursive`, `-r`: Recursively search through directories.
- `--threshold`, `-t`: Similarity threshold (default: 0.75, range: 0.0 - 1.0).
- `--window-percentage`, `-w`: Window percentage (default: 1.0, range: 0.0 - 1.0).

## Usage

PySimChecker can be used from the command line. Here are some usage examples:

### Compare Specific Files
```sh
pysimchecker --files file1.py file2.py
```

### Analyze an Entire Directory
```sh
pysimchecker --path /path/to/directory --recursive
```

### Adjust the Similarity Threshold
```sh
pysimchecker --path /path/to/directory --threshold 0.8
```

### Adjust the Window Percentage
```sh
pysimchecker --path /path/to/directory --window-percentage 0.5
```

## Contributing

Contributions are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## Additional Documentation
For more information on the techniques used, you can refer to the following resources:

- [Edit Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [Tokenization](https://en.wikipedia.org/wiki/Tokenization)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Links

- [Repository](https://github.com/EdsonEddy/pysimchecker)
- [Documentation](https://github.com/EdsonEddy/pysimchecker/wiki)
- [Report a Bug](https://github.com/EdsonEddy/pysimchecker/issues)