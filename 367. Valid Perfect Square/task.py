'''

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

'''

def isPerfectSquare(num: int) -> bool:
    # print(f'num**0.5 {num**0.5}')
    # print(f'num {num}')
    # print(f'num**0.5 ^ 2 {num**0.5 * num**0.5}')
    return ((int(num**0.5)*int(num**0.5)) == (num))
    

print("Test case 14:")
print(isPerfectSquare(14))

print("Test case 4:")
print(isPerfectSquare(4))

print("Test case 9:")
print(isPerfectSquare(9))
