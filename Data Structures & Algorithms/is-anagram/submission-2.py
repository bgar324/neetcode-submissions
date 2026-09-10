class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0] * 26

        for i in s:
            index = ord(i) - ord('a')
            arr[index] += 1
        
        for j in t:
            index = ord(j) - ord('a')
            arr[index] -= 1
            # if at any point an instance is less than 0 than it isnt a anagram?
            if (arr[index] < 0):
                return False
        
        return True