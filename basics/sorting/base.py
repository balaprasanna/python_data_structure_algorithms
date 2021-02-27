import abc


class Sorting(object):

    @abc.abstractmethod
    def sort(self, arr):
        raise NotImplementedError()

    @staticmethod
    def swap(arr, i, j):
        """
        :param arr: list to be modified
        :param i:
        :param j:
        :return: None
        """
        arr[i], arr[j] = arr[j], arr[i]

    def test(self, size=(10000,)):
        import numpy as np
        inp = np.random.randint(0, 5000, size=size).tolist()
        expected = sorted(inp)
        actual = self.sort(inp)
        print("actual", actual)
        print("expected", expected)
        assert actual == expected
        print("Pass !!!")
