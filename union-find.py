class UnionFind:
    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.arr_size = [1] * n
        self.largest_el_list = self.arr[:]

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def _root(self, node):
        while self.arr[node] != node:
            # self.arr[node] = self.arr[self.arr[node]]
            node = self.arr[node]
        return node

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)

        if i == j:
            return

        if self.largest_el_list[i] > self.largest_el_list[j]:
            self.largest_el_list[j] = self.largest_el_list[i]
        else:
            self.largest_el_list[i] = self.largest_el_list[j]

        if self.arr_size[i] < self.arr_size[j]:
            self.arr[i] = j
            self.arr_size[j] += self.arr_size[i]
        else:
            self.arr[j] = i
            self.arr_size[i] += self.arr_size[j]

    def find(self, i):
        return self.largest_el_list[self._root(i)]


uf = UnionFind(10)

uf.union(0, 4)
uf.union(5, 4)
uf.union(5, 3)
uf.union(1, 2)
uf.union(1, 7)
uf.union(7, 4)

print uf.find(3)

print uf.arr
print uf.arr_size
