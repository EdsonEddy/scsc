## PySimChecker Methods

### `get_extra_info`

- **Description:** This method retrieves additional information about the PySimChecker process. It generates a detailed report of the code changes, including insertions and deletions.
- **Arguments:** None
- **Returns:** `str` - A formatted string containing the extra information.

### `get_similarity`

- **Description:** This method calculates the similarity between two pieces of code using the Myers' algorithm. PySimChecker is a tool that compares source code files and detects similarities based on tokenization and edit distance.
- **Arguments:**
  - `code1 (str)`: The first piece of code.
  - `code2 (str)`: The second piece of code.
- **Returns:** `float` - The similarity score between the two pieces of code.

### Algorithm Used: Myers' Algorithm

- **Description:** Myers' algorithm is an efficient algorithm for calculating the edit distance between two sequences. The edit distance is the minimum number of operations required to transform one sequence into another, where the allowed operations are insertions and deletions.
- **Algorithm Description:** Myers' algorithm finds the shortest path in an edit graph, where nodes represent prefixes of the sequences and edges represent edit operations (insertions, deletions, or matches). The algorithm optimizes space and time usage by using a vector to store the furthest reaching points in the edit graph.
- **Complexity:**
  - **Time:** O((N+M)D), where N and M are the lengths of the sequences and D is the edit distance.
  - **Space:** O(N+M), due to the use of a vector to store the furthest reaching points in the edit graph.