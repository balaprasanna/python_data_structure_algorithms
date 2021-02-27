
from base import Sorting


class InsertionSort(Sorting):

    def sort(self, arr):
        arr_len = len(arr)

        # for every pos from left to right
        for i in range(arr_len):
            curr_item_to_insert = arr[i]
            curr_item_to_insert_pos = i
            for j in range(i-1, -1, -1):
                if arr[j] > curr_item_to_insert:
                    self.swap(arr, j, curr_item_to_insert_pos)
                    curr_item_to_insert_pos -= 1
                    curr_item_to_insert = arr[curr_item_to_insert_pos]
                else:
                    break

        return arr


if __name__ == '__main__':
    InsertionSort().test(10)