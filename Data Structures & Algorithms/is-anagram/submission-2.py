class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        # both the len of the string will be same 
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            first[s[i]] = first.get(s[i],0)+1
            first[t[i]] = first.get(t[i],0)-1


        # for ch in s:
        #     first[ch] = first.get(ch,0)+1

        # for ch2 in t:
        #     first[ch2] = first.get(ch2,0)-1

        return all(v == 0  for v in first.values())




        