
def mySqrt(x: int) -> int:
    n = 0
    while(n*n <= x):
        n+=1
    return n-1


print(mySqrt(4)) # -> 2
print(mySqrt(8)) # -> 2

# long-time solution