class Solution:

    def encode(self, strs: List[str]) -> str:
        # list to str
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
 
        return ans
    def decode(self, s: str) -> List[str]:
        # str to list
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1

            ans.append(s[j:j + length])
            i = j + length

        return ans