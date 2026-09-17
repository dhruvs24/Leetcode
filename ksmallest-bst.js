/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root, k) {
        const result = []
        function dfs(root){
            if(root === null){
                return
            }
            
            dfs(root.left)
            result.push(root.val)
            dfs(root.right)
        }
        dfs(root)
        return result[k - 1]
    }
}
