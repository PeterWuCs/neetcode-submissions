class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengtha = len(s)
        lengthb = len(t)

        if lengtha != lengthb:
            return False
        dict_a = { }
        dict_b = { }

        for i in range(lengtha):
            if not dict_a.get(s[i]):
                dict_a[s[i]] = 1
            else:
                dict_a[s[i]] += 1

            if not dict_b.get(t[i]):
                dict_b[t[i]] = 1
            else:
                dict_b[t[i]] += 1
        
        return dict_a == dict_b 


        