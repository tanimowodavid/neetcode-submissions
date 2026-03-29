class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for a, b in zip(s, s[1:]):
            score += abs(ord(a) - ord(b))
        return score
        