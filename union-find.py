class UnionFind:
    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.set_size = [1] * n

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def _root(self, node):
        while self.arr[node] != node:
            self.arr[node] = self.arr[self.arr[node]]
            node = self.arr[node]
        return node

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)

        if i == j:
            return

        if self.set_size[i] < self.set_size[j]:
            self.arr[i] = j
            self.set_size[j] += self.set_size[i]
        else:
            self.arr[j] = i
            self.set_size[i] += self.set_size[j]


class UnionFindWithSpecificCanonicalElement(UnionFind):
    def __init__(self, n):
        UnionFind.__init__(self, n)
        self.largest_el_list = self.arr[:]

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)

        if i == j:
            return

        # processing the largest element in new merged set
        if self.largest_el_list[i] > self.largest_el_list[j]:
            self.largest_el_list[j] = self.largest_el_list[i]
        else:
            self.largest_el_list[i] = self.largest_el_list[j]

        if self.set_size[i] < self.set_size[j]:
            self.arr[i] = j
            self.set_size[j] += self.set_size[i]
        else:
            self.arr[j] = i
            self.set_size[i] += self.set_size[j]

    def find(self, i):
        return self.largest_el_list[self._root(i)]


class UnionFindWithTreeHeight(UnionFind):
    def __init__(self, n):
        UnionFind.__init__(self, n)
        self.subtrees_height = [1] * n

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)

        if i == j:
            return

        if self.subtrees_height[i] == self.subtrees_height[j]:
            self.subtrees_height[j] += 1
            self.arr[i] = j
        elif self.subtrees_height[i] < self.subtrees_height[j]:
            self.arr[i] = j
        else:
            self.arr[j] = i


if __name__ == '__main__':

    print '\nUnion-find: '
    print '-------------------------------------------'
    uf = UnionFind(10)

    uf.union(0, 4)
    uf.union(5, 4)
    uf.union(5, 3)
    uf.union(1, 2)
    uf.union(1, 7)
    uf.union(7, 4)

    print uf.arr
    print uf.set_size

    print '\nUnion Find With Specific Canonical Element: '
    print '-------------------------------------------'

    uf = UnionFindWithSpecificCanonicalElement(10)

    uf.union(0, 4)
    uf.union(5, 4)
    uf.union(5, 3)
    uf.union(1, 2)
    uf.union(1, 7)
    uf.union(7, 4)

    print uf.find(3)

    print uf.arr
    print uf.set_size

    print '\nWeighted By Tree\'s Height Union Find: '
    print '-------------------------------------------'

    uf = UnionFindWithTreeHeight(10)

    uf.union(0, 4)
    uf.union(5, 4)
    uf.union(5, 3)
    uf.union(1, 2)
    uf.union(1, 7)
    uf.union(7, 4)

    print uf.arr
    print uf.subtrees_height
