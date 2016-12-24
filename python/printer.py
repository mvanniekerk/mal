from lisptypes import *

def pr_str(mal):
    if isinstance(mal, list):
        return_str = ""
        for mal_sub in mal:
            return_str += " " + pr_str(mal_sub)
        return "(" + return_str[1:] + ")"
    if isinstance(mal, bool):
        if mal:
            return "true"
        else:
            return "false"
    if isinstance(mal, int):
        return str(mal)
    if isinstance(mal, str):
        return mal
    if isinstance(mal, Quote):
        return mal.toString()
    if isinstance(mal, QuasiQuote):
        return mal.toString()
    if isinstance(mal, UnQuote):
        return mal.toString()
    if isinstance(mal, SpliceUnquote):
        return mal.toString()
    if mal is None:
        return "nil"
