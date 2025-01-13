class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        n = len(people)
        l = 0
        r = n-1

        while l<r:
            if people[r]+people[l]>limit:
                r-=1
                ans+=1

            elif people[r]+people[l]<=limit:
                ans+=1
                l+=1
                r-=1

        if l==r:
            ans+=1

        return ans