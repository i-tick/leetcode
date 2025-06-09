# Given the root of a perfect binary tree, where each node is equipped with an additional pointer, next, connect all nodes from left to right. Do so in such a way that the next pointer of each node points to its immediate right sibling except for the rightmost node, which points to the first node of the next level.

# The next pointer of the last node of the binary tree (i.e., the rightmost node of the last level) should be set to NULL.


from collections import deque

def connect_all_siblings(root):

    if not root:
        return root
        
    q = deque([root])
    while q:
        qlen = len(q)
        prev = q[-1]
        for i in range(qlen):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        for i in range(len(q)-1):
            q[i].next = q[i+1]
        if q:
            prev.next = q[0]
        else:
            prev.next = None
            

    
    return root