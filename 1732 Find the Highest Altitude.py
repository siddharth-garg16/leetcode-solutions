class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        #extra auxilary space required---------------------------------
        # altitudes = [0]
        # max_alt = -sys.maxint-1
        # point_gain = 0
        
        # for i in range(0, len(gain)):
        #     point_gain = point_gain + gain[i]
        #     altitudes.append(point_gain)
        
        # for i in range(0, len(altitudes)):
        #     if altitudes[i]>max_alt:
        #         max_alt = altitudes[i]
                
        # return max_alt

        #no extra auxilary space required-------------------------------
        highest_alt = max(0, gain[0])
        temp = gain[0]
        for i in range(1, len(gain)):
            temp += gain[i]
            highest_alt = max(temp, highest_alt)
            
        return highest_alt