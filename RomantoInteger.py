class Solution:
    def romanToInt(self, s:str):
        # List the 13 unique symbols containing length-1 and length-2.
        map = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        i = total = 0
        # We add up each value of given Roman numbers.
        # From left to right, we firstly check if it's a length-2 symbol,
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in map:
                total += map[s[i: i + 2]]
                i += 2
        # else we treat it as length-1 symbol.
            else:
                total += map[s[i: i + 1]]
                i += 1
        return total

sol = Solution()
n = sol.romanToInt('MIV')
print(n)