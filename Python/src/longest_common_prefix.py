from typing import List

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        # get length of shortest string, max possible prefix size
        i = len(min(strs, key=len))
        # reduce i until all substrings to index i for items in the list match
        # if i reaches 0 no prefix is found, return empty string
        while i > 0:
            if all(strs[0][:i] == x[:i] for x in strs):
                return strs[0][:i]
            i -= 1

        return ""
