"""
https://leetcode.com/problems/time-based-key-value-store/
"""

from collections import OrderedDict

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeMap = OrderedDict()
        

    def check_and_get_value(self, key, input_timestamp):
        all_timestamps = self.timeMap[key]['timestamps']
        all_values = self.timeMap[key]['values']
        left, right = 0, len(all_timestamps) - 1
        while left <= right:
            if all_timestamps[left] > input_timestamp:
                return ''
            mid = (left + right) // 2
            if all_timestamps[mid] == input_timestamp:
                return all_values[mid]
            if input_timestamp < all_timestamps[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return all_values[right]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key]['timestamps'] = self.timeMap[key].get('timestamps', list()) + [timestamp]
            self.timeMap[key]['values'] = self.timeMap[key].get('values', list()) + [value]            
        else:
            self.timeMap[key] = dict()
            self.timeMap[key]['timestamps'] = [timestamp]
            self.timeMap[key]['values'] = [value]            

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            return self.check_and_get_value(key, timestamp)
        return ""


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))
print(obj.get("foo", 3))
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))
print(obj.get("foo", 5))
