class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_sum = 0

        for i in range(0, len(accounts)):
            column_sum = 0
            for j in range(0, len(accounts[i])):
                column_sum = column_sum + accounts[i][j]
            if column_sum >= max_sum:
                max_sum = column_sum
                
        return max_sum