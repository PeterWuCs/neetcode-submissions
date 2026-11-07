class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0

        people.sort()


        l = 0
        r = len(people) - 1
        print(people)

        while l <= r:
            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            res += 1

        return res
        