class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass

roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # Total value of the Roman numeral
        prev_value = 0  # Previous numeral value (initially 0)

        # Iterate over the string in reverse
        for char in reversed(s):
            curr_value = roman_map[char]  # Get the current numeral value

            # If the current value is less than the previous value, subtract it
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value  # Otherwise, add it to the total

            prev_value = curr_value  # Update previous value for next iteration
        
        return total

