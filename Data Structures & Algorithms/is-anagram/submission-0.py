class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}

        for ch in s:
            first[ch] = first.get(ch,0)+1

        for ch2 in t:
            first[ch2] = first.get(ch2,0)-1

        return all(v == 0  for v in first.values())




        