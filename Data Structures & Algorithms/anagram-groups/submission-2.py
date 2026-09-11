class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate through strs, getting the frequency of that word, then adding it onto the hash map if the frequency alr exist
        # if frequency does not exist, then create new frequency and add onto that word
        groups = {}

        for word in strs:
            freq = [0] * 26

            for char in word:
                freq[ord(char) - ord('a')] += 1
            
            key = tuple(freq)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())