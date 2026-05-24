class TimeMap:

    def __init__(self):
        self.arry = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.arry:
            self.arry[key] = [(timestamp, value), ]
        else:
            self.arry[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.arry:
            return ""
        low = 0
        high = len(self.arry[key]) - 1
        
        res = ""
        while low <= high:
            mid = (low + high) // 2

            time = self.arry[key][mid][0]

            if  time == timestamp:
                return self.arry[key][mid][1]
            elif time < timestamp:
                res = self.arry[key][mid][1]
                low = mid + 1
            else:
                high = mid - 1
        return res
