class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        length = len(strs)
        if length == 0:
            return ''
        prefix = strs[0]
        for i in range(len(prefix)):
            for j in range(1, length):
                next_str = strs[j]
                if len(next_str) <= i or next_str[i] != prefix[i]:
                    new_prefix = prefix[:i]
                    return new_prefix
        return prefix