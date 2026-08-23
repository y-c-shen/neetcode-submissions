class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # strategy: 
        # sort the array, then use two sum II, two pointer strategy

        res = []

        nums.sort()

        # [-2, -2, 0, 1, 1, 1]
        # [-10, 3, 3, 7]

        prev = None
        for i in range(len(nums)-2):
            # if our first nbr is the same as prev, skip it (no dupes)
            if prev == nums[i]:
                continue
            else:
                # initialize pointers
                l = i+1
                r = len(nums) - 1

                # iterate until l = r
                while l < r:
                    s = nums[l] + nums[r]
                    if s == (-nums[i]):
                        res.append([nums[i], nums[l], nums[r]])
                        # move pointers
                        l_num = nums[l]
                        r_num = nums[r]
                        while l<r and nums[l] == l_num:
                            l += 1
                        while l<r and nums[r] == r_num:
                            r -= 1
                    elif s < (-nums[i]):
                        l += 1
                    else:
                        r -= 1

                # set prev for next iteration
                prev = nums[i]
            
        return res




            