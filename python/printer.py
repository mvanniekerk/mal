from lisptypes import *

def pr_str(mal):
    if isinstance(mal, bool):
        if mal:
            return "true"
        else:
            return "false"
    if isinstance(mal, Token):
        return str(mal)
