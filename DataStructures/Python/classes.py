# Methods may call other methods by using method attributes of the self argument:
# First argument to a method is self (OMITTED WHEN CALLING)

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

# Iterator
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

class Bag2:
    
    # self.dog = 11     Must create instance variables in __init__
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

a = [0,1]
b= a
b[0] = 9
print(a)
