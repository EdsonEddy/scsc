from pygments.token import Token

# Constants for filtering irrelevant tokens
IRRELEVANT_TOKENS = {
    # Token.Comment,
    # Token.Comment.Hashbang,
    # Token.Comment.Multiline,
    # Token.Comment.Preproc,
    # Token.Comment.PreprocFile,
    # Token.Comment.Single,
    # Token.Comment.Special,
    # Token.Text,
    # Token.Whitespace,
    # Token.Punctuation,
    # Token.Punctuation.Marker,
    # Token.String.Doc,
    # Token.Generic,
    # Token.Generic.Deleted,
    # Token.Generic.Emph,
    # Token.Generic.Error,
    # Token.Generic.Heading,
    # Token.Generic.Inserted,
    # Token.Generic.Output,
    # Token.Generic.Prompt,
    # Token.Generic.Strong,
    # Token.Generic.EmphStrong,
    # Token.Generic.Subheading,
    # Token.Generic.Traceback,
    # Token.Keyword.Namespace,
}

# Constants for the Myers' Algorithm
KEEP = 'K'
ADD = '+'
DELETE = '-'

# ANSI color codes for terminal output
ADD_HIGHLIGHT = '\033[42m'
DELETE_HIGHLIGHT = '\033[41m'
END_HIGHLIGHT = '\033[0m'