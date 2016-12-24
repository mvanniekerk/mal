class Token:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content

class Quote(Token):
    def __str__(self):
        return "(quote " + str(self.content) + ")"

class QuasiQuote(Token):
    def __str__(self):
        return "(quasiquote " + str(self.content) + ")"

class UnQuote(Token):
    def __str__(self):
        return "(unquote " + str(self.content) + ")"

class SpliceUnquote(Token):
    def __str__(self):
        return "(splice-unquote " + str(self.content) + ")"

class Deref(Token):
    def __str__(self):
        return "(deref " + str(self.content) + ")"

class LinkedList(Token):
    def __init__(self, li):
        self.li = li

    def __str__(self, open="(", close=")"):
        return_str = ""
        for el in self.li:
            return_str += " " + str(el)
        return open + return_str[1:] + close

class Vector(LinkedList):
    def __str__(self):
        return super().__str__(open="[", close="]")

class HashMap(Token):
    def __init__(self, li):
        self.di = {li[i]:li[i+1] for i in range(0,len(li),2)}

    def __str__(self):
        returnstr = ""
        for k, v in self.di.items():
            returnstr += " " + str(k) + " " + str(v)
        return "{" + returnstr[1:] + "}"

class String(Token):
    def __init__(self, quote_string):
        self.str = quote_string[1:-1]

    def __str__(self):
        return '"' + self.str + '"'

class Nil(Token):
    def __init__(self):
        pass

    def __str__(self):
        return "nil"
