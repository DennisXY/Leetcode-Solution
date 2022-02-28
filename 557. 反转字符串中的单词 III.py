# Given a string, you need to reverse the order of characters in each word within a sentence
# still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be
# any extra space in the string.

class Solution:
    def reverseWords(self, s):
        length = len(s)
        result = ''
        temp = ''
        for i in range(length):
            if s[i] == ' ':
                for j in range(len(temp)-1, -1, -1):
                    result = result+temp[j]
                result += ' '
                temp = ''
            else:
                temp = temp + s[i]

        for j in range(len(temp) - 1, -1, -1):
            result = result + temp[j]
        return result


if __name__ == '__main__':
    a = "Let's take LeetCode contest"
    solution = Solution()
    c = solution.reverseWords(a)
    print(c)