from typing import List

startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        for i,j in (startTime,endTime):
            if (1 <= startTime[i] <= endTime[i]