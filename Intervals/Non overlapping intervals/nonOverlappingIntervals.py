def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0])
        new = [intervals[0]]
        res = 0
        i = 1
        while i < len(intervals):
            if new[-1][1] > intervals[i][0]:
                new[-1][1] = min(new[-1][1], intervals[i][1])
                res+=1
            else:
                new.append(intervals[i])
            i+=1
        return res
