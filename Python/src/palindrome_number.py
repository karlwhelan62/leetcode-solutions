class Solution:

    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        reverse_int = 0
        orignial_int = x

        while x != 0:
            reverse_int = reverse_int * 10 + x % 10
            x = x // 10

        return orignial_int == reverse_int
