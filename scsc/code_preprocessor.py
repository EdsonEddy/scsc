from .constants import IRRELEVANT_TOKENS, TOKENS_WITHOUT_TRANSFORMATION
from pygments import lex
from pygments.token import STANDARD_TYPES
from pygments.lexers import guess_lexer
from csim import ANTLR_parse
from csim import Normalize
from .gst_adapter import SignatureFactory
import os

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
                # TODO: the token table should be created based on the tokens found in the code
                if token_type in TOKENS_WITHOUT_TRANSFORMATION or not token_type in self.token_table:
                    token_content = [token_str, token_str]
                else:
                    token_content = [self.token_table[token_type], token_str]
                tokens.append(token_content)
        
        return tokens
    
    def tokenize_and_hash_code(self, code_string):
        # Tokenize the code string and hash the tokens
        tokens = self.tokenize_code(code_string)
        token_hashes = [hash(tuple(token)) for token in tokens]
        return token_hashes
    
    def normalize_code(self, code_string):
        T1 = ANTLR_parse(code_string)
        return Normalize(T1)
    
    def get_complete_path(self, file_name):
        return os.path.abspath(file_name)
    
    def get_signature(self, code_string):
        return SignatureFactory(code_string)

    def preprocess_code(self, code_string, file_name):
        if self.method == 'ted':
            return self.add_main(code_string)
        elif self.method == 'mdiff':
            return self.tokenize_code(code_string)
        elif self.method == 'lf':
            return self.get_complete_path(file_name)
        elif self.method == 'gst':
            return self.get_signature(code_string)
        elif self.method == 'trs':
            return self.tokenize_and_hash_code(code_string)
        elif self.method == 'csim':
            return self.normalize_code(code_string)
        
        # Default method return the same code
        return self.add_main(code_string)