class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        for i in range(len(position)):
            fleets.append((position[i],speed[i]))
        fleets.sort(reverse=True)

        times = []
        for pos, speed in fleets:
            time = (target - pos) / speed
            if not times:
                times.append(time)
            elif times[-1] < time:
                times.append(time)
        return len(times)



        