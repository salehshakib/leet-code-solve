from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)

        intervals = quicksort(intervals)
        
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if merged[-1][0] <= interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)

        return merged

# Example usage
intervals = [[1,3], [2,6], [8,10], [15,18]]
s = Solution()
print(s.merge(intervals))
