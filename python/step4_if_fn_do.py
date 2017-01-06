import sys
import traceback
import reader
import printer
from lisptypes import *
from env import Env
from core import ns

repl_env = Env(None)
for k, v in ns.items():
    repl_env.set(k, v)


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
        except NameError as e:
            print(e)

if __name__ == "__main__":
    EVAL(READ("(def! not (fn* (a) (if a false true)))"), repl_env)
    mainloop()
