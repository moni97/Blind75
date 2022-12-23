def minWindow(self, s: str, t: str) -> str:
  if t == "": return ""

  count, window = {}, {}
  for val in t:
      count[val] = 1 + count.get(val, 0)

  have, need = 0, len(t) 

  l = 0
  res, resLen = [-1, -1], float("infinity")
  for r in range(len(s)):
      c = s[r]
      window[c] = 1 + window.get(c, 0)

      if c in count and window[c] == count[c]:
          have += 1

      while have == need:
          if r - l + 1 < resLen:
              res = [l, r]
              resLen = r - l + 1
          window[s[l]] -= 1
          if s[l] in count and window[s[l]] < count[s[l]]:
              have -= 1
          l += 1
  return s[res[0]:res[1] + 1] if resLen != float("infinity") else  ""
