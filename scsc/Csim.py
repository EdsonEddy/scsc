from csim import SimilarityIndex
from zss import simple_distance
class Csim():

    def get_similarity_coefficient(self, proccesed_code1, proccesed_code2):
        N1, len_N1 = proccesed_code1
        N2, len_N2 = proccesed_code2
        d = simple_distance(N1, N2)
        result = SimilarityIndex(d, len_N1, len_N2)
        return result