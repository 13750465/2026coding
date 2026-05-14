# week12-1b.py ¾Ç²ß­pµe
# 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def helper(now):
            for k in rooms[now]:
                if k not in visited:
                    visited.add(k)
                    helper(k)
        visited.add(0)
        helper(0)
        return len(rooms) == len(visited)
