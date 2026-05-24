class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = { }

        for word in strs:
            key = []
            for i in range(26):
                key.append(0)

            for letter in word:
                key[ord(letter) - ord("a")] += 1

            tup = tuple(key)

            if result.get(tup):
                result[tup].append(word)
            else:
                result[tup] = [word]
            
        return list(result.values())
                
            
