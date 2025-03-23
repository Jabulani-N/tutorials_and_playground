# Binary Trees

## 何です

binary trees are essentially doubly linked list structures, *except* they have a third link, allowing two children: `left`, and `right`.

the "previous" slot of the node is replaced with `parent`.

## purpose of binary trees

binary trees allow more efficient sorting and therefore locating of particular elements.

- likely, it it's a exploit to get a lograthimic execution time.

perfect binary tree: all nodes have 0 or 2 children

balanced binary tree: all nodes have same number of children + children's children + etc..

## traversal of binary trees

post/in/pre order traversal of binary tree means when it runs the data in the current node.

* post - AFTER the l(eft) and r(ight) children

* in - INBETWEEN the l(eft) and r(ight) children

* pre - BEFORE the l(eft) and r(ight) children

you'll likely (but not necessarily) be using a recursive function in traversal, so that it can keep track of where it is within the function


