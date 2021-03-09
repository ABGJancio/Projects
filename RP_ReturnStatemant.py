"""Best practices: using Return statement."""


def template_func(args):
    """Templete to begin every def with."""
    result = 0  # Initialize the return value
    # Your code goes here...
    return result  # Explicitly return the result


def variance(data, ddof=0):
    """Calculate the variance of a sample of numeric data."""
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - ddof)

#variance([3, 4, 7, 5, 6, 2, 9, 4, 1, 3])


def variance(data, ddof=0):
    """Calculate the variance in several steps.
       Avoid using complex expressions."""
    n = len(data)
    mean = sum(data) / n
    total_square_dev = sum((x - mean) ** 2 for x in data)
    return total_square_dev / (n - ddof)


profit = 0


def sell(sample):
    #global profit
    profit = sum(sample)
    return profit

#sell([3, 4, 5])

# print(profit)


def my_abs(number):
    """Use return With Conditionals."""
    if number < 0:
        return -number
    return number


def both_true(a, b):
    """An explicit if statement."""
    if a and b:
        return True
    return False


def both_true(a, b):
    """A conditional expression or ternary operator."""
    return True if a and b else False


def both_true(a, b):
    """Use built-in function bool()."""
    return bool(a and b)


def my_any(iterable):
    """Implement a short-circuit evaluation."""
    for item in iterable:
        if item:
            # Short-circuit
            return True
    return False


def dead_code():
    """Example of dead code."""
    return 42
    # Dead code
    print("Hello, World")


def no_dead_code(condition):
    """Whether True or False."""
    if condition:
        return 42
    print("Hello, World")


import statistics as st
from collections import namedtuple

def describe(sample):
    Desc = namedtuple("Desc", ["mean", "median", "mode"])
    return Desc(
        st.mean(sample),
        st.median(sample),
        st.mode(sample),
    )

sample = [10, 2, 4, 7, 9, 3, 9, 8, 6, 7]
stat_desc = describe(sample)
# Get the mean by its attribute name
print(stat_desc.mean)
# Get the median by its index
print(stat_desc[1])
# Unpack the values into three variables
mean, median, mode = describe(sample)
print(mean)
print(mode)


def by_factor(factor, number):
    return factor * number


def by_factor(factor):
    """uses a closure to retain the value of factor between calls."""
    def multiply(number):
        return factor * number
    return multiply

double = by_factor(2)
print(double(3)) # 2*3 = 6
print(double(9)) # 2*9 = 18

triple = by_factor(3)
print(triple(3)) # 3*3 = 9
print(triple(9)) # 3*9 = 27

def by_factor(factor):
    """Use of a lambda function make closure factory more concise."""
    return lambda number: factor * number

double = by_factor(2)
print(double(3)) # 2*3 = 6
print(double(9)) # 2*9 = 18

import time
 
def my_timer(func):
    """Idea of the execution time of a given Python function."""
    def _timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return _timer

@my_timer # Is equivalent to the expression delayed_mean = my_timer(delayed_mean).
          # In this case, you can say that my_timer() is decorating delayed_mean().
def delayed_mean(sample):
    """A decorator function takes a function object as an argument and returns a function object.
    Decorator adds extra logic to existing functions without modifying them.
    For example, you can code a decorator to log function calls, 
    validate the arguments to a function, 
    measure the execution time of a given function, and so on."""
    time.sleep(1)
    return sum(sample) / len(sample)

delayed_mean([10, 2, 4, 7, 9, 3, 9, 8, 6, 7])
# when you call delayed_mean(), you’re really calling the return value of my_timer(),
# which is the function object _timer. 
# The call to the decorated delayed_mean() will return the mean of the sample
# and will also measure the execution time of the original delayed_mean().
# Execution time: 1.0011096000671387
# 6.5


class Circle:
    def __init__(self, radius):
        self.radius = radius
    # Class implementation...


class Square:
    def __init__(self, side):
        self.side = side
    # Class implementation...


# Once you have a class for each shape, you can write a function that 
# takes the name of the shape as a string and an optional list of arguments (*args) 
# and keyword arguments (**kwargs) to create and initialize shapes on the fly:
def shape_factory(shape_name, *args, **kwargs):
    """Return User-Defined Objects: The Factory Pattern."""
    shapes = {"circle": Circle, "square": Square}
    return shapes[shape_name](*args, **kwargs)


# This function creates an instance of the concrete shape and returns it to the caller. 
# Now you can use shape_factory() to create objects of different shapes in response to the needs of your users:

# If you call shape_factory() with the name of the required shape as a string, 
# then you get a new instance of the shape that matches the shape_name you’ve just passed to the factory.

circle = shape_factory("circle", radius=20)
print(type(circle))
# <class '__main__.Circle'>
print(circle.radius)
# 20

square = shape_factory("square", side=10)
print(type(square))
# <class '__main__.Square'>
print(square.side)
# 10


def func(value):
    """Use 'return' in 'try … finally' blocks."""
    try:
        return float(value)
    except ValueError:
        return str(value)
    finally:
        print("Run this before returning")

print(func(9))
# Run this before returning
# 9.0

print(func("one"))
# Run this before returning
# 'one'


def gen():
    """Use 'return' in Generator Functions."""
    yield 1
    yield 2
    return 3

g = gen()
print(g)
# <generator object gen at 0x7f4ff4853c10>

print(next(g))
# 1
print(next(g))
# 2

# You can use a return statement inside a generator function to indicate that the generator is done. 
# The return statement will make the generator raise a StopIteration. 
# The return value will be passed as an argument to the initializer of StopIteration 
# and will be assigned to its .value attribute.

print(next(g))
# Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#    next(g)
# StopIteration: 3




