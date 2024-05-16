class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)

        y_str = x_str[::-1]

        return x_str == y_str

# Test the function
sol = Solution()
input_number = 12321
print("Is", input_number, "a palindrome?", sol.isPalindrome(input_number))
