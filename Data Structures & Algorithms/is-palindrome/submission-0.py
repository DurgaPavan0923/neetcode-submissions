class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = 0
        y = len(s) - 1

        while x < y:
            if not s[x].isalnum():
                x += 1
            elif not s[y].isalnum():
                y -= 1
            elif s[x].lower() != s[y].lower():
                return False
            else:
                x += 1
                y -= 1

        return True