class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pass
bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Stack to keep track of opening brackets
        stack = []

        # Iterate over each character in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top of the stack if it's not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the current closing bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, it means all brackets were properly closed
        return not stack

    # Method to convert Roman numerals to an integer
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Map of Roman numerals and their corresponding values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate over the Roman numeral string from left to right
        for char in s:
            curr_value = roman_map[char]
            
            # If the previous value is smaller than the current, subtract twice the previous value
            # because it was added earlier and now needs to be subtracted
            if prev_value < curr_value:
                total += curr_value - 2 * prev_value
            else:
                total += curr_value
            
            # Update the previous value
            prev_value = curr_value
        
        return total






    



  

