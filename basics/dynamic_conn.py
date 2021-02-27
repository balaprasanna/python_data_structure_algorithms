

class UF(object):
    def __init__(self, N):
        self.ids = [i for i in range(N)]

    def root(self, x, with_height=False):
        height = 0

        while x != self.ids[x]:
            x = self.ids[x]
            height += 1

        if with_height:
            return x, height
        else:
            return x

    def print_path_to_root(self, x):
        path = f"{x} ->"
        while x != self.ids[x]:
            x = self.ids[x]
            path += f"{x} ->"
        print(path)
        return x

    def union(self, u, v):
        u_root, u_height = self.root(u, with_height=True)
        v_root, v_height = self.root(v, with_height=True)
        # self.ids[u_root] = v_root
        if u_height < v_height:
            self.ids[u_root] = v_root
        else:
            self.ids[v_root] = u_root

    def is_connected(self, u, v):
        return self.root(u) == self.root(v)


if __name__ == '__main__':
    N = 20
    uf = UF(N)
    import numpy as np
    a = np.random.randint(0, N, N//2)
    b = np.random.randint(0, N, N // 2)
    print(a)
    print(b)
    for pair in zip(a, b):
        print(f"union({pair})")
        uf.union(*pair)

    print(2, 4, "connected: ", uf.is_connected(2, 4))
    for i in range(N):
        uf.print_path_to_root(i)