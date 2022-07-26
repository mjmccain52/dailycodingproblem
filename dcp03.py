"""
Given the root to a binary tree, implement serialize(root), which 
serializes the tree into a string, and deserialize(s), which 
deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test_1():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

def serialize(root: Node) -> str:
    """Level order traversal, including null nodes."""
    output = ""
    if root is None:
        return output
    queue = []
    queue.append(root)
    while len(queue) > 0:
        output += str(queue[0].val if queue[0] else None) + " "
        node = queue.pop(0)
        if node is not None:
            queue.append(node.left)
            queue.append(node.right)
    
    return output

def deserialize(s: str) -> Node:
    if not s:
        return None
    values = s.split()
    root = Node(values.pop(0))
    nodes = [root]
    while len(values) > 0:
        curr = nodes.pop(0)
        if (left := values.pop(0)) != "None":
            curr.left = Node(left)
            nodes.append(curr.left)
            
        if (right := values.pop(0)) != "None":
            curr.right = Node(right)
            nodes.append(curr.right)
    
    return root
