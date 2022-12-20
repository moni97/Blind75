def encode(self, strs):
        # write your code here
        return "".join(f'{len(string)}#{string}' for string in strs)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        index = 0
        len_str = len(str)
        result = []
        while index < len_str:
            j = index
            while str[j] != '#':
                j += 1
            length = int(str[index:j])
            moveIndex = j + 1
            result.append(str[moveIndex:moveIndex+length])
            index = moveIndex + length
        return result
