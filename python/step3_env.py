import sys
import reader
import printer
from lisptypes import *

repl_env = {'+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)}

def eval_ast(ast, env):
    if isinstance(ast, Symbol):
        # TODO pretty error
        return env[ast.content]
    elif isinstance(ast, LinkedList):
        return [EVAL(t, env) for t in ast.li]
    elif isinstance(ast, Vector):
        return Vector([EVAL(t, env) for t in ast.li])
    elif isinstance(ast, HashMap):
        return HashMap({k : EVAL(v, env) for k, v in ast.di.items()})
    else:
        return ast


def READ(inp):
    return reader.read_str(inp)

def EVAL(ast, env):
    if isinstance(ast, LinkedList):
        if ast.li == []:
            return ast
        else:
            new_list = eval_ast(ast, env)
            return new_list[0](*new_list[1:])
    else:
        return eval_ast(ast, env)

def PRINT(mal):
    return printer.pr_str(mal)

def rep(inp):
    return PRINT(EVAL(READ(inp), repl_env))

while True:
    inp = input("user> ")
    try:
        print(rep(inp))
    except EOFError as e:
        print("\nbye!")
        sys.exit(0)
    except IndexError:
        print("expected ')', got EOF")
    except KeyError:
        print("Symbol not found")
