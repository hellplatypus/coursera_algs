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


class QuickSort(SortBase):

    def sort(self):
        low = 0
        high = len(self.arr) - 1
        self.quick_sort(low, high)

    def quick_sort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quick_sort(low, pivot_index - 1)
            self.quick_sort(pivot_index + 1, high)

    @abstractmethod
    def partition(self, low, high):
        pass


class QuickSortWiki(QuickSort):

    def partition(self, low, high):
        pivot = self.arr[high]
        left_index = low
        for right_index in range(low, high):
            if self.arr[right_index] < pivot:
                self._swap(left_index, right_index)
                left_index += 1
        self._swap(left_index, high)
        return left_index


class QuickSortClassic(QuickSort):

    def partition(self, start, end):
        pivot = self.arr[end]
        bottom = start - 1
        top = end

        done = 0
        while not done:
            while not done:
                bottom += 1
                if bottom == top:
                    done = 1
                    break
                if self.arr[bottom] > pivot:
                    self.arr[top] = self.arr[bottom]
                    break

            while not done:
                top -= 1
                if top == bottom:
                    done = 1
                    break
                if self.arr[top] < pivot:
                    self.arr[bottom] = self.arr[top]
                    break
        self.arr[top] = pivot
        return top


class QuickSortOneLine(SortBase):

    def sort(self):
        self.qsort(self.arr)

    def qsort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            return self.qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + self.qsort([x for x in arr[1:] if x >= arr[0]])

if __name__ == '__main__':

    ARRAY_SIZE = 10000

    sort_class_list = [
                        ShellSort,
                        MergeSort,
                        QuickSortWiki,
                        QuickSortClassic,
                        QuickSortOneLine
                      ]
    for sort_class in sort_class_list:
        sort_instance = sort_class(ARRAY_SIZE)
        print sort_instance.__class__.__name__
        print "_________________________________________________________"
        # sort_instance.print_arr()
        start_time = time.time()
        sort_instance.sort()
        print "Sorting time: ", time.time() - start_time
        if sort_instance.is_sorted():
            print "Array is sorted."
        else:
            print "Array is not sorted."
        # sort_instance.print_arr()
        print


