"""
Capital One Coding Challenge - Comment Counter
Python 3.7.4 - PEP 8
Author: Mathieu Godin
"""
import sys
import os.path


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

"""Dictionary that maps programming languages file
extensions to their respective programming languages
comment syntax family"""
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
    "cpp": "C",  # C++
    "cxx": "C",  # C++
    "c++": "C",  # C++
    "hh": "C",  # C++
    "hpp": "C",  # C++
    "hxx": "C",  # C++
    "h++": "C",  # C++
    "cs": "C",  # C#
    "m": "C",  # Objective-C
    "mm": "C",  # Objective-C
    "go": "C",  # Go
    "groovy": "C",  # Groovy
    "gvy": "C",  # Groovy
    "gy": "C",  # Groovy
    "gsh": "C",  # Groovy
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
    "ts": "JavaScript",  # TypeScript
    "jsx": "JavaScript",
    "tsx": "JavaScript",  # TypeScript
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
    "htm": "XML",  # HTML
    "html": "XML",  # HTML
    "xaml": "XML",  # XAML
    "yaml": "YAML",
    "css": "CSS"}

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
    "YAML": CommentTokens(
        [SingleLineCommentToken("#")]),
    "R": CommentTokens(
        [SingleLineCommentToken("#")])}

if len(sys.argv) < 2:
    exit(0)
file_name = sys.argv[1]
if (file_name.startswith(".")):
    exit(0)
file_name_dot_split = file_name.split(".")
if len(file_name_dot_split) < 2:
    exit(0)
file_extension = file_name_dot_split[1].lower()
if file_extension not in languages_extensions:
    exit(0)
language = languages_extensions[file_extension]
language_comment_tokens = languages_comment_tokens[language]
if not os.path.isfile(file_name):
    exit(0)
file_content = ""
with open(file_name, "r") as file:
    file_content = file.read()
file_content_line_splitted = file_content.split("\n")
num_lines = len(file_content_line_splitted)
num_todos = 0
num_comment_lines = 0
num_single_line_comments = 0
num_multi_line_comments_lines = 0
num_multi_line_comments = 0


first_token_i = -1
inside_block = False
inside_block_right = ""
found_block = False
found_line = False
cur_i = 0
for line_f in file_content_line_splitted:
    line = line_f
    found_block = False
    found_line = False
    first_token_i = -1
    cur_i = 0
    num_todos += line.count("TODO")
    if inside_block:
        num_comment_lines += 1
        num_multi_line_comments_lines += 1
        cur_i = line.find(inside_block_right)
        if cur_i != -1:
            inside_block = False
            line = line[cur_i + len(inside_block_right):]
    if not inside_block:
        for tok_obj in language_comment_tokens.single:
            cur_i = line.find(tok_obj.token)
            if cur_i != -1 and (first_token_i == -1 or cur_i < first_token_i):
                first_token_i = cur_i
                found_line = True
    if not inside_block:
        for tok_obj in language_comment_tokens.multi:
            cur_i = line.find(tok_obj.left_token)
            if cur_i != -1 and (first_token_i == -1 or cur_i < first_token_i):
                first_token_i = cur_i
                inside_block_right = tok_obj.right_token
                found_block = True
    if found_block:
        num_comment_lines += 1
        num_multi_line_comments += 1
        num_multi_line_comments_lines += 1
        inside_block = True
    elif found_line:
        num_comment_lines += 1
        num_single_line_comments += 1
    
'''inside_line = False
inside_block = False
break_loop = False
current_block_right = ""
for line in file_content_line_splitted:
    i = 0
    while i < len(line):
        i_check = i
        if inside_block:
            j = 0
            while j < len(current_block_right):
                if i < len(line) and
                line[i] == current_block_right[j]:
                    j += 1
                    i += 1
                else:
                    break
            else:
                num_comment_lines += 1
                num_multi_line_comments += 1
                num_multi_line_comments_lines += 1
                inside_block = False
                current_block_right = right
                i = i_check
                break
        else:
            for tok_obj in language_comment_tokens.single:
                token = tok_obj.token
                i = i_check
                j = 0
                while j < len(token):
                    if i < len(line) and
                    line[i] == token[j]:
                        j += 1
                        i += 1
                    else:
                        break
                else:
                    num_comment_lines += 1
                    num_single_line_comments += 1
                    inside_line = True
                    break
            for tok_obj in language_comment_tokens.multi:
                if inside_line:
                    break
                left = tok_obj.left_token
                right = tok_obj.right_token
                i = i_check
                j = 0
                while j < len(left):
                    if i < len(line) and
                    line[i] == left[j]:
                        j += 1
                        i += 1
                    else:
                        break
                else:
                    num_comment_lines += 1
                    num_multi_line_comments += 1
                    num_multi_line_comments_lines += 1
                    inside_block = True
                    break'''

print("\n")
print("Total # of lines: " + str(num_lines))
print("Total # of comment lines: " +
      str(num_comment_lines))
print("Total # of single line comments: " +
      str(num_single_line_comments))
print("Total # of comment lines within block comments: " +
      str(num_multi_line_comments_lines))
print("Total # of block line comments: " +
      str(num_multi_line_comments))
print("Total # of TODO’s: " + str(num_todos))
