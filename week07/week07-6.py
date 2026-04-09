# week07-6.py
# Leetcode 649. Dota2 Senate
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        banR, banD = 0, 0  # 目前被消滅的次數，初始是 0
        R, D = senate.count('R'), senate.count('D')  # 目前各有幾個人

        while queue:
            now = queue.popleft()  # 左邊出佇列，代表該議員出場

            if now == 'R':
                if banR > 0:
                    banR -= 1  # 用掉 1 個消滅名額
                    R -= 1     # R 少 1 人
                else:
                    banD += 1
                    queue.append(now)  # 沒被消滅，回到隊尾
            else:  # now == 'D'
                if banD > 0:
                    banD -= 1
                    D -= 1
                else:
                    banR += 1
                    queue.append(now)

            if R == 0:
                return 'Dire'
            if D == 0:
                return 'Radiant'
