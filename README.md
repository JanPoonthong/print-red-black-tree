# print-red-black-tree
This is source code debugging, print, console, visualizing red black tree in Python

You can modify `s_color` to match your style of data, in my case; RED=1 and BLACK=0

Check full example: `RedBlackTree.py`

```python
        def print_tree(self, val="key", left="left", right="right"):
        root = self.root
        visited = set()

        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            s_color = "RED" if root.color == 1 else "BLACK"

            if root is not self.NIL:
                if root in visited:
                    line = "***%s(%s)***" % (getattr(root, val), s_color)
                    width = len(line)
                    height = 1
                    middle = width // 2
                    return [line], width, height, middle
                visited.add(root)

            if getattr(root, right) is None and getattr(root, left) is None:
                line = "%s(%s)" % (getattr(root, val), s_color)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = "%s" % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * " " + (n - x - 1) * "_" + s
                second_line = x * " " + "/" + (n - x - 1 + u) * " "
                shifted_lines = [line + u * " " for line in lines]
                return (
                    [first_line, second_line] + shifted_lines,
                    n + u,
                    p + 2,
                    n + u // 2,
                )

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = "%s" % getattr(root, val)
                u = len(s)
                first_line = s + x * "_" + (n - x) * " "
                second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
                shifted_lines = [u * " " + line for line in lines]
                return (
                    [first_line, second_line] + shifted_lines,
                    n + u,
                    p + 2,
                    u // 2,
                )

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = "%s(%s)" % (getattr(root, val), s_color)
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
            second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
            if p < q:
                left += [n * " "] * (q - p)
            elif q < p:
                right += [m * " "] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, val, left, right)
        for line in lines:
            print(line)
        print("---------------------------------------------------------------")

```

Output:
```
                           ___________5(BLACK)___________________________
                          /                                              \
            __________5(BLACK)____                         ___________8(RED)__________________________
           /                      \                       /                                           \
     ___2(RED)____            0(BLACK)             ___6(BLACK)____                      __________10(BLACK)___________
    /             \                               /               \                    /                              \
0(BLACK)      0(BLACK)                        0(BLACK)        0(BLACK)           ___9(RED)____                  ___12(RED)____
                                                                                /             \                /              \
                                                                            0(BLACK)      0(BLACK)         0(BLACK)       0(BLACK)
```

Credit https://stackoverflow.com/a/65865825/12271495 + https://github.com/strager (@strager)
