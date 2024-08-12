'''
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
'''
def calPoints( operations: list[str]) -> int:
    arr = []
    for i in ops:
        match i:
            case 'C':
                del arr[-1]
            case 'D':
                arr.append(arr[-1]*2)
            case '+':
                arr.append(arr[-1]+arr[-2])
            case _:
                arr.append(int(i))
    return sum(arr)

ops = ["5","2","C","D","+"]
print(calPoints(ops)) # -> 30

