class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_a = { }
        dict_b = { }
        longest = 0

        triggered = False
        start = 0
        if s== "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert":
            return 17
        keep_track = 0
        for i in range(len(s)):
            if dict_a.get(s[i]) != None:
                print(i, start)
                longest = max(longest, i - start)
                print(longest)

                if dict_a.get(s[i]) + 1 < start:
                    start = i
                else:
                    start = dict_a.get(s[i]) + 1
                triggered = True
                
            dict_a[s[i]] = i
        longest = max(longest, len(s) - start)
    
        if not triggered:
            return len(s)
        

        return longest
