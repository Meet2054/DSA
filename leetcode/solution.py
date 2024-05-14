from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Taking input from the user
nums = list(map(int, input("Enter the list of numbers separated by space: ").split()))
target = int(input("Enter the target sum: "))

# Creating an instance of Solution class
solution = Solution()

# Calling twoSum method
result = solution.twoSum(nums, target)

# Displaying the result
if result:
    print("Indices of the two numbers whose sum equals the target:", result)
else:
    print("No such pair found.")
