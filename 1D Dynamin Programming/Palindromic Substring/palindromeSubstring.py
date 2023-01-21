def countSubstrings(self, s: str) -> int:
      palindrome = []
      def dfs(l, r, palindrome):
          if r >= len(s):
              return
          if r == l:
              # print(r, l)
              palindrome.append(s[r])
          else:
              currStr = s[l:r+1]
              # print(currStr)
              if currStr == currStr[::-1]:
                  palindrome.append(currStr)
                  # isPalindrome = Tre
          r += 1
          dfs(l, r, palindrome)
          return

      for i in range(len(s)):
          dfs(i, i, palindrome)
      # print(palindrome)
      return len(palindrome)
