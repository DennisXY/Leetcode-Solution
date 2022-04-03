# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target,
# find the smallest element in the list that is larger than the given target.
#
# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
#
# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 二分
        left = 0
        right = len(letters) # 左闭右开
        while left < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        if left >= len(letters):
            return letters[0]
        return letters[left]

