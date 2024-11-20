# Levenshtein Algorithm

The `get_edit_distance` function calculates the edit distance between two sequences. This optimized version of the edit distance algorithm reduces memory usage.

## Parameters

- `sequence_a` (list): The first sequence.
- `sequence_b` (list): The second sequence.

## Returns

- `int`: The minimum cost to transform `sequence_a` into `sequence_b`.

## Optimized Version

### Time Complexity

The traditional edit distance algorithm has a time complexity of O(n * m), where `n` and `m` are the lengths of the two sequences.

### Memory Efficiency

The traditional algorithm uses a 2D table of size (n+1) x (m+1) to store the intermediate results, which requires O(n * m) space. The optimized version uses a 2-row table of size 2 x (m+1), which reduces the space complexity to O(m).

### How It Works

1. **Dynamic Programming Table**: A 2-row dynamic programming table is used to store the intermediate results.

### Detailed Description

The function first swaps the sequences if `sequence_b` is longer than `sequence_a` to ensure memory efficiency. A dynamic programming table with dimensions 2 x (length of the shorter sequence + 1) is created.

For each element in `sequence_a`, the function performs the necessary insert, delete, and replace operations within these bounds. The minimum cost among these operations is stored in the dynamic programming table.

Finally, the function returns the minimum cost to transform `sequence_a` into `sequence_b`.
