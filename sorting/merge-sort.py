"""
# https://www.geeksforgeeks.org/merge-sort/
"""

class MergeSort(object):

    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def merge_remainig(self, p_ptr, p_array, global_ptr):
        while p_ptr < len(p_array):
            self.array[global_ptr] = p_array[p_ptr]
            p_ptr += 1
            global_ptr += 1

    def merge(self, left, mid, right):
        left_array, right_array = [], []
        for index in range(left, mid + 1):
            left_array.append(self.array[index])
        for index in range(mid + 1, right + 1):
            right_array.append(self.array[index])
        left_ptr, right_ptr, global_ptr = 0, 0, left
        while left_ptr < len(left_array) and right_ptr < len(right_array):
            if left_array[left_ptr] <= right_array[right_ptr]:
                self.array[global_ptr] = left_array[left_ptr]
                left_ptr += 1
            else:
                self.array[global_ptr] = right_array[right_ptr]
                right_ptr += 1
            global_ptr += 1
        self.merge_remainig(left_ptr, left_array, global_ptr)
        self.merge_remainig(right_ptr, right_array, global_ptr)

    def merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)

    def print_array(self):
        print(self.array)


array = [10,10,-1,3,1,12,34,2,100]
sort_obj = MergeSort(array)
sort_obj.merge_sort(0, len(array) - 1)
sort_obj.print_array()