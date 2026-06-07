class Solution:
    def isPalindrome(self, s):
        filtered = [character.lower() for character in s if character.isalnum()]
        return filtered == list(reversed(filtered))
