import sys
import reader
import printer

repl_env = {'+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)}

def READ(inp):
    return reader.read_str(inp)

def EVAL(inp, env):
    return inp

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
