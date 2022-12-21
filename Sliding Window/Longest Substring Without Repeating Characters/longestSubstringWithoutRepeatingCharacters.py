def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    maxlen = 0
    visited = set()
    for r in range(len(s)):
        while s[r] in visited:
            visited.remove(s[l])
            l += 1
        visited.add(s[r])
        maxlen = max(maxlen, r - l + 1)
    return maxlen
