# week05-4.py ¬Q¤Ñ2026-03-25¬D¾ÔÃD
# Leetcode problems 3546. Equal Sum Grid Partition I
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum( [sum(row) for row in grid] )
        #print(total)
        preSum = 0
        for row in grid:
            preSum += sum(row)
            if preSum == total - preSum:
                return True

        preSum = 0
        for col in zip(*grid):
            preSum += sum(col)
            if preSum == total - preSum:
                return True
        return False
