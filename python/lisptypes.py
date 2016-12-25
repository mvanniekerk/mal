from env import Env

class Token:
    def __init__(self, content):
        self.content = content

    def EVAL(self, env):
        return self.eval_ast(env)

    def eval_ast(self, env):
        return self

    def __str__(self):
        return self.content

class Symbol(Token):
    def eval_ast(self, env):
        return env.get(self.content)

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

    def EVAL(self, env):
        if self.li == []:
            return self
        else:
            if self.li[0].content == "def!":
                value = self.li[2].EVAL(env)
                env.set(self.li[1].content, value)
                return value
            elif self.li[0].content == "let*":
                new_env = Env(env)
                env_list = self.li[1].li
                for i in range(0, len(env_list), 2):
                    key = env_list[i].content
                    value = env_list[i+1].EVAL(new_env)
                    new_env.set(key, value)
                return self.li[2].EVAL(new_env)
            else:
                new_list = self.eval_ast(env)
                return new_list[0](*new_list[1:])

    def eval_ast(self, env):
        return [t.EVAL(env) for t in self.li]

    def __str__(self):
        return_str = ""
        for el in self.li:
            return_str += " " + str(el)
        return "(" + return_str[1:] + ")"

class Vector(Token):
    def __init__(self, li):
        self.li = li

    def eval_ast(self, env):
        return Vector([t.EVAL(env) for t in self.li])

    def __str__(self):
        return_str = ""
        for el in self.li:
            return_str += " " + str(el)
        return "[" + return_str[1:] + "]"

class HashMap(Token):
    def __init__(self, li):
        if isinstance(li, list):
            self.di = {li[i]:li[i+1] for i in range(0,len(li),2)}
        elif isinstance(li, dict):
            self.di = li

    def eval_ast(self, env):
        return HashMap({k : v.EVAL(env) for k, v in self.di.items()})

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

class Integer(Token):
    def __init__(self, content):
        self.content = int(content)

    def __add__(self, i):
        return Integer(self.content + i.content)

    def __sub__(self, i):
        return Integer(self.content - i.content)

    def __mul__(self, i):
        return Integer(self.content * i.content)

    def __floordiv__(self, i):
        return Integer(self.content / i.content)

    def __str__(self):
        return str(self.content)

class Nil(Token):
    def __init__(self):
        pass

    def __str__(self):
        return "nil"
