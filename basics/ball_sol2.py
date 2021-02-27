from math import factorial

class Solution:

    @staticmethod
    def find_c(n, r):
        if n >= r >= 0:
            return factorial(n) / (factorial(r) * factorial(n - r))
        else:
            return 0

    def solve(self, distance, obstacles, bounds):
        mid = distance/2

        # solution for placing 1 obstacle
        # mid at +mid, and -mid pos
        count = 0
        if mid == bounds:
            avail_slots_for_obs = bounds
            val = self.find_c(n=avail_slots_for_obs, r=obstacles - 1)
            count += val*2 # to mirror for other side
        if mid > bounds:
            avail_slots_for_obs = abs(bounds - mid)
            val = self.find_c(n=avail_slots_for_obs, r=obstacles - 1)
            count += val * 2
        elif mid < bounds:
            avail_slots_for_obs = abs(bounds-mid)
            val = self.find_c(n=avail_slots_for_obs, r= obstacles-1 )
            count += val*2
            # for the mirror effect - use right comb values to derive for left comb

        # solution for placing 2 obstacle
        if mid == bounds:
            avail_slots_for_obs = bounds-1
            val = self.find_c(n=avail_slots_for_obs, r=obstacles - 2)
            count += val*2  # to mirror for other side
        if mid > bounds:
            avail_slots_for_obs = abs(bounds - mid)
            val = self.find_c(n=avail_slots_for_obs, r=obstacles - 2)
            count += val * 2
        elif mid < bounds:
            avail_slots_for_obs = abs(bounds - mid)
            val = self.find_c(n=avail_slots_for_obs, r=obstacles - 2)
            count += val*2
            # for the mirror effect - use right comb values to derive for left comb

        # solution for placing >2 obstacle
        return count


if __name__ == '__main__':
    distance = 6
    obstacles = 4
    bounds = 4

    s = Solution()
    res = s.solve(distance, obstacles, bounds)
    print(res)
