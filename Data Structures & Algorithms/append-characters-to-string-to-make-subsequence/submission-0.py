class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        point = 0
        for i in s:
            if point < len(t) and i == t[point]:
                point+=1
        return len(t) - point
        