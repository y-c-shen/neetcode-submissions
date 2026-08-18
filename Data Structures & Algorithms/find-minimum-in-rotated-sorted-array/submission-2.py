class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = (r+l)//2

        while l < r:
            
            if r - l <= 2:
                return min(nums[l], nums[r], nums[m])


            # [3,4,(5),6,1,2]
            # [3,4,5,6,(1),2]
            # [3,4,5,(6),1]
            elif nums[l] < nums[m]:
                if nums[m] < nums[r]:
                    # it is well sorted, return l
                    return nums[l]
                else: # m > r, so pivot is between m and r
                    l = m + 1
                    m = (r + l)//2

            # [4,5,(0),1,2,3]
            else: # l > m, so pivot is to the left
                # if m on the pivot, return m
                if nums[m-1] > nums[m]:
                    return nums[m]
                r = m - 1
                m = (r + l)//2
        return nums[m]



            