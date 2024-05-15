class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxlen = 0
        charset = set()
        l = 0
        for right in range(n):
            if s[right] not in charset:
                charset.add(s[right])
                maxlen = max(maxlen, right - l + 1)
            else:
                while s[right] in charset:
                    charset.remove(s[l])
                    l += 1
                charset.add(s[right])
        return maxlen

# Taking input from the user
s = input("Enter a string: ")

# Creating an instance of the Solution class
sol = Solution()

# Calling the lengthOfLongestSubstring function
result = sol.lengthOfLongestSubstring(s)

# Displaying the result
print("Length of the longest substring without repeating characters:", result)
