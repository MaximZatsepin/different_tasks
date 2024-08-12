'''
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
'''

def findNumbers(nums: list[int]) -> int:
    return len([i for i in nums if len(str(i)) % 2 == 0])

nums = [12,345,2,6,7896]
print(findNumbers(nums)) # -> 2
nums = [555,901,482,1771]
print(findNumbers(nums)) # -> 1