
# class Solution(object):
#    def fourSumCount(self, A, B, C, D):
#       sums ={}
#       for i in A:
#          for j in B:
#             if i+j not in sums:
#                sums[i+j] = 1
#             else:
#                sums[i+j] +=1
#       counter = 0
#       for i in C:
#          for j in D:
#             if -1 * (i+j) in sums:
#                #print(-1 * (i+j))
#                counter+=sums[-1*(i+j)]
#       return counter

class Solution:

    def find_solution(self, A, B, C, D, target):
        sums = {}
        # possibles = {}
        for i in A:
            for j in B:
                if i+j not in sums:
                    sums[i+j] = 1
                    # possibles[i+j] = [[i, j]]
                else:
                    sums[i+j] += 1
                    # possibles[i+j] = [i,j]
        count = 0
        for m in C:
            for n in D:
                key = target - (m+n)
                if key in sums:
                    # possibles[key].append([m,n])
                    count += sums[key]
        # print(possibles)
        return count


if __name__ == '__main__':
    s = Solution()
    target = 109
    import numpy as np
    r = s.find_solution(
        np.random.randint(0, 109, (103,)),
        np.random.randint(0, 109, (103,)),
        np.random.randint(0, 109, (103,)),
        np.random.randint(0, 109, (103,)),
        target)
    print(r)