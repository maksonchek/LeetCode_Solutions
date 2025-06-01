class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        un = set()
        for e in emails:
            name, dom = e.split('@')
            name = name.split('+')[0].replace('.', '')
            un.add(f"{name}@{dom}")
        return len(un)