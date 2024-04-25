class Solution(object):
    def isValid(self, s):
        """
    
      stack = []
      mapping = {')': '(', ']': '[', '}': '{'}
      for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
            else:
                return False
        return not stack
        :type s: str
        :rtype: bool
        """
        pass
    



  

