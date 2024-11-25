from constants import IRRELEVANT_TOKENS, TOKENS_WITHOUT_TRANSFORMATION
from pygments import lex
from pygments.token import STANDARD_TYPES
from pygments.lexers import guess_lexer

# Code Preprocessor, includes methods for preprocessing code
class CodePreprocessor:

    def __init__(self, method):
        self.method = method
        self.token_table = self.create_token_table()

    def add_main(self, source_code):
        if ('def main():' in source_code):
            return source_code
        
        code_lines = str(source_code).split('\n')
        code_lines = ['\t' + line + '\n' for line in code_lines]
        code_fixed = ['def main():\n'] + code_lines

        return ''.join(code_fixed)
    
    def create_token_table(self):
        token_table = {}

        for type_key in STANDARD_TYPES.keys():
            token_table[type_key] = len(token_table)
        
        return token_table

    def tokenize_code(self, code_string):
        lexer = guess_lexer(code_string)
        tokens = []

        for token in lex(code_string, lexer):
            token_type = token[0]
            token_str = token[1]
            if token_type not in IRRELEVANT_TOKENS:
                if token_type in TOKENS_WITHOUT_TRANSFORMATION:
                    token_content = [token_str, token_str]
                else:
                    token_content = [self.token_table[token_type], token_str]
                tokens.append(token_content)
        
        return tokens
    
    def preprocess_code(self, code_string):
        if self.method == 'pycode_similar':
            return self.add_main(code_string)
        elif self.method == 'pysimchecker':
            return self.tokenize_code(code_string)
        
        # Default method return the same code
        return code_string