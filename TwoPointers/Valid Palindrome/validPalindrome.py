    def isPalindrome(self, s: str) -> bool:
        converted_s = ''.join(c for c in s.lower() if c.isalnum())
        length_s = len(converted_s)
        if length_s == 0 or length_s == 1:
            return True
        loopEnd = length_s // 2 - 1
        i = 0
        # print(loopEnd)
        while (i <= loopEnd):
            # print(i, length_s - 1 - i)
            if (converted_s[i] != converted_s[length_s - 1 - i]):
                return False
            i += 1
        return True
