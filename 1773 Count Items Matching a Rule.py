class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        #-------------method 1-----------
        # matched_items = 0
        
        # if ruleKey == "type":
        #     j=0
        # elif ruleKey == "color":
        #     j=1
        # else:
        #     j=2
        
        # for i in range(0, len(items)):
        #     if items[i][j] == ruleValue:
        #         matched_items += 1
                
        # return matched_items

        #method 2
        keys = {"type":0, "color":1, "name":2}
        
        return sum(1 for item in items if item[keys[ruleKey]]==ruleValue)