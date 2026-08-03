class Solution(object):
    def isPalindrome(self, x):
        xn=str(x)
        if xn==xn[::-1]:
            return True
        else:
            return False
        