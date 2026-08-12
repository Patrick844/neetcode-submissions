class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterMap_s = {}
        letterMap_t = {}
        for char in s:
            if char in letterMap_s:
                letterMap_s[char]+=1
            else:
                letterMap_s[char] = 1
        
        for char in t:
            if char in letterMap_t:
                letterMap_t[char]+=1
            else:
                letterMap_t[char] = 1
        
        if letterMap_t == letterMap_s:
            return True
        else:
             return False