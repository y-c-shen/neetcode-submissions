class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        d_new = sorted(d.items(), key=lambda item: item[1], reverse=True)
        i = 0
        for key, v in d_new:
            if i < k:
                res.append(key)
                i += 1
            else: return res


        return res