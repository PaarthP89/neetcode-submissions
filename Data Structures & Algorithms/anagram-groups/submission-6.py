class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            map[key].append(word)
        print(map.values())
        return list(map.values())