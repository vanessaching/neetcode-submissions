class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all = {}
        for s in strs:
            key = "".join(sorted(s))
            all.setdefault(key, []).append(s)
        return list(all.values())