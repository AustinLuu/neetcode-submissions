class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for i in nums:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 0
        out = []
        key = sorted(cnt, key=cnt.get)
        return key[-k:]
