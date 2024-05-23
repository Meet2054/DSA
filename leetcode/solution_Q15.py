from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        
        for i in range(len(nums) - 2):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            firstNum = nums[i]
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                secondNum = nums[j]
                thirdNum = nums[k]

                potentialSum = firstNum + secondNum + thirdNum 
                
                if potentialSum > 0:
                    k -= 1
                elif potentialSum < 0:
                    j += 1
                else:
                    triplets.add((firstNum, secondNum, thirdNum))
                    j += 1
                    k -= 1
                    # Skip duplicate elements for the second number
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # Skip duplicate elements for the third number
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return [list(triplet) for triplet in triplets]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    example_input = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(example_input)
    print(result)  # Expected output: [[-1, -1, 2], [-1, 0, 1]]
