from env import Env

class Token:
    def __init__(self, content):
        self.content = content

    def EVAL(self, env):
        return self.eval_ast(env)

    def eval_ast(self, env):
        return self

    def __bool__(self):
        return True

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

class LinkedList(list, Token):
    def __init__(self, *args, **kwargs):
        super(LinkedList, self).__init__(*args, **kwargs)
        self.content = self

    def EVAL(self, env):
        if len(self) == 0:
            return self
        else:
            if self[0].content == "def!":
                value = self[2].EVAL(env)
                env.set(self[1].content, value)
                return value
            elif self[0].content == "let*":
                new_env = Env(env)
                env_list = self[1]
                for i in range(0, len(env_list), 2):
                    key = env_list[i].content
                    value = env_list[i+1].EVAL(new_env)
                    new_env.set(key, value)
                return self[2].EVAL(new_env)
            elif self[0].content == "do":
                ev = [ast.EVAL(env) for ast in self[1:]]
                return ev[-1]
            elif self[0].content == "if":
                cond = self[1].EVAL(env)
                if cond:
                    return self[2].EVAL(env)
                else:
                    if len(self) > 3:
                        return self[3].EVAL(env)
                    else:
                        return Nil()
            elif self[0].content == "fn*":
                def function(*args):
                    new_env = Env(env, [s.content for s in self[1]], args)
                    return self[2].EVAL(new_env)
                return function
            else:
                new_list = self.eval_ast(env)
                return new_list[0](*new_list[1:])

    def __eq__(self, other):
        if isinstance(other, LinkedList) or isinstance(other, Vector):
            return super().__eq__(other)

    def eval_ast(self, env):
        return [t.EVAL(env) for t in self]

    def __str__(self):
        return_str = ""
        for el in self:
            return_str += " " + str(el)
        return "(" + return_str[1:] + ")"

class Vector(list, Token):
    def eval_ast(self, env):
        return Vector([t.EVAL(env) for t in self])

    def __eq__(self, other):
        if isinstance(other, Vector) or isinstance(other, LinkedList):
            return super().__eq__(other)

    def __str__(self):
        return_str = ""
        for el in self:
            return_str += " " + str(el)
        return "[" + return_str[1:] + "]"

class HashMap(dict, Token):
    def __init__(self, li):
        if isinstance(li, list):
            di = {li[i]:li[i+1] for i in range(0,len(li),2)}
        elif isinstance(li, dict):
            di = li
        super().__init__(di)

    def eval_ast(self, env):
        return HashMap({k : v.EVAL(env) for k, v in self.items()})

    def __str__(self):
        returnstr = ""
        for k, v in self.items():
            returnstr += " " + str(k) + " " + str(v)
        return "{" + returnstr[1:] + "}"

class String(Token):
    # TODO remove the need for this class
    def __init__(self, quote_string):
        self.content = quote_string[1:-1]

    def __eq__(self, other):
        if isinstance(other, String):
            return self.content == other.content

    def __hash__(self):
        return hash(self.content)

    def __str__(self):
        return '"' + self.content + '"'

class Keyword(Token):
    def __eq__(self, other):
        if isinstance(other, Keyword):
            return self.content == other.content

    def __hash__(self):
        return hash(self.content)

class Integer(int, Token):
    # TODO remove the need for this class
    def __add__(self, i):
        return Integer(super().__add__(i))

    def __sub__(self, i):
        return Integer(super().__sub__(i))

    def __mul__(self, i):
        return Integer(super().__mul__(i))

    def __bool__(self):
        return True

    def __floordiv__(self, i):
        return Integer(super().__floordiv__(i))

class Boolean(Token):
    def __bool__(self):
        return self.content

    def __str__(self):
        if self.content:
            return "true"
        else:
            return "false"

class Nil(Token):
    def __init__(self):
        pass

    def __bool__(self):
        return False

    def __eq__(self, other):
        return isinstance(other, Nil)

    def __len__(self):
        return 0

    def __str__(self):
        return "nil"
