# Define Node
class RB_Node:
    def __init__(self, key, data=None):
        self.data = data
        self.key = key  # Key of Node
        self.p = None  # Parent of Node
        self.left = None  # Left Child of Node
        self.right = None  # Right Child of Node
        self.color = 1  # Red Node as new node is always inserted as Red Node


# Define R-B Tree
class RBTree:
    def __init__(self):
        self.NULL = RB_Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    # Insert New Key
    def insert(self, key):
        node = RB_Node(key)
        node.p = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1  # Set root colour as Red
        self.RB_Insert(node)

    # Insert New Node
    def RB_Insert(self, node):
        node.p = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1  # Set root colour as Red

        y = None
        x = self.root

        while x != self.NULL:  # Find position for new node
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.p = y  # Set p of Node as y
        if y is None:  # If parent i.e, is none then it is root node
            self.root = node
        elif (
            node.key < y.key
        ):  # Check if it is right Node or Left Node by checking the value
            y.left = node
        else:
            y.right = node

        if node.p is None:  # Root node is always Black
            node.color = 0
            return

        if node.p.p is None:  # If parent of node is Root Node
            return

        self.fixInsert(node)  # Else call for Fix Up

    def Tree_Minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def Tree_Maximum(self, node):
        while node.right != self.NULL:
            node = node.right
        return node

    # Code for left rotate
    def LR(self, x):
        y = x.right  # Y = Right child of x
        x.right = y.left  # Change right child of x to left child of y
        if y.left != self.NULL:
            y.left.p = x

        y.p = x.p  # Change parent of y as parent of x
        if x.p is None:  # If parent of x == None ie. root node
            self.root = y  # Set y as root
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    # Code for right rotate
    def RR(self, x):
        y = x.left  # Y = Left child of x
        x.left = y.right  # Change left child of x to right child of y
        if y.right != self.NULL:
            y.right.p = x

        y.p = x.p  # Change parent of y as parent of x
        if x.p is None:  # If x is root node
            self.root = y  # Set y as root
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    # Fix Up Insertion
    def fixInsert(self, k):
        while k.p.color == 1:  # While parent is red
            if k.p == k.p.p.right:  # if parent is right child of its parent
                u = k.p.p.left  # Left child of grandparent
                if (
                    u.color == 1
                ):  # if color of left child of grandparent i.e, uncle node is red
                    u.color = (
                        0  # Set both children of grandparent node as black
                    )
                    k.p.color = 0
                    k.p.p.color = 1  # Set grandparent node as Red
                    k = (
                        k.p.p
                    )  # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.p.left:  # If k is left child of it's parent
                        k = k.p
                        self.RR(k)  # Call for right rotation
                    k.p.color = 0
                    k.p.p.color = 1
                    self.LR(k.p.p)
            else:  # if parent is left child of its parent
                u = k.p.p.right  # Right child of grandparent
                if (
                    u.color == 1
                ):  # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0  # Set color of childs as black
                    k.p.color = 0
                    k.p.p.color = 1  # set color of grandparent as Red
                    k = k.p.p  # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.p.right:  # if k is right child of its parent
                        k = k.p
                        self.LR(k)  # Call left rotate on parent of k
                    k.p.color = 0
                    k.p.p.color = 1
                    self.RR(k.p.p)  # Call right rotate on grandparent
            if k == self.root:  # If k reaches root then break
                break
        self.root.color = 0  # Set color of root as black

    # Function to fix issues after deletion
    def fixDelete(self, x):
        while (
            x != self.root and x.color == 0
        ):  # Repeat until x reaches nodes and color of x is black
            if x == x.p.left:  # If x is left child of its parent
                s = x.p.right  # Sibling of x
                if s.color == 1:  # if sibling is red
                    s.color = 0  # Set its color to black
                    x.p.color = 1  # Make its parent red
                    self.LR(x.p)  # Call for left rotate on parent of x
                    s = x.p.right
                # If both the child are black
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1  # Set color of s as red
                    x = x.p
                else:
                    if s.right.color == 0:  # If right child of s is black
                        s.left.color = 0  # set left child of s as black
                        s.color = 1  # set color of s as red
                        self.RR(s)  # call right rotation on x
                        s = x.p.right

                    s.color = x.p.color
                    x.p.color = 0  # Set parent of x as black
                    s.right.color = 0
                    self.LR(x.p)  # call left rotation on parent of x
                    x = self.root
            else:  # If x is right child of its parent
                s = x.p.left  # Sibling of x
                if s.color == 1:  # if sibling is red
                    s.color = 0  # Set its color to black
                    x.p.color = 1  # Make its parent red
                    self.RR(x.p)  # Call for right rotate on parent of x
                    s = x.p.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.p
                else:
                    if s.left.color == 0:  # If left child of s is black
                        s.right.color = 0  # set right child of s as black
                        s.color = 1
                        self.LR(s)  # call left rotation on x
                        s = x.p.left

                    s.color = x.p.color
                    x.p.color = 0
                    s.left.color = 0
                    self.RR(x.p)
                    x = self.root
        x.color = 0

    # Function to transplant nodes
    def __rb_transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    # Function to return node containing the given key
    def Tree_Search(self, k):
        x = self.root
        while x != self.NULL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # Function to return succesor of x
    def Tree_Successor(self, x):
        if x.right != self.NULL:
            return self.Tree_Minimum(x.right)
        y = x.p
        while y != self.NULL and x == y.right:
            x = y
            y = y.p
        return y

    # Function to return succesor of x
    def Tree_Predecessor(self, x):
        if x.left != self.NULL:
            return self.Tree_Maximum(x.left)
        y = x.p
        while y != self.NULL and x == y.left:
            x = y
            y = y.p
        return y

    # Function to handle deletion
    def delete_node_helper(self, node, key):
        z = self.NULL
        while (
            node != self.NULL
        ):  # Search for the node having that value/ key and store it in 'z'
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if (
            z == self.NULL
        ):  # If Kwy is not present then deletion not possible so return
            print("Value not present in Tree !!")
            return
        else:
            self.RB_Delete(z)

    def RB_Delete(self, z):
        y = z
        y_original_color = y.color  # Store the color of z- node
        if z.left == self.NULL:  # If left child of z is NULL
            x = z.right  # Assign right child of z to x
            self.__rb_transplant(
                z, z.right
            )  # Transplant Node to be deleted with x
        elif z.right == self.NULL:  # If right child of z is NULL
            x = z.left  # Assign left child of z to x
            self.__rb_transplant(
                z, z.left
            )  # Transplant Node to be deleted with x
        else:  # If z has both the child nodes
            y = self.Tree_Minimum(z.right)  # Find minimum of the right subtree
            y_original_color = y.color  # Store color of y
            x = y.right
            if y.p == z:  # If y is child of z
                x.p = y  # Set parent of x as y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 0:  # If color is black then fixing is needed
            self.fixDelete(x)

    # Deletion of node
    def delete(self, key):
        self.delete_node_helper(self.root, key)  # Call for deletion

    # Function to print
    def __printCall(self, node, indent, last):
        if node != self.NULL:
            print(indent, end=" ")
            if last:
                print("R----", end=" ")
                indent += "     "
            else:
                print("L----", end=" ")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    # Function to call print
    def print_RBTree(self):
        self.__printCall(self.root, "", True)

    def print_tree(self, val="key", left="left", right="right"):
        root = self.root
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            # s_color = f"{Fore.RED}RED{Style.RESET_ALL}" if root.color == 1 else f"{Fore.GREEN}BLACK{Style.RESET_ALL}"
            s_color = "RED" if root.color == 1 else "BLACK"

            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s(%s)' % (getattr(root, val), s_color)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s(%s)' % (getattr(root, val), s_color)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, val, left, right)
        for line in lines:
            print(line)

def main():
    red_black_tree = RBTree()
    data = [10, 5, 5, 2, 8, 6, 9, 12]
    # data = [8, 5, 15, 12, 19, 9, 13, 23]
    for each in data:
        red_black_tree.insert(each)
    search_node = red_black_tree.Tree_Search(5)

    red_black_tree.print_tree()
    # red_black_tree.print_RBTree()
    # red_black_tree.LR(search_node)
    # red_black_tree.print_RBTree()


main()

# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>
