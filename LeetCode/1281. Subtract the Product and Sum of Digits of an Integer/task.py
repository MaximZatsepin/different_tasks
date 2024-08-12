
def subtractProductAndSum(n: int) -> int:
    power =1 
    sum = 0
    for num in str(n):
        power *= int(num)
        sum += int(num)
    return power-sum


print(subtractProductAndSum(234)) # -> 15
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
print(subtractProductAndSum(4421)) # -> 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21