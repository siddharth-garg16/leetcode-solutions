class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i in range(len(intervals)):
            intervals[i].append(i)

        intervals.sort()
        ret = [-1] * len(intervals)

        for i in range(len(intervals)):
            _, target_end, old_idx = intervals[i]
            left, right = i, len(intervals)
            while left < right:
                mid = left + (right - left) // 2
                if intervals[mid][0] < target_end:
                    left = mid + 1
                else:
                    right = mid

            if left < len(intervals) and intervals[left][0] >= target_end:
                ret[old_idx] = intervals[left][2]

        return ret