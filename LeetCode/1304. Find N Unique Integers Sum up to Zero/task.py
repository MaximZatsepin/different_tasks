'''
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
'''
def sumZero(n: int) -> list[int]:
    arr = []
    arr.append(0) if n % 2 != 0 else arr
    for i in range(1,n,2):
        arr.append(i)
        arr.append(-i)
    return arr

n = 7
print(sumZero(n))