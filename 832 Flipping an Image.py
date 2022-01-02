class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for img in image:
            img[:]=img[::-1]
            for j in range(0, len(img)):
                img[j]^=1
                    
        return image