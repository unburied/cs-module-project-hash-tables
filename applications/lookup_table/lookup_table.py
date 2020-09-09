# Your code here
import random
import math

# empty dict to cache values
cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # key will be a tuple of arrgs
    key = (x,y)

    # add key, val to cache if not in table
    if key not in cache:
        cache[key] = slowfun_too_slow(x,y)
        return cache[key]
    else:
        return cache[key]    


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
