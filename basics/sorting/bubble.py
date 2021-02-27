
from base import Sorting


class BubbleSort(Sorting):

    def sort(self, arr):
        arr_len = len(arr)

        last_sorted_index = arr_len

        # outer loop to run for every element of arr
        while last_sorted_index >= 0:
            # inner loop
            for j in range(1, last_sorted_index):
                if arr[j-1] > arr[j]:
                    self.swap(arr, j-1, j)
            # decrement last sorted index
            last_sorted_index -= 1

        return arr


if __name__ == '__main__':
    BubbleSort().test(10)
