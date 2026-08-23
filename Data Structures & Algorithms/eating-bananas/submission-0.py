class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(piles, h, speed):
            total = 0
            for pile in piles:
                # get ceiling div
                total += (pile + speed - 1) // speed
            return total <= h

        l = 1
        r = max(piles)
        min_speed = r
        while l <= r:
            m = (r + l) // 2
            # speed is enough, try less
            if canEat(piles, h, m):
                r = m-1
                min_speed = m
            else: # too slow, try more
                l = m + 1
        return min_speed


  
