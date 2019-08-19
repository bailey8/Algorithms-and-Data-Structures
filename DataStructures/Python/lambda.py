# https://realpython.com/python-lambda/

def identity(x):
    return x

lambda x: x

# In the example above, the expression is composed of:

# The keyword: lambda
# A bound variable: x
# A body: x
# Note: In the context of this article, a bound variable is an argument to a lambda function.

# How to execute
(lambda x: x + 1)(2)

#Name Function
add_one = lambda x: x + 1
# Call later
add_one(2)

def add_oneSTD(x):
    return x + 1

#Multiple arguments
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'

# IIFE (Immediatley involked Function Expresison)
(lambda x, y: x + y)(2, 3)

# Use as higher order functions
high_ord_func = lambda x, func: x + func(x)
# Notice how the higher order function is a lambda itself
high_ord_func(2, lambda x: x * x)


dic = {}
print(True if dic.get("hi") else False)