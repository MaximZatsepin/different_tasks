
def runningSum(nums: list[int]) -> list[int]:
    for i in range(1,len(nums)): nums[i] += nums[i-1]
    return nums



nums = [1,2,3,4]
print(runningSum(nums)) # -> [1,3,6,10]
nums = [1,1,1,1,1]
print(runningSum(nums)) # -> [1,2,3,4,5]