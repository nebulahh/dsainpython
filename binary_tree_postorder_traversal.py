class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                answer.append(node.val)
                
        dfs(root)
        return answer
