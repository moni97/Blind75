from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test = defaultdict()
        for c in s:
            if c in test:
                test[c] += 1
            else:
                test[c] = 1
        for c in t:
            if c not in test:
                return False
            test[c] -= 1
            if test[c] < 0:
                return False
        return True
