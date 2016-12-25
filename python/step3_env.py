import sys
import reader
import printer
from lisptypes import *
from env import Env

repl_env = Env(None)
repl_env.set("+", lambda a,b: a+b)
repl_env.set("-", lambda a,b: a-b)
repl_env.set("*", lambda a,b: a*b)
repl_env.set("/", lambda a,b: int(a/b))


def eval_ast(ast, env):
    if isinstance(ast, Symbol):
        # TODO pretty error
        return env.get(ast.content)
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
            if ast.li[0].content == "def!":
                value = EVAL(ast.li[2], env)
                env.set(ast.li[1].content, value)
                return value
            elif ast.li[0].content == "let*":
                new_env = Env(env)
                env_list = ast.li[1].li
                for i in range(0, len(env_list), 2):
                    key = env_list[i].content
                    value = EVAL(env_list[i+1], new_env)
                    new_env.set(key, value)
                return EVAL(ast.li[2], new_env)
            else:
                new_list = eval_ast(ast, env)
                return new_list[0](*new_list[1:])
    else:
        return eval_ast(ast, env)

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
