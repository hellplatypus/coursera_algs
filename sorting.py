import random
import time
from abc import abstractmethod, ABCMeta


class SortBase:
    __metaclass__ = ABCMeta

    def __init__(self, array_size):
        self.arr = random.sample(xrange(10*array_size), array_size)

    def print_arr(self):
        print self.arr

    @abstractmethod
    def sort(self):
        pass

    def is_sorted(self):
        for i in range(len(self.arr)-1):
            if self.arr[i] > self.arr[i+1]:
                return False
        return True

    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


class ShellSort(SortBase):

    def sort(self):
        step = 1
        while step < len(self.arr):
            step = 3 * step + 1
        step /= 3

        while step >= 1:
            self._select_sort(step)
            step /= 3

    def _select_sort(self, step):
        for i in range(step):
            j = i
            arr_len = len(self.arr)
            while j + step < arr_len:
                k = j
                j += step
                while k >= 0:
                    if self.arr[j] <= self.arr[k]:
                        self._swap(k, j)
                        k -= step
                        j -= step
                    else:
                        break


class MergeSort(SortBase):

    def sort(self):
        low_border = 0
        high_border = len(self.arr) - 1
        self.arr = self._sort(low_border, high_border)

    def _sort(self, low_border, high_border):
        left_list = []
        right_list = []
        middle = low_border + (high_border - low_border) / 2
        if low_border != middle:
            left_list = self._sort(low_border, middle)
        if middle + 1 != high_border:
            right_list = self._sort(middle + 1, high_border)
        if low_border == middle and middle + 1 == high_border:
            return self._merge(self.arr[low_border:middle+1], self.arr[middle+1:high_border+1])
        return self._merge(left_list, right_list)

    @staticmethod
    def _merge(left_list, right_list):

        result_arr = []
        left_list_index = 0
        right_list_index = 0

        while left_list_index != len(left_list) and right_list_index != len(right_list):
            if left_list[left_list_index] < right_list[right_list_index]:
                result_arr.append(left_list[left_list_index])
                left_list_index += 1
            else:
                result_arr.append(right_list[right_list_index])
                right_list_index += 1

        if left_list_index == len(left_list):
            result_arr.extend(right_list[right_list_index:])

        if right_list_index == len(right_list):
            result_arr.extend(left_list[left_list_index:])

        return result_arr


if __name__ == '__main__':

    sort_class_list = [
                        ShellSort,
                        MergeSort
                      ]
    for sort_class in sort_class_list:
        sort_instance = sort_class(11000)
        print sort_instance.__class__.__name__
        print "_________________________________________________________"
        sort_instance.print_arr()
        start_time = time.time()
        sort_instance.sort()
        print "Sorting time: ", time.time() - start_time
        if sort_instance.is_sorted():
            print "Array is sorted."
        else:
            print "Array is not sorted."
        sort_instance.print_arr()
        print


