# Given an integer array of even length arr, return true if
# it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i]
# for every 0 <= i < len(arr) / 2, or false otherwise.
# Example 1:
#
# Input: arr = [3,1,3,6]
# Output: false
# 设arr的长度为n，题目本质上是问arr能否分成n/2对元素，每对元素中一个数是另一个数的两倍
# 设cnt[x]表示arr中x的个数。
# 对于arr中的0，它只能与0匹配。如果cnt[0]是奇数，那么必然无法满足题目要求。
# 去掉arr中的0。设x为arr中绝对值最小的元素，由于没有绝对值比x更小的数，
# 因此x只能与2x匹配。如果此时cnt[2x]<cnt[x]，那么会有部分x 无法找到它的另一半，
# 即无法满足题目要求；否则将所有x和cnt[x] 个2x 从arr中去掉，继续判断剩余元素是否满足题目要求。不断重复此操作，如果某个时刻 \textit{arr}arr 为空，则说明 \textit{arr}arr 可以满足题目要求。

from collections import *


class Solution:
    def canReorderDoubled(self, arr) -> bool:
        cnt = Counter(arr)
        if cnt[0] % 2:
            return False
        for x in sorted(cnt, key=abs):
            if cnt[2 * x] < cnt[x]:  # 无法找到足够的 2x 与 x 配对
                return False
            cnt[2 * x] -= cnt[x]
        return True
