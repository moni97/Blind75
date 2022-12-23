    def isValid(self, s: str) -> bool:
      stack = []
      left = {')': '(', ']': '[', '}': '{'}
      for c in s:
          if c not in left:
              stack.append(c)
          elif len(stack) != 0 and left[c] == stack[-1]:
              stack.pop()
          else: return False
      print(stack)
      return True if len(stack) == 0 else False
