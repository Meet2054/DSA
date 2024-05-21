#Brute force
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res =0 
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area = (j-i)*min(height[i],height[j])
                res = max(res,area)
        
        return res
    
'''

# Two pointer approach
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res =0 
        l=0
        r=len(height)-1
        while(l<r):
            area = (r-l)* min(height[l],height[r])
            res = max(res,area)
            if height[l]>height[r]:
                r-=1
            elif height[l]<height[r]:
                l+=1
            else:
                l+=1
            
        return res

 #Example input
height = [1,8,6,2,5,4,8,3,7]

# Create an instance of the Solution class
solution = Solution()

# Call the maxArea method with the example input
max_water_area = solution.maxArea(height)

# Print the output
print("The maximum area of water the container can hold is:", max_water_area)

        