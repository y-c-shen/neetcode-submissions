class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # think of it as decision tree
        # left = include element
        # right = leave out
        res = []
        
        s = []

        def dfs(i):
            if i >= len(nums):
                res.append(s.copy())
                return
            
            # do not include index i, right branch
            # basically, this explores all possibilities WITHOUT index i
            dfs(i+1)
            # include index i, left branch
            # Explore all possibilities WITH i
            s.append(nums[i])
            dfs(i+1)
            # reset s
            s.pop()

        dfs(0)
        return res


            
            
            