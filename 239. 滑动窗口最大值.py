# You are given an array of integers nums,
# there is a sliding window of size k which is moving from
# the very left of the array to the very right.
# You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.

# 官方题解第二个解法
# https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/

import collections


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        q = collections.deque()
        # 当滑动窗口向右移动时，只要i还在窗口中，那么j一定也还在窗口中，
        # 这是 i 在 j 的左侧所保证的。因此，由于 nums[j] 的存在，
        # nums[i] 一定不会是滑动窗口中的最大值了，我们可以将 \nums[i] 永久地移除。
        # 当滑动窗口向右移动时，我们需要把一个新的元素放入队列中。为了保持队列的性质，
        # 我们会不断地将新的元素与队尾的元素相比较，如果前者大于等于后者，
        # 那么队尾的元素就可以被永久地移除，我们将其弹出队列。
        # 我们需要不断地进行此项操作，直到队列为空或者新的元素小于队尾的元素。


        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        # 由于队列中下标对应的元素是严格单调递减的，
        # 因此此时队首下标对应的元素就是滑动窗口中的最大值。但与方法一中相同的是，
        # 此时的最大值可能在滑动窗口左边界的左侧，并且随着窗口向右移动，
        # 它永远不可能出现在滑动窗口中了。因此我们还需要不断从队首弹出元素，
        # 直到队首元素在窗口中为止。

            while q[0] <= i-k:
                q.popleft()
            ans.append(nums[q[0]])
        return ans