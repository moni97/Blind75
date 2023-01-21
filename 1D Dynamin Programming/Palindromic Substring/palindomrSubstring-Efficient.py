class Solution:
    def isPalindrome(self, l, r, s):
        res= 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            r += 1
            l -= 1
            res += 1
        return res
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(0, len(s)):
            res += self.isPalindrome(i, i, s)
            res += self.isPalindrome(i, i+1, s)
        return res
