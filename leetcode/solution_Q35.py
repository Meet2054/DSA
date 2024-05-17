from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__ == "__main__":
    # Taking input from the user
    nums = list(map(int, input("Enter a sorted list of integers (separated by spaces): ").split()))
    target = int(input("Enter the target integer: "))
    
    # Creating an instance of the Solution class
    solution = Solution()
    
    # Calling the searchInsert method and printing the result
    result = solution.searchInsert(nums, target)
    print(f"The target should be inserted at index: {result}")
