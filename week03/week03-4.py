# week03-4.py
# Leetcode 1004. Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        N = len(nums)
        ans = 0
        tail = 0
        for head in range(N):
            if nums[head] == 0:
                zeros += 1
                #if zeros > k:
                while zeros > k:
                    if nums[tail] == 0:
                        zeros -= 1
                    tail += 1
            ans = max(ans, head - tail+1)
        return ans
