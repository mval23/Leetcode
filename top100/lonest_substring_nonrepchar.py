class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        sub = []
        for c in s:
            if c in sub:
                i = sub.index(c)
                sub = sub[sub.index(c) + 1 :]
            sub.append(c)
            if len(sub) > max:
                max = len(sub)
        return max


print(Solution().lengthOfLongestSubstring(""))

