import lisptypes

class Env:
    def __init__(self, outer=None, binds=[], exprs=[]):
        self.outer = outer
        self.data = {}
        for i in range(0, len(binds)):
            if binds[i] == "&":
                self.data[binds[i+1]] = lisptypes.LinkedList(exprs[i:])
                break
            self.data[binds[i]] = exprs[i]

    def set(self, key, value):
        self.data[key] = value

    def find(self, key):
        if key in self.data:
            return self
        elif self.outer is not None:
            return self.outer.find(key)
        # TODO raise error
        raise NameError("NameError: " + key + " does not exist in the namespace")

    def get(self, key):
        return self.find(key).data[key]

