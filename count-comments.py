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
    "sbl": "BASIC",
    "bas": "QBASIC",
    "vb": "Visual Basic",
    "vbs": "VBScript",
    "vbe": "VBScript",
    "wsf": "VBScript",
    "wsc": "VBScript",
    "c": "C",
    "h": "C",
    "cc": "C",
    "cpp": "C",
    "cxx": "C",
    "c++": "C",
    "hh": "C",
    "hpp": "C",
    "hxx": "C",
    "h++": "C",
    "cs": "C",
    "m": "C",
    "mm": "C",
    "go": "C",
    "groovy": "C",
    "gvy": "C",
    "gy": "C",
    "gsh": "C",
    "cfm": "ColdFusion",
    "cfc": "ColdFusion",
    "f77": "Fortran 77",
    "f": "Fortran 77",
    "for": "Fortran 77",
    "fpp": "Fortran 77",
    "ftn": "Fortran 77",
    "f90": "Fortran",
    "f95": "Fortran",
    "f03": "Fortran",
    "f08": "Fortran",
    "hs": "Haskell",
    "lhs": "Haskell",
    "tex": "LaTeX",
    "java": "Java",
    "js": "JavaScript",
    "mjs": "JavaScript",
    "ts": "JavaScript",
    "jsx": "JavaScript",
    "tsx": "JavaScript",
    "sh": "Shell script",
    "r": "R",
    "lua": "Lua",
    "e": "Eiffel",
    "sql": "SQL",
    "vhdl": "VHDL",
    "vhd": "VHDL",
    "ml": "OCaml",
    "mli": "OCaml",
    "pp": "Pascal",
    "pas": "Pascal",
    "inc": "Pascal",
    "pl": "Perl",
    "p6": "Raku",
    "raku": "Raku",
    "php": "PHP",
    "phtml": "PHP",
    "php3": "PHP",
    "php4": "PHP",
    "php5": "PHP",
    "php7": "PHP",
    "ps1": "PowerShell",
    "py": "Python",
    "rb": "Ruby",
    "swift": "Swift",
    "xml": "XML",
    "htm": "XML",
    "html": "XML",
    "css": "CSS"
    }

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
    "BASIC": CommentTokens(
        [SingleLineCommentToken("REM ")]),
    "QBASIC": CommentTokens(
        [SingleLineCommentToken("REM "),
         SingleLineCommentToken("\'")]),
    "Visual Basic": CommentTokens(
        [SingleLineCommentToken("REM "),
         SingleLineCommentToken("\'")]),
    "C": CommentTokens(
        [SingleLineCommentToken("//")],
        [MultiLineCommentTokens("/*", "*/")]),
    "ColdFusion": CommentTokens(
        multi=[MultiLineCommentTokens("<!---", "--->")]),
    "Fortran 77": CommentTokens(
        [SingleLineCommentToken("\nC"),
         SingleLineCommentToken("\nc"),
         SingleLineCommentToken("\n*")]),
    "Fortran": CommentTokens(
        [SingleLineCommentToken("!")]),
    "Haskell": CommentTokens(
        [SingleLineCommentToken("--")],
        [MultiLineCommentTokens("{-", "-}")]),
    "LaTeX": CommentTokens(
        [SingleLineCommentToken("%")]),
    "Java": CommentTokens(
        [SingleLineCommentToken("//")],
        [MultiLineCommentTokens("/*", "*/")]),
    "JavaScript": CommentTokens(
        [SingleLineCommentToken("//")],
        [MultiLineCommentTokens("/*", "*/")]),
    "Lua": CommentTokens(
        [SingleLineCommentToken("--")],
        [MultiLineCommentTokens("--[[", "]]")]),
    "Eiffel": CommentTokens(
        [SingleLineCommentToken("--")]),
    "SQL": CommentTokens(
        [SingleLineCommentToken("--")],
        [MultiLineCommentTokens("/*", "*/")]),
    "VHDL": CommentTokens(
        [SingleLineCommentToken("--")]),
    "OCaml": CommentTokens(
        multi=[MultiLineCommentTokens("(*", "*)")]),
    "Pascal": CommentTokens(
        [SingleLineCommentToken("//")],
        [MultiLineCommentTokens("{", "}"),
         MultiLineCommentTokens("(*", "*)")]),
    "Perl": CommentTokens(
        [SingleLineCommentToken("#")],
        [MultiLineCommentTokens("=", "\n=cut\n")]),
    "Raku": CommentTokens(
        [SingleLineCommentToken("#")],
        [MultiLineCommentTokens("=", "\n=cut\n"),
         MultiLineCommentTokens("#`{", "}"),
         MultiLineCommentTokens("#`(", ")")]),
    "PHP": CommentTokens(
        [SingleLineCommentToken("#"),
         SingleLineCommentToken("//")],
        [MultiLineCommentTokens("/*", "*/")]),
    "PowerShell": CommentTokens(
        [SingleLineCommentToken("#")],
        [MultiLineCommentTokens("<#", "#>")]),
    "Python": CommentTokens(
        [SingleLineCommentToken("#")],
        [MultiLineCommentTokens("\"\"\"", "\"\"\""),
         MultiLineCommentTokens("\'\'\'", "\'\'\'")]),
    "Ruby": CommentTokens(
        [SingleLineCommentToken("#")],
        [MultiLineCommentTokens("=begin", "=end")]),
    "Swift": CommentTokens(
        [SingleLineCommentToken("//")],
        [MultiLineCommentTokens("/*", "*/")]),
    "XML": CommentTokens(
        multi=[MultiLineCommentTokens("<!--", "-->")]),
    "CSS": CommentTokens(
        multi=[MultiLineCommentTokens("/*", "*/")]),
    "Shell script": CommentTokens(
        [SingleLineCommentToken("#")]),
    "R": CommentTokens(
        [SingleLineCommentToken("#")])
    }
