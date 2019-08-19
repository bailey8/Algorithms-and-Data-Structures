class Solution(object):
    def isSameTree(self, p, q):
        def same(p,q):
            if (p and not q) or (q and not p):
                return False
            if not p and not q:
                return True
            if p.val == q.val:
                return True
        stack = []
        stack.append((p,q))
        while stack:
            p,q = stack.pop()
            if not same(p,q):
                return False
            if p:
                stack.append((p.left,q.left))
                stack.append((p.right,q.right))
        return True

def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """    
    # p and q are both None
    if not p and not q:
        return True
    # one of p and q is None
    if not q or not p:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.right, q.right) and \
            self.isSameTree(p.left, q.left)

def isSameTree2(self, p, q):
    def match(p,q):
        if(not p and q)or(not q and p):
            return False
        if not p and not q:
            return True
        if p.val == q.val:
            return match(p.left,q.left) and match(p.right,q.right)
        return False
    return match(p,q)
        