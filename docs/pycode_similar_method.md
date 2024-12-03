## PyCodeSimilar Methods

### `get_similarity`

- **Description:** This method calculates the similarity between two pieces of code using the PyCodeSimilar algorithm. PyCodeSimilar is a tool that compares Python source code files and detects similarities based on Abstract Syntax Tree (AST) and Tree Edit Distance.
- **Arguments:**
  - `code1 (str)`: The first piece of code.
  - `code2 (str)`: The second piece of code.
- **Returns:** `float` - The similarity score between the two pieces of code.

### `get_differences`

- **Description:** This method identifies the differences between two pieces of code using the PyCodeSimilar algorithm.
- **Arguments:**
  - `code1 (str)`: The first piece of code.
  - `code2 (str)`: The second piece of code.
- **Returns:** `list` - A list of differences between the two pieces of code.

### Algorithms Used: AST and Tree Edit Distance

- **Abstract Syntax Tree (AST):** AST is a tree representation of the abstract syntactic structure of source code. Each node of the tree denotes a construct occurring in the source code.
- **Tree Edit Distance:** Tree Edit Distance is a measure of similarity between two tree structures. It is defined as the minimum number of edit operations required to transform one tree into another.