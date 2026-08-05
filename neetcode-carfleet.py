class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_stack = []
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)
        for p, s in pairs:
            car_stack.append((target - p) / s)
            if len(car_stack) >= 2 and car_stack[-1] <= car_stack[-2]:
                car_stack.pop()
        return len(car_stack)