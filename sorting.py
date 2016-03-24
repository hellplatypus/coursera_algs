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
        for i in range(len(self.arr)):
            if self.arr[i] > self.arr[i+1]:
                return False
        return True


class ShellSort(SortBase):
    def sort(self):
        step = 1
        while step < len(self.arr):
            step = 3 * step + 1
        step /= 3


        print step

if __name__ == '__main__':
    print "Shell sort:"
    print "_________________________________________________________"
    shell = ShellSort(20)
    shell.print_arr()
    start_time = time.time()
    shell.sort()
    print "Sorting time: ", time.time() - start_time
    if shell.is_sorted():
        print "Array is sorted."
    else:
        print "Array is not sorted."
    print
