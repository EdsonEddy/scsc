from collections import namedtuple
from .constants import ADD_HIGHLIGHT_COLOR, DELETE_HIGHLIGHT_COLOR, END_COLOR

class PySimChecker():
    Keep = namedtuple('Keep', ['item'])
    Insert = namedtuple('Insert', ['item'])
    Remove = namedtuple('Remove', ['item'])
    Frontier = namedtuple('Frontier', ['x', 'history'])

    def __init__(self, verbose):
        self.frontier = {}
        self.history = []
        self.verbose = verbose

    def compare(self, element_a, element_b):
        return element_a[0] == element_b[0]

    def calculate_edit_distance(self, sequence_a, sequence_b):
        len_a = len(sequence_a)
        len_b = len(sequence_b)
        max_length = len_a + len_b

        # If verbose is False, return the fast edit distance without storing the history
        if not self.verbose:
            v = [0] * (2 * max_length + 1)
            v[1] = 0
            for d in range(max_length + 1):
                for k in range(-d, d + 1, 2):
                    if k == -d or (k != d and v[k - 1] < v[k + 1]):
                        x = v[k + 1]
                    else:
                        x = v[k - 1] + 1
                    y = x - k
                    while x < len_a and y < len_b and self.compare(sequence_a[x], sequence_b[y]):
                        x += 1
                        y += 1
                    v[k] = x
                    if x >= len_a and y >= len_b:
                        return d
            return max_length

        self.frontier = {1: self.Frontier(0, [])}
        self.history = []

        for d in range(len_a + len_b + 1):
            for k in range(-d, d + 1, 2):
                go_down = (k == -d or (k != d and self.frontier[k - 1].x < self.frontier[k + 1].x))
                if go_down:
                    old_x, current_history = self.frontier[k + 1]
                    x = old_x
                else:
                    old_x, current_history = self.frontier[k - 1]
                    x = old_x + 1
                current_history = current_history[:]
                y = x - k
                if 1 <= y <= len_b and go_down:
                    # Insert the text of token from sequence_b
                    current_history.append(self.Insert(sequence_b[y - 1][1]))
                elif 1 <= x <= len_a:
                    # Remove the text of token from sequence_a
                    current_history.append(self.Remove(sequence_a[x - 1][1]))
                while x < len_a and y < len_b and self.compare(sequence_a[x], sequence_b[y]):
                    x += 1
                    y += 1
                    current_history.append(self.Keep(sequence_a[x - 1][1]))
                self.frontier[k] = self.Frontier(x, current_history)
                if x >= len_a and y >= len_b:
                    self.history = current_history
                    return d
        
        return max_length

    def get_extra_info(self):

        code_with_inserts = []
        code_with_removes = []

        for elem in self.history:
            if isinstance(elem, self.Keep):
                code_with_inserts.append(str(elem.item))
                code_with_removes.append(str(elem.item))
            elif isinstance(elem, self.Insert):
                code_with_inserts.append(f'{ADD_HIGHLIGHT_COLOR}{str(elem.item)}{END_COLOR}')
            elif isinstance(elem, self.Remove):
                code_with_removes.append(f'{DELETE_HIGHLIGHT_COLOR}{str(elem.item)}{END_COLOR}')
        
        code_with_inserts = ''.join(token for token in code_with_inserts)
        code_with_removes = ''.join(token for token in code_with_removes)
        separator = '---'
        output = (
            f"{code_with_removes}\n"
            f"{separator}\n"
            f"{code_with_inserts}"
        )

        return output

    def get_similarity_coefficient(self, proccesed_code1, proccesed_code2):
        edit_distance = self.calculate_edit_distance(proccesed_code1, proccesed_code2)
        len_a = len(proccesed_code1)
        len_b = len(proccesed_code2)
        
        return (1 - edit_distance / (len_a + len_b))