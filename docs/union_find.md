# Union-Find

The Union-Find data structure, also known as Disjoint Set Union (DSU), is a data structure that keeps track of a partition of a set into disjoint (non-overlapping) subsets. It provides efficient operations for union and find.

## Implementation

The Union-Find implementation in `utils.py` includes the following methods:

#### `__init__(self, n)`
Initializes the Union-Find data structure with `n` elements.

- **Parameters**:
  - `n` (int): The number of elements.

#### `find(self, x)`
Finds the representative of the set containing `x` with path compression.

- **Parameters**:
  - `x` (int): The element to find.
- **Returns**:
  - `int`: The representative of the set containing `x`.

#### `union(self, a, b)`
Unions the sets containing `a` and `b`.

- **Parameters**:
  - `a` (int): The first element.
  - `b` (int): The second element.

#### `size(self, x)`
Returns the size of the set containing `x`.

- **Parameters**:
  - `x` (int): The element whose set size is to be found.
- **Returns**:
  - `int`: The size of the set containing `x`.

#### `is_same_set(self, a, b)`
Checks if `a` and `b` are in the same set.

- **Parameters**:
  - `a` (int): The first element.
  - `b` (int): The second element.
- **Returns**:
  - `bool`: `True` if `a` and `b` are in the same set, `False` otherwise.

## Time Complexity

Both `find` and `union` operations have an amortized time complexity of nearly O(1), specifically O(α(n)), where α is the inverse Ackermann function, which grows very slowly. This makes the Union-Find data structure extremely efficient for practical use.

## Example

Here is an example of how to use the Union-Find data structure:

```python
# Example usage
uf = UnionFind(10)
uf.union(1, 2)
uf.union(3, 4)
uf.union(2, 4)
print(uf.find(1))  # Output: 1
print(uf.find(3))  # Output: 1
print(uf.find(4))  # Output: 1
```

In this example, we create a Union-Find data structure with 10 elements. We then perform union operations to merge sets and use the find operation to determine the representative of each set.

## Purpose
*The purpose of the `UnionFind` data structure in this project is to efficiently group files that exceed a specified similarity threshold when compared. By using the Union-Find algorithm, we can quickly determine and merge sets of files that are similar, thereby improving execution time and reducing the number of unnecessary comparisons. This optimization ensures that the similarity checking process is both effective and efficient, making it suitable for handling large codebases.*