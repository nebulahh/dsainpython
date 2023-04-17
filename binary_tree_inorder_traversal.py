class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                answer.append(node.val)
                dfs(node.right)
        dfs(root)
        return answer
