class Solution:
    def isValid(self, s: str) -> bool:

        curr = ''

        if s == '':
            return True

        while s != curr:
            curr = s

            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')

            if s == '':
                return True
            
        return False