# tree23.py
# By yohannes dawit

class _Node23:
    def __init__(self, keys = None, trees = None):

        if trees:
            self.trees = [trees]
        else:
            self.trees = []
        if keys:
            self.keys = [keys]
        else:
            self.keys = []
            

    def __contains__(self, key):

        if key in self.keys:
            return True
        else:
            for tree in self.trees:
                if key in tree:
                    return True
        return False
    

    def __iter__(self):

        if len(self.keys) == 1:

            for node in self.trees[0]:
                yield node
                
            yield self.keys[0]
            
            for node in self.trees[1]:
                yield node

        elif len(self.keys) == 2:

            for node in self.trees[0]:
                yield node

            yield self.keys[0]

            for node in self.trees[1]:
                yield node

            yield self.key[1]

            for node in self.trees[2]:
                yield node

    def insert(self, key):
        print("a")
        len_keys = len(self.keys)
        i = 0

        if len_keys == 1:
            print("b")

            if key < self.keys[0]:
                i = 0

            else:
                i = 1

        elif len_keys == 2:
            print("c")

            if key < self.keys[0]:
                i = 0

            elif self.keys[0] < key < self.keys[1]:
                i = 1

            else:
                i = 2

        if self.trees:
            print("d")
            ans = self.trees[i].insert(key)

            if ans:
                print("e")
                key, left, right = ans
                self.keys.insert(i, key)
                self.trees[i] = [left, right]
        else:
            print("f")
            self.keys.insert(i, key)

        if len(self.keys) == 3:
            print("g")
            l_half = _Node23(self.keys[0], self.trees[0:2])
            r_half = _Node23(self.keys[2], self.trees[2:])
            return self.keys[1], l_half, r_half

    def pretty_print(self):
        print(self.keys)

        for tree in self.trees:
            tree.pretty_print()


class Tree23:
    def __init__(self, nodes):
        self.root = _Node23()

        for node in nodes:
            self.insert(node)

    def __contains__(self, key):
        return key in self.root

    def __iter__(self):

        for node in self.root:
            yield node

    def insert(self, key):
        temp = self.root.insert(key)

        if temp:
            key, left, right = temp
            node = _Node23(key, [left, right])
            self.root.insert(node)

    def pretty_print(self):
        self.root.pretty_print()

def main():
    
if __name__ == "__main__":
    main()
