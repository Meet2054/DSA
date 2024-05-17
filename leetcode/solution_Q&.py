class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign of the number
        sign = -1 if x < 0 else 1
        
        # Convert the number to a string and reverse it
        x_str = str(abs(x))[::-1]
        
        # Convert the reversed string back to an integer
        reversed_int = sign * int(x_str)
        
        # Handle 32-bit integer overflow
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        
        return reversed_int

# Example of using the Solution class
if __name__ == "__main__":
    # Taking input from the user
    x = int(input("Enter an integer: "))
    
    # Creating an instance of the Solution class
    solution = Solution()
    
    # Calling the reverse method
    result = solution.reverse(x)
    
    # Printing the result
    print(f"Reversed integer: {result}")
