"""
Capital One Coding Challenge - Comment Counter
Python 3.7.4 - PEP 8
Author: Mathieu Godin
"""


class SingleLineCommentToken:
    """Class that represents a single line comment token"""
    def __init__(self, token=""):
        self.token = token


class MultiLineCommentTokens:
    """Class that represents a multi-line comment tokens"""
    def __init__(self, left_token="", right_token=""):
        self.left_token = left_token
        self.right_token = right_token


class CommentTokens:
    """Class that represents possible comment tokens
    in a programming language"""
    def __init__(self, single=[], multi=[]):
        # Token for start of single line comment
        self.single = single
        # Left and right tokens for start
        # and end of multi-line comment
        self.multi = multi
        # Indicates if multi-line comments are supported
        self.multi_supported = single != []
        # Indicates if single line comments are supported
        self.single_supported = multi != []

"""Dictionary that maps programming languages file
extensions to their respective programming languages"""
languages_extensions = {
    "adb": "Ada",
    "ads": "Ada",
    "apl": "APL",
    "scpt": "AppleScript",
    "scptd": "AppleScript",
    "applescript": "AppleScript",
    "sbl": "BASIC"}

"""Dictionary that maps programming languages to their
respective programming languages single line and multi-line
comment tokens"""
languages_comment_tokens = {
    "Ada": CommentTokens(
        [SingleLineCommentToken("--")]),
    "APL": CommentTokens(
        [SingleLineCommentToken("⍝")],
        [MultiLineCommentTokens("⊣", "⊢")]),
    "AppleScript": CommentTokens(
        [SingleLineCommentToken("--")],
        [MultiLineCommentTokens("(*", "*)")]),
    "BASIC": CommentTokens("REM ")}
