'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
# Solved after 0.5years-break
def twoSum(nums: list[int], target: int) -> list[int]:
    arr = {}
    for index,value in enumerate(nums):
        if target-value in arr:
            return index, arr[target-value]
        arr[value] = index
        print(arr)



nums = [2,11,7,15]
target = 9
print(twoSum(nums,target)) # -> [0,1]

