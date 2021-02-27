
class Solution:
    def arrangeCoins(self, n: int) -> int:
        acc = 0

        for i in range(0, n + 1):
            if i > (n - acc):
                return i - 1
            acc += i
        return n


if __name__ == '__main__':
    Solution().arrangeCoins(5)