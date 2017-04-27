from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *


class OCLLexer(RegexLexer):
    name = 'OCL'
    aliases = ['ocl']
    filenames = ['*.ocl']
    mimetypes = ['text/x-ocl']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'(context|pre|post|init|inv)\b', Keyword),
            (r'\b(private|protected|public|static)\b', Keyword.Declaration),
            (r'\b(void|bool|char|floor|int)\b', Keyword.Type),
            (r'\b(true|false|null|self)\b', Keyword.Constant),
            (r"'[^']*'", String),
            (r"\"[^\"]*\"", String),
            (r'.', Text),
        ],
        'comment': [
            (r'[^*/]', Comment),
            (r'/\*', Comment, '#push'),
            (r'\*/', Comment, '#pop'),
            (r'[*/]', Comment)
        ],
    }
