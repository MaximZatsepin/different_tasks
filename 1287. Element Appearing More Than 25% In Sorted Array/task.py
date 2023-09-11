'''
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
'''
def findSpecialInteger(arr: list[int]) -> int:
    counter = 1
    number = arr[0]
    #print(f'len: {len(arr)}')
    #print(f'len/4: {int(len(arr)/4)}')
    for i in range(len(arr)-1):
        counter = counter + 1 if arr[i] == arr[i+1] else 1
        number = arr[i]
        #print(f'index: {i}, counter: {counter}, number: {number}')
        if counter > int(len(arr)/4):
            return number
    return arr[0]


arr = [1,2,2,6,6,6,6,7,10]
print(findSpecialInteger(arr)) # -> 6
arr = [1,1]
print(findSpecialInteger(arr)) # -> 1
arr = [1,2,3,3]
print(findSpecialInteger(arr)) # -> 3