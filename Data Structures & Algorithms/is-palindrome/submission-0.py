class Solution:
    def isPalindrome(self, s: str) -> bool:
        t =  ''.join(char for char in s if char.isalnum()).lower()
        for i in range(len(t)//2):
            if t[i] != t[len(t)-1-i]:
                return False
        return True

        