def numDecodings(self, s: str) -> int:
    cache = {len(s): 1}
    def dfs(i):
        if i in cache:
            return cache[i]
        # print(i, cache)
        if s[i] == "0":
            return 0
        res = dfs(i+1)
        if i+1 < len(s) and ([i] == '1' or s[i] == '2' or s[i+1] in '0123456'):
            res += dfs(i+2)
        cache[i] = res
        return res
    return dfs(0)
