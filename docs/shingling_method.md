# Token Rolling Shingling

## Overview

Token Rolling Shingling is a method used to calculate the similarity between two sequences of tokens. It works by breaking down sequences into overlapping subsets of a fixed size, called shingles, and then comparing these subsets to determine the similarity. This approach is particularly useful for detecting similarities in text or code, even when the sequences are not identical but share common patterns.

## How It Works

1. **Shingle Generation**:  
   The method generates shingles by sliding a window of a fixed size (`w`) over the sequence. Each shingle is a tuple of consecutive tokens.

2. **Jaccard Similarity**:  
   The similarity between two sequences is calculated using the Jaccard similarity coefficient. This is defined as the size of the intersection of two sets of shingles divided by the size of their union.

## Key Components

- **Shingle Size (`w`)**:  
  The default size of each shingle is 5 tokens. This can be adjusted based on the requirements of the analysis.

- **Jaccard Similarity Formula**:  
  \[
  J(A, B) = \frac{|A \cap B|}{|A \cup B|}
  \]  
  Where \(A\) and \(B\) are the sets of shingles from two sequences.

## Implementation

The `TokenRollingShingling` class provides the following key methods:

- `calculate_shingles(sequence)`:  
  Generates shingles from a given sequence.

- `calculate_jaccard_similarity(shingles1, shingles2)`:  
  Computes the Jaccard similarity between two sets of shingles.

- `get_similarity_coefficient(proccesed_code1, proccesed_code2)`:  
  Combines the above methods to calculate the similarity coefficient between two processed sequences of tokens.

## Use Cases

- **Code Similarity Detection**:  
  Useful for identifying similar code snippets, even if they are not identical.

- **Plagiarism Detection**:  
  Helps in detecting copied or slightly modified content.

- **Text Analysis**:  
  Can be applied to compare textual data for similarity.

## Limitations

- **Fixed Shingle Size**:  
  The method relies on a fixed shingle size, which may not capture all patterns in sequences of varying lengths.

- **Performance**:  
  For very large sequences, the computation of shingles and their comparison can be resource-intensive.
