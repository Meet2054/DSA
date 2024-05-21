class Solution:
    def intToRoman(self, num: int) -> str:
        sysList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
                   ["XL", 40], ["L", 50], ["XC", 90], ["C", 100],
                   ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        
        res = ""
        for sys, val in reversed(sysList):
            if num // val:
                count = num // val
                res += sys * count
                num = num % val
        
        return res

# Example inputs and usage
solution = Solution()

# Test with various input values
inputs = [3, 58, 1994, 2023, 3999]
outputs = [solution.intToRoman(num) for num in inputs]

# Print the results
for num, roman in zip(inputs, outputs):
    print(f"The integer {num} converts to the Roman numeral {roman}")
