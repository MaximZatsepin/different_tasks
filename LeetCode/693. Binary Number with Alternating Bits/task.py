'''
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
'''
def hasAlternatingBits(n: int):# -> bool:
    return '11' not in bin(n) and '00' not in bin(n)

# print(hasAlternatingBits(5)) # -> True
# print(hasAlternatingBits(7)) # -> False

for i in range(1000):
    if hasAlternatingBits(i):

        print(f'{i} is {bin(i)[2:]}, {hasAlternatingBits(i)}')


'''
0 + 0 + 1 = 1
1 + 1 = 2
2 + 2 + 1 = 5
5 + 5 = 10
10 + 10 + 1 = 21
21 + 21 = 42
42 + 42 + 1 = 85
85+85 = 170

'''