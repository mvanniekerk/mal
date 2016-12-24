import sys

def READ(inp):
    return inp

def EVAL(inp):
    return inp

def PRINT(inp):
    return inp

def rep(inp):
    return READ(EVAL(PRINT(inp)))

while True:
    try:
        inp = input("user> ")
        print(rep(inp))
    except EOFError as e:
        print("\nbye!")
        sys.exit(0)
