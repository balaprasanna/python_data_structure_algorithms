
from base import Sorting


class SelectSort(Sorting):

    def sort(self, arr):
        arr_len = len(arr)

        # loop to run from 0 ... N
        for i in range(arr_len):
            curr_min = arr[i]
            curr_min_pos = i
            has_min = False
            for j in range(i, arr_len):
                if arr[j] < curr_min:
                    curr_min = arr[j]
                    curr_min_pos = j
                    has_min = True
            # at the end , swap the i'th with the min element from (i+1, N)
            if has_min:
                self.swap(arr, i, curr_min_pos)

        return arr


if __name__ == '__main__':
    SelectSort().test(10)
