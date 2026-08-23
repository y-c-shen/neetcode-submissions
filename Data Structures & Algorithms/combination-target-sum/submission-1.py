class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        """
        [2,5,6,9]

        [2], [5], [6], [9]
        [2,2], [2,5], [2,6] | [9] yes
        [2,2,2], [2,2,5] yes
        [2,2,2,2]

        
        """
        
        def dfs(i):
            total = sum(subset)
            if total > target:
                return
            elif total == target:
                res.append(subset.copy())
            
            # now total < target
            for k in range(i, len(nums)):
                if total + nums[k] <= target:
                    subset.append(nums[k])
                    dfs(k)
                    subset.pop()

        dfs(0)
        return res
