class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return 0
        
        i = 0
        l = len(needle)
        while i + l <= len(haystack):
            if haystack[i:i+l] == needle:
                return i
            i += 1

        return -1

def main():
    test_object = Solution()
    print(test_object.strStr("hello", "ll"))
    print(test_object.strStr("aaaaa", "bba"))
    print(test_object.strStr("", ""))

if __name__ == "__main__":
    main()