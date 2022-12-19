def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dictionary = defaultdict(list)
    for j in strs:
        count = [0] * 26
        for i in j:
            count[ord(i) - ord('a')] += 1
        dictionary[tuple(count)].append(j)
    return dictionary.values()
