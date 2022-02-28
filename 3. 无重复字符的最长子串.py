class Solution:
    def lengthOfLongestSubstring(self, s):
        occ = set()
        length = len(s)
        max_length = 0
        start, end = 0, 0
        while end < length:
            if s[end] not in occ:
                occ.add(s[end])
                end += 1
            else:

                while s[end] in occ:
                    occ.remove(s[start])
                    start += 1
            max_length = max(max_length, len(occ))
        return max_length


if __name__ == '__main__':
    a = input("Please input the list: ")
    a = str(a)
    solution = Solution()
    b = solution.lengthOfLongestSubstring(a)
    print(b)