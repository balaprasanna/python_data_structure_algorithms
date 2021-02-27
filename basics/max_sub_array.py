def find_max_sub_array(arr):
    n = len(arr)
    final = 0
    i, j, z = 0, 0, 0
    while i < n:
        j = i
        while j < n:
            z = i
            s = 0
            while z < j:
                s += arr[z]
                z += 1
            final = max(final, s)
            j += 1
        i += 1
    print(final)
    return final


def find_max_sub_array_v2(arr):
    p, s = 0, 0
    for i in range(len(arr)):
        s = max(arr[i], s+arr[i])
        p = max(p, s)
    print(p)

if __name__ == '__main__':
    arr = [-1, 2, 4, -3, 5, 2, -5, 2]
    find_max_sub_array_v2(arr)

