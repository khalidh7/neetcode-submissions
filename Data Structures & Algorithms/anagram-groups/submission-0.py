class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}

        for word in strs:
            temp1 = self.getset(word)
            if temp1 in sets:
                sets[temp1].append(word)
            else:
                sets[temp1] = [word]

        return list(sets.values())

    def getset(self, word):
        temp = {}

        for letter in word:
            if letter in temp:
                temp[letter] +=1
            else:
                temp[letter] = 1

        return frozenset(temp.items())