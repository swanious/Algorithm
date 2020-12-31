def reverseList(head):
    def reverse(node, prev = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head)

head = [1,2,3,4,5]
reverseList(head)