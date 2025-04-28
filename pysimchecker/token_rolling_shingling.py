class TokenRollingShingling:
    """
    Token Rolling Shingling
    """

    def __init__(self, verbose):
        self.verbose = verbose
        # The default shingle size is 5
        self.w = 5

    def calculate_shingles(self, sequence):
        """
        Calculate the shingles of a sequence
        """
        shingles = []
        for i in range(len(sequence) - self.w + 1):
            shingle = tuple(sequence[i:i + self.w])
            shingles.append(shingle)
        return shingles
    
    def calculate_jaccard_similarity(self, shingles1, shingles2):
        """
        Calculate the Jaccard similarity between two sets of shingles
        """
        intersection = len(set(shingles1) & set(shingles2))
        union = len(set(shingles1) | set(shingles2))
        return intersection / union if union != 0 else 0.0
    
    def get_extra_info(self):
        return ""

    def get_similarity_coefficient(self, proccesed_code1, proccesed_code2):
        shingles1 = self.calculate_shingles(proccesed_code1)
        shingles2 = self.calculate_shingles(proccesed_code2)
        return self.calculate_jaccard_similarity(shingles1, shingles2)