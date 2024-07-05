from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __str__(self):
        return f"[{self.start}, {self.end}]"

def merge_intervals_solA(intervals: List[Interval]) -> List[Interval]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x.start)
    merged_intervals = [intervals[0]]

    for curr_interval in intervals[1:]:
        if curr_interval.start > merged_intervals[-1].end:
            merged_intervals.append(curr_interval)
        else:
            merged_intervals[-1].end = max(merged_intervals[-1].end, curr_interval.end)

    return merged_intervals

intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
print("Original intervals:", [str(interval) for interval in intervals])


def merge_intervals_solB(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for interval in intervals[1:]:
        last_interval = merged[-1]
        if interval[0] <= last_interval[1]:
            last_interval[1] = max(last_interval[1], interval[1])
        else:
            merged.append(interval)
    return merged

intervals_solB = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged_solA = merge_intervals_solA(intervals)
print("Merged intervals:", [str(interval) for interval in merged_solA])
merged_solB = merge_intervals_solB(intervals_solB) # Output: [Interval(1, 6), Interval(8, 10), Interval(15, 18)]
print("Merged intervals using solution B:", merged_solB)