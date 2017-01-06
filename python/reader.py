import re
from lisptypes import *

class Reader:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def next(self):
        token = self.peek()
        self.position += 1
        return token

    def peek(self):
        return self.tokens[self.position]

def read_str(inp):
    tokens = tokenizer(inp)
    reader = Reader(tokens)
    return read_form(reader)

def tokenizer(inp):
    re_string = r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)"""
    return re.findall(re_string, inp)

def read_form(reader):
    token = reader.peek()
    if token == "(":
        return read_list(reader)
    elif token == "[":
        return read_list(reader, "[")
    elif token == "{":
        return read_list(reader, "{")
    else:
        return read_atom(reader)

def read_list(reader, startswith="("):
    reader.next()
    tokens = []
    while True:
        token = reader.peek()
        if token == ")" and startswith == "(":
            reader.next()
            return LinkedList(tokens)
        elif token == "]" and startswith == "[":
            reader.next()
            return Vector(tokens)
        elif token == "}" and startswith == "{":
            reader.next()
            return HashMap(tokens)
        else:
            tokens.append(read_form(reader))

def read_atom(reader):
    token = reader.next()
    if isint(token):
        return Integer(token)
    elif token == "'":
        return Quote(read_form(reader))
    elif token == "`":
        return QuasiQuote(read_form(reader))
    elif token == "~":
        return UnQuote(read_form(reader))
    elif token == "~@":
        return SpliceUnquote(read_form(reader))
    elif token == "@":
        return Deref(read_form(reader))
    elif token[0] == '"' and token[-1] == '"':
        #TODO Better error handling
        return String(token)
    elif token[0] == ":":
        return Keyword(token)
    elif token == "true":
        return Boolean(True)
    elif token == "false":
        return Boolean(False)
    elif token == "nil":
        return Nil()
    else:
        return Symbol(token)

def isint(int_string):
    try:
        int(int_string)
        return True
    except ValueError:
        return False
