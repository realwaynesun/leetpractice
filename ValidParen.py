class Solution:
    def isValid(self, s:str):
        parentheses = ['()', '[]', '{}']
        open_paren = ['(', '[', '{']
        stack = []
        for char in s:
            if char in open_paren:
                stack.append(char)
            elif not stack or stack.pop() + char not in parentheses:
                return False
        return not stack