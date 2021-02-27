
import math

class Solution:

    def sovle(self, timeframes, instance_cnt):
        total = len(timeframes)
        JUMP_THRESHOLD = 11  # sec
        i = 0
        UTIL_THRESHOLD_LBOUND = 25
        UTIL_THRESHOLD_UBOUND = 60
        while i < total:
            print("@at", i, timeframes[i])
            if timeframes[i] < UTIL_THRESHOLD_LBOUND and instance_cnt > 1:
                instance_cnt = math.ceil(instance_cnt / 2.0)
                print("SCALED DOWN")
                i = i+JUMP_THRESHOLD
            elif timeframes[i] > UTIL_THRESHOLD_UBOUND and instance_cnt*2 <= 2*(10**8):
                instance_cnt = math.ceil(instance_cnt * 2)
                print("SCALE UP")
                i = i+JUMP_THRESHOLD
            else:
                i += 1
        return instance_cnt


if __name__ == '__main__':
    s = Solution()
    instance_count = 200000000
    r = s.sovle([100], instance_count)
    print(r)
