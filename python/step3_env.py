import sys
import reader
import printer
from lisptypes import *
from env import Env

repl_env = Env(None)
repl_env.set("+", lambda a,b: a+b)
repl_env.set("-", lambda a,b: a-b)
repl_env.set("*", lambda a,b: a*b)
repl_env.set("/", lambda a,b: a//b)


def READ(inp):
    return reader.read_str(inp)

def EVAL(ast, env):
    return ast.EVAL(env)

def PRINT(mal):
    return printer.pr_str(mal)

def rep(inp):
    return PRINT(EVAL(READ(inp), repl_env))

def mainloop():
    while True:
        try:
            inp = input("user> ")
            print(rep(inp))
        except EOFError as e:
            print("\nbye!")
            sys.exit(0)
        except IndexError:
            print("expected ')', got EOF")
        except AttributeError:
            print("Symbol not found")

if __name__ == "__main__":
    mainloop()
