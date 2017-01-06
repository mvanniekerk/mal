from lisptypes import *

def pr_str(mal):
    if isinstance(mal, Token):
        return str(mal)
    elif callable(mal):
        return '#<function>'
