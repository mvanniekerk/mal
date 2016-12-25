class Env:
    def __init__(self, outer):
        self.outer = outer
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def find(self, key):
        if key in self.data:
            return self
        elif self.outer is not None:
            return self.outer.find(key)
        # TODO raise error

    def get(self, key):
        return self.find(key).data[key]

