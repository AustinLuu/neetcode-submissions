from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = []
        out = []
        bob = defaultdict(list)
        for i in strs:
            sorted_str.append("".join(sorted(i)))
        for idx, val in enumerate(sorted_str):
            bob[val].append(strs[idx])
        return list(bob.values())
