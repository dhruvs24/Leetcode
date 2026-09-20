class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxVal):
            if root is None:
                return 0
            res = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)
            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)
            return res
        return dfs(root, root.val)