class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grps={}

        for ch in strs:
            sortedch = ''.join(sorted(ch))

            if sortedch not in grps:
                grps[sortedch]=[]

            grps[sortedch].append(ch)

        return list(grps.values())


        