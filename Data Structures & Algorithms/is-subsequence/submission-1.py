
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        point = 0
        for i in t:
            if point < len(s) and i == s[point]:
                point += 1
        return point == len(s)

        