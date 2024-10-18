# Optimized Edit Distance

The `optimized_edit_distance` function calculates the edit distance between two sequences using a window of a specified percentage. This optimized version of the edit distance algorithm reduces both time complexity and memory usage.

## Parameters

- `sequence_a` (list): The first sequence.
- `sequence_b` (list): The second sequence.
- `window_percentage` (float): The window size as a percentage of the shorter sequence.

## Returns

- `int`: The minimum cost to transform `sequence_a` into `sequence_b`.

## Usage

The `optimized_edit_distance` function is used to calculate the minimum number of operations required to transform one sequence into another. The operations can be insertions, deletions, or substitutions.

### Example

```python
from utils import optimized_edit_distance

sequence_a = [1, 2, 3, 4]
sequence_b = [2, 3, 4, 5]
window_percentage = 0.5

distance = optimized_edit_distance(sequence_a, sequence_b, window_percentage)
print(f"The edit distance is: {distance}")
```

## Optimized Version

### Time Complexity

The traditional edit distance algorithm has a time complexity of O(n * m), where `n` and `m` are the lengths of the two sequences. The optimized version reduces this complexity by using a sliding window, which limits comparisons to a subset of elements. The new time complexity is O(n * w), where `w` is the window size, calculated as a percentage of the shorter sequence's length. This approach significantly reduces the number of comparisons, making the algorithm more efficient for large sequences.

### Memory Efficiency

The traditional algorithm uses a 2D table of size (n+1) x (m+1) to store the intermediate results, which requires O(n * m) space. The optimized version uses a 2-row table of size 2 x (m+1), which reduces the space complexity to O(m).

### How It Works

1. **Window Size Calculation**: The window size is calculated as a percentage of the length of the shorter sequence.
2. **Dynamic Programming Table**: A 2-row dynamic programming table is used to store the intermediate results.
3. **Row Swapping**: The rows of the table are swapped at each iteration to reuse the space.
4. **Bounded Comparisons**: Only the elements within the window are compared, reducing the number of operations.

### Detailed Description

The function first swaps the sequences if `sequence_b` is longer than `sequence_a` to ensure memory efficiency. It then calculates the window size based on the `window_percentage`. A dynamic programming table with dimensions 2 x (length of the shorter sequence + 1) is created.

For each element in `sequence_a`, the function calculates the left and right bounds of the window and performs the necessary insert, delete, and replace operations within these bounds. The minimum cost among these operations is stored in the dynamic programming table.

Finally, the function returns the minimum cost to transform `sequence_a` into `sequence_b`.

This optimized approach significantly reduces both the time and space complexity, making it suitable for large sequences.

## Purpose

*The purpose of the `optimized_edit_distance` function is to calculate the edit distance between two sequences efficiently, using tokens from source code. This function determines how different two pieces of source code are by computing the minimum number of operations (insertions, deletions, or substitutions) required to transform one sequence into another. By leveraging an optimized algorithm that reduces both time and space complexity through a sliding window approach, the function is particularly suitable for comparing large codebases. This makes it an effective tool for analyzing code similarity and detecting differences in source code.*