class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Huff(object):
    @staticmethod
    def create_tree(array):
        nodes = []
        for i in array:
            nodes.append(Node(i))
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.val)
            left_node = nodes.pop(0)
            right_node = nodes.pop(0)
            treeNode = Node(left_node.val + right_node.val)
            treeNode.left = left_node
            treeNode.right = right_node
            nodes.append(treeNode)
        return nodes[0]

    def get_node(self, node):
        if node is None:
            return
        print(node.val, end=" ")
        self.get_node(node.left)
        self.get_node(node.right)


if __name__ == '__main__':
    array = [13, 7, 8, 3, 29, 6, 1]
    h = Huff()
    tmp = h.create_tree(array)
    res = h.get_node(tmp)
    print(res)
