import sys
import reader
import printer

def READ(inp):
    return reader.read_str(inp)

def EVAL(inp):
    return inp

def PRINT(mal):
    return printer.pr_str(mal)

def rep(inp):
    return PRINT(EVAL(READ(inp)))

while True:
    try:
        inp = input("user> ")
        print(rep(inp))
    except EOFError as e:
        print("\nbye!")
        sys.exit(0)
