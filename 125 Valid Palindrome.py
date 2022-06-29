class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        new_str = ""

        for i in range(len(s)):
            if (ord(s[i]) > 96 and ord(s[i]) < 123) or (ord(s[i]) > 47 and ord(s[i]) < 58):
                new_str += s[i]

        rev_str = new_str[::-1]

        return new_str == rev_str