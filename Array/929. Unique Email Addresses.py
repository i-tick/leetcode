class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq = set()
        for i in emails:
            l,d = i.split('@')
            f = l.split('+')[0]
            f = f.replace('.','')
            print([f,l])
            uniq.add((f,d))
        return len(uniq)
        