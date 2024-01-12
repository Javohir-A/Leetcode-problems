# %% problem 5 SOLVED
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lst_palin = []
        max_palin = s[0]
        for i in range(len(s)):
            lst_palin.append(s[i])
            palin = s[i]
            for j in range(i+1, len(s)):
                palin+=s[j]
                if palin[::-1] == palin:
                    lst_palin.append(palin) 
                    if len(max_palin) < len(palin):
                        max_palin = palin
        return max_palin
