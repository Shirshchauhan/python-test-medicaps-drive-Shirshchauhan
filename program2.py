class Solution(object):
    def romanToInt(self, s):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        
        for char in s:
            curr_value = roman_values[char]
            if curr_value > prev_value:
                total += curr_value - 2 * prev_value
            else:
                total += curr_value
            prev_value = curr_value
        return total
   
solution = Solution()

# Input value "III"
output_1 = solution.romanToInt("III")
print("Output 1:", output_1)  # Output: 3

# Input value "LVIII"
output_2 = solution.romanToInt("LVIII")
print("Output 2:", output_2)  # Output: 58

# Input value "MCMXCIV"
output_3 = solution.romanToInt("MCMXCIV")
print("Output 3:", output_3)  # Output: 1994