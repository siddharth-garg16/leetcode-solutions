class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, 10 ** 9
        while low <= high:
            k = (low + high) // 2
            if sum(math.ceil(pile / k) for pile in piles) > h:
                low = k + 1
            else:
                high = k - 1

        return low