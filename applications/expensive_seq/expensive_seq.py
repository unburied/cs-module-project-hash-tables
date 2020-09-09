# Your code here


def expensive_seq(x, y, z, cache = {}):
    # set key as a tuple
    key = (x,y,z)

    # check if in dict
    if key in cache:
        return cache[key]

    # base case
    if x <= 0:
        return y + z
    else:
        #find val for this tuple
        val = (
            expensive_seq(x-1,y+1,z, cache) +
            expensive_seq(x-2,y+2,z*2, cache) + 
            expensive_seq(x-3,y+3,z*3, cache)
        )

        # store this val in dict
        cache[key] = val

        # send val upstream
        return val

    


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
