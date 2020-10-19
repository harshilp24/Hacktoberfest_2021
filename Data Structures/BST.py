class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, data):
        if self.val == data:
            return False

        elif self.val > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.val == data:
            return True
        elif self.val > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.val), end=" ")
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.val), end=" ")

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.val), end=" ")
            if self.right:
                self.right.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print('Preorder')
        self.root.preorder()

    def postorder(self):
        print('Postorder')
        self.root.postorder()

    def inorder(self):
        print('Inorder')
        self.root.inorder()


bst = Tree()
bst.insert(10)
bst.insert(40)
bst.insert(44)
bst.insert(32)
bst.preorder()
print()
bst.postorder()
print()
bst.inorder()
bst.find(77)