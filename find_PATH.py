# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    res = []
    res1 = []
    def FindPath(self, root, expectNumber):
        def recur(root,path,sums):
            if root:
                path.append(root.val)
                sums = sums+root.val

                if not root.left and not root.right:
                    if sums==expectNumber:
                        self.res.append(path)
                else:
                    if root.left:
                        recur(root.left,path.copy(),sums)
                    if root.right:
                        recur(root.right,path.copy(),sums)
        recur(root,[],0)
        return self.res

    def root2leaf(self,root,alist):
        if not root:
            return None
        alist.append(root.val)
        if not root.left and not root.right:
            self.res1.append(alist)

        if root.left:
            self.root2leaf(root.left,alist.copy())
        if root.right:
            self.root2leaf(root.right,alist.copy())

##找到所有子路径
class Solution1:
    res = []

    def root2leaf(self, root, alist):
        if not root:
            return None
        alist.append(root.val)
        if not root.left and not root.right:
            self.res.append(alist)

        if root.left:
            self.root2leaf(root.left, alist.copy())
        if root.right:
            self.root2leaf(root.right, alist.copy())


class Solution2:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        res = []
        path = []
        def recur(root, tar):
            if not root:return
            path.append(root.val)
            tar += root.val
            if (tar == expectNumber) and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()
        recur(root, 0)
        return res


#
#
# @param root TreeNode类
# @return int整型
#
class Solution3:

    def sumNumbers(self, root):
        res = self.binaryTreePaths1(root)
        sums = 0
        for i in range(len(res)):
            sums = sums + int(res[i])
        return sums

    def binaryTreePaths(self, root: TreeNode):
        if not root:
            return []
        result = []

        def dfs(root, auxiliary):
            if not root:
                return
            if not root.left and not root.right:
                auxiliary_auxiliary = auxiliary + str(root.val)
                result.append(auxiliary_auxiliary)
            dfs(root.left, auxiliary + str(root.val))
            dfs(root.right, auxiliary + str(root.val))

        dfs(root, '')
        return result

    def binaryTreePaths1(self, root: TreeNode):
        if root == None:
            return []
        res = []

        def dfs(root, astr):
            if root == None:
                return None
            if not root.left and not root.right:
                number = astr + str(root.val)
                res.append(number)
            dfs(root.left, astr + str(root.val))
            dfs(root.right, astr + str(root.val))

        dfs(root, '')
        return res


f = Solution3()

pRoot = TreeNode(1)
left = TreeNode(2)
left.left = TreeNode(3)
left.right = TreeNode(4)

right = TreeNode(5)
right.left = TreeNode(6)
right.right = TreeNode(7)
pRoot.left = left
pRoot.right = right

res = f.sumNumbers(pRoot)


