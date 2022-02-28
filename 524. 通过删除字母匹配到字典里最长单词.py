# Given a string and a string dictionary, find the longest string in the dictionary that can
# be formed by deleting some characters of the given string.
# If there are more than one possible results, return the longest word with the
# smallest lexicographical order. If there is no possible result, return the empty string.

# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # 用好python内置函数sort()、find(),比双指针效率更高
        # 可以用元组表示多关键字排序，第一关键字是长度降序，第二关键字是字符串本身字典序
        d.sort(key = lambda x: (-len(x), x))

        for word in d:
            index = 0
            for ch in word:
                index = s.find(ch, index) + 1  # find输出-1:False
                if not index:
                    break
            else:       # 这里用else语句保证break之后不会执行，正常循环结束会执行
                return word
        return ''


if __name__ == '__main__':
    #s = "abpcplea"
    #s = "aaa"
    #d = ["aaa","aa","a"]
    s = "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq"
    #d = ["ale", "monkey","abpcple", "plea"]
    #d = ["a", "b", "c"]
    #d = ["ba","ab","a","b"]
    d = [ "ettphsiunoglotjlccurlre","ntgcykxhdfescxxypyew"]
    solution = Solution()
    c = solution.findLongestWord(s, d)
    print(c)