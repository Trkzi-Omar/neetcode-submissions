class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - y = x
        # nums[j] = diff = target - nums[i]
        # j = nums.index(diff)
        # nums=[3,2,3]
        # target=6

        if len(nums)<=2: 
            if nums[0] == nums[1]: return [0,1]
            return []
        for n in nums:
            n_idx=nums.index(n)
            nums[n_idx]=math.inf
            if (target-n) in nums: 
                return sorted([n_idx, nums.index(target-n)])
            nums[n_idx]=n
        return []
        