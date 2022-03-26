class Solution:
    def reachNumber(self, target: int) -> int:
        displacement, steps = 0, 0
        target = abs(target)

        while displacement < target:
            steps += 1
            displacement += steps

        while (displacement - target) % 2 == 1:
            steps += 1
            displacement += steps

        return steps