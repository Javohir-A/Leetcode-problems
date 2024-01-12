#%%problem 14 SOLVED
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key= lambda x : len(x))
        min_el = strs[0]
        if len(min_el) == 0:
            return ""
        while len(min_el) > 0:
            check = min_el
            for i in range(1, len(strs)):
                if min_el != strs[i][:len(min_el)]:
                    min_el = min_el[:len(min_el)-1]
                if len(min_el) == 0:
                    return ""
            if check == min_el: 
                return min_el
