class MaxSizeList(object):
    def __init__(self, size):
        self.list = []
        self.size = size
    def push(self, val):
        if(len(self.list) == self.size):
            del self.list[0]
        self.list.append(val)
    def get_list(self):
        return self.list

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())


