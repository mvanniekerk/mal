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
    else:
        return read_atom(reader)

def read_list(reader):
    reader.next()
    tokens = []
    while True:
        try:
            token = reader.peek()
        except IndexError:
            print("Expected ')', got EOF")
            return
        if token == ")":
            reader.next()
            return tokens
        else:
            tokens.append(read_form(reader))

def read_atom(reader):
    token = reader.next()
    if isint(token):
        return int(token)
    elif token == "'":
        return [Quote(), read_form(reader)]
    elif token == "`":
        return [QuasiQuote(), read_form(reader)]
    elif token == "~":
        return [UnQuote(), read_form(reader)]
    elif token == "~@":
        return [SpliceUnquote(), read_form(reader)]
    elif token == "true":
        return True
    elif token == "false":
        return False
    elif token == "nil":
        return None
    else:
        return token

def isint(int_string):
    try:
        int(int_string)
        return True
    except ValueError:
        return False
