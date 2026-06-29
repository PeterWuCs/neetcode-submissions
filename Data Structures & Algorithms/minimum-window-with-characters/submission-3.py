class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_count = defaultdict(int)
        for letter in t:
            t_count[letter] += 1
        dis = len(t_count)

        s_count = defaultdict(int)
        match = 0
        
        left = 0
        right = 0

        res = [-1, -1]

        while right < len(s):
            while match != dis and right < len(s):
                    if s[right] in t_count:
                        s_count[s[right]] += 1
                        if s_count[s[right]] == t_count[s[right]]:
                            match += 1
                    right += 1

            if match != dis:
                break

            while left < len(s) - 1 and (s[left] not in t_count or s_count[s[left]] - 1 >= t_count[s[left]]):
                if s[left] in t_count:
                    s_count[s[left]] -= 1
                left += 1
            

            if (res == [-1, -1] or res[1] - res[0] > right - left):
                res = [left, right]

            s_count[s[left]] -= 1
            match -= 1
            left += 1


        if res == [-1, -1]:
            return ""

        return s[res[0]: res[1]]


