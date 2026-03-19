# week04-4b.py (­«¼g week04-3.py)
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = [0] * 200
        for nn in nums:
            H[nn] += 1
        for nn in nums:
            if nn % 2 == 0 and H[nn] == 1:
                return nn
        return -1
