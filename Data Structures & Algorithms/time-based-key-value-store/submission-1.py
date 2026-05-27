class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(value,timestamp)]
        else:
            self.map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        values = self.map.get(key)
        answer = ''
        left, right = 0, len(values) -1

        while left <= right:
            mid = left + (right - left) // 2

            value, time = values[mid]
            if time <= timestamp:
                answer = value
                left = mid + 1
            else:
                right = mid - 1
        return answer

