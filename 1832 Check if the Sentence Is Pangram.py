class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """

        if len(set(sentence)) == 26:
            return True
            
        return False