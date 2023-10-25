'''

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

'''

def isPerfectSquare(num: int) -> bool:
    # print(num**0.5)
    # print(num)
    # print(num**0.5 * num**0.5)
    return ((float(num**0.5)*float(num**0.5)) == (float(num)))
    


print(isPerfectSquare(14))
