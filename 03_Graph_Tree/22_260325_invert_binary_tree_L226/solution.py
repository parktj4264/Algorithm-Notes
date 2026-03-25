from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. Base Case: root가 비어있다면 None 반환
        if root is None:
            return None
        
        # 2. 파이썬 치트키를 써서 현재 노드의 왼쪽 자식과 오른쪽 자식을 Swap!
        root.left, root.right = root.right, root.left
        
        # 3. 바뀐 왼쪽 자식을 타고 내려가면서 재귀적으로 뒤집기 (self.invertTree 활용)
        self.invertTree(root.left)
        
        # 4. 바뀐 오른쪽 자식을 타고 내려가면서 재귀적으로 뒤집기
        self.invertTree(root.right)
        
        # 5. 다 뒤집힌 현재 트리의 root 반환
        return root


# 🎁 트리를 눈으로 확인하기 위한 시각화 툴 (건드릴 필요 없음)
def display_tree(node, space=0, LEVEL_SPACE=6):
    if node is None:
        return
    space += LEVEL_SPACE
    display_tree(node.right, space)
    print(' ' * (space - LEVEL_SPACE) + f"-> {node.val}")
    display_tree(node.left, space)



if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: [4, 2, 7, 1, 3, 6, 9] 조립
    root1 = TreeNode(4, 
                TreeNode(2, TreeNode(1), TreeNode(3)), 
                TreeNode(7, TreeNode(6), TreeNode(9)))
    
    print("\n[ 🌳 원본 트리 ]")
    display_tree(root1)
    
    # 반전 실행!
    inverted_root1 = sol.invertTree(root1)
    
    print("\n[ 🔄 반전된 트리 ]")
    display_tree(inverted_root1)
    print("-" * 40)