class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterMap = {}
        for char in s:
            if char in letterMap:
                letterMap[char]+=1
            else:
                letterMap[char] = 1
        
        for char in t:
            if char in letterMap:
                letterMap[char]+=1
            else:
                return False
        
        for k,v in letterMap.items():
            if v%2 == 1:
                return False
        return True