import string
class Solution(object):
    def isPalindrome(self, s):
        a=""
        for i in s:
            if i not in string.punctuation and i!=" " and i!=":":
                a+=i.lower()
        if a==a[::-1]:
            return True
        else:
            return False
