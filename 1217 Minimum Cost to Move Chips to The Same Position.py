class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddpos, evenpos = 0, 0
        
        for i in range(len(position)):
            if position[i] % 2 == 0:
                evenpos += 1
                position[i] = 2
            else:
                oddpos += 1
                position[i] = 1
                
        return evenpos if evenpos < oddpos else oddpos