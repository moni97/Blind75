class Solution(object):
    def isAnagram(self, s, t):
        from collections import Counter
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count_s = set(s)
        for i in count_s:
            if s.count(i) != t.count(i):
                return False
        return True
