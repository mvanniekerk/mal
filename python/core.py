from lisptypes import *
from printer import pr_str

def prn(*args):
    print(args[0])
    return Nil()

def toString(*args):
    return String("".join([pr_str(arg) for arg in args]))


ns = {
        'str': toString,
        'list': lambda *args: LinkedList(args),
        'list?': lambda *args: Boolean(isinstance(args[0], LinkedList)),
        'empty?': lambda *args: Boolean(len(args[0]) == 0),
        'count': lambda *args: Integer(len(args[0])),
        '=': lambda *args: Boolean(args[0] == args[1]),
        '<': lambda *args: Boolean(args[0] < args[1]),
        '>': lambda *args: Boolean(args[0] > args[1]),
        '<=': lambda *args: Boolean(args[0] <= args[1]),
        '>=': lambda *args: Boolean(args[0] >= args[1]),
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a//b
      }
