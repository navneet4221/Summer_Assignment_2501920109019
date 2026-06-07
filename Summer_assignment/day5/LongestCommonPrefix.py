class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        n = strs[0]      
        for s in strs[1:]:
            while not s.startswith(n):
                n = n[:-1]
                if not n:
                    return ""
        return n
