class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a_sum = sum(aliceSizes)
        b_sum = sum(bobSizes)
        diff = (a_sum - b_sum)//2
        
        a_hash = set(aliceSizes)
        
        for number in bobSizes:
            if number+diff in a_hash:
                return [number+diff, number]