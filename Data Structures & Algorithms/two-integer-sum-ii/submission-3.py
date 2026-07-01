class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, val in enumerate(numbers[0:-1]):
            for i in range(idx+1, len(numbers)):
                if val == numbers[i]:
                    continue
                if val + numbers[i] == target:
                    return [idx+1, i+1]
