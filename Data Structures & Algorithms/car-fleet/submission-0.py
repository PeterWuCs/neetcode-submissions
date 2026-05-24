class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_spd = []
        length = len(position)
        for i in range(length):
            pos_spd.append((position[i], speed[i]))
        
        pos_spd.sort(reverse=True)

        curr = pos_spd[0]
        print(curr)
        cur_time = (target - curr[0]) / curr[1]
        count = 1
        for i in range(1, length):
            time = (target - pos_spd[i][0]) / pos_spd[i][1]
            if time > cur_time:
                curr = pos_spd[i]
                cur_time = time
                count += 1

        return count
            