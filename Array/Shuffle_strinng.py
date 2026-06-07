class Solution:
    def restoreString(self, s, indices):

        result = [""] * len(s)

        for i in range(len(s)):
            result[indices[i]] = s[i]

        return "".join(result)


s = "abc"
indices = [2, 1, 0]

obj = Solution()

print(obj.restoreString(s, indices))