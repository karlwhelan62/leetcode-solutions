class Solution:

    def isPalindrom(self, x: int) -> bool:
        
        if x < 0:
            return False

        reverse_int = 0
        orignial_int = x

        while orignial_int != 0:
            reverse_int *= 10
            reverse_int += orignial_int % 10
            orignial_int = orignial_int // 10

        return x == reverse_int