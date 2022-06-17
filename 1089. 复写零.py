# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining
# elements to the right.
#
# Note that elements beyond the length of the original array are not written. Do the above modifications
# to the input array in place and do not return anything.
#
# Example 1:
#
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        stop, left, length = 0, 0, len(arr)
        while left < length:
            if arr[stop] == 0:
                left += 2
            else:
                left += 1
            stop += 1
        stop -= 1
        right = length-1
        if left > length:
            arr[right] = 0
            stop -= 1
            right -= 1
        for i in range(stop, -1, -1):
            arr[right] = arr[i]
            if arr[i] == 0:
                arr[right-1] = arr[i]
                right -= 1
            right -= 1