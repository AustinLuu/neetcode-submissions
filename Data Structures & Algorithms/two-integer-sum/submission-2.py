class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        unique_list = list(set(nums))
        for i in range(len(unique_list)):
            t_val = target - unique_list[i]
            if t_val in unique_list:
                if t_val == unique_list[i]:
                    idx = [j for j, x in enumerate(nums) if x == t_val]
                    if len(idx) == 1:
                        continue
                    else:
                        return [idx[0], idx[1]]
                else:
                    res = sorted([nums.index(unique_list[i]), nums.index(t_val)])
                    return res