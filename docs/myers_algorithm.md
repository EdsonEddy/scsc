## Myers' Algorithm

Myers' algorithm is an efficient algorithm for calculating the edit distance between two sequences. The edit distance is the minimum number of operations required to transform one sequence into another, where the allowed operations are insertions and deletions.

### Algorithm Description

Myers' algorithm uses a dynamic programming technique to find the sequence of operations that transforms one sequence into another with the least cost. The implementation in this project uses a variation of the algorithm that optimizes space and time usage.

### Complexity

- **Time:** O((N+M)D), where N and M are the lengths of the sequences and D is the edit distance.
- **Space:** O(N+M), due to the use of a vector to store the furthest reaching points in the edit graph.

### Example Usage

```python
# Example usage of Myers' algorithm
diff = MyersDiff()
edit_distance = diff.calculate_diff(sequence_a, sequence_b)
changes_with_add, changes_with_delete = diff.get_changes()
print(f"Edit Distance: {edit_distance}")
print(f"Changes with additions: {changes_with_add}")
print(f"Changes with deletions: {changes_with_delete}")
```