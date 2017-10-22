class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value

    def remove_node(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
                return True
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                return True
            elif self.left_child and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
                return True
            elif self.left_child and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
                return True
            elif self.right_child and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
                return True
            elif self.right_child and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
                return True
            else:


    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def find_smaller_node(self):
        if self.left_child:
            return self.left_child.find_smaller_node()
        else:
            return self

    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

    def pre_order_traversal(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order_traversal()

        if self.right_child:
            self.right_child.pre_order_traversal()

    def in_order_traversal(self):
        if self.left_child:
            self.left_child.in_order_traversal()

        print(self.value)

        if self.right_child:
            self.right_child.in_order_traversal()

    def post_order_traversal(self):
        if self.left_child:
            self.left_child.post_order_traversal()

        if self.right_child:
            self.right_child.post_order_traversal()

        print(self.value)
