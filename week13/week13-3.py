# week13-3.py
# 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #heapify(nums)
        #while nums:
        #   print(heappop(nums))

        heapify(nums)
        for i in range(len(nums)-k):
            ans = heappop(nums)
        return heappop(nums)
