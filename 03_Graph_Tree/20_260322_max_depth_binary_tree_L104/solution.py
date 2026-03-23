from typing import Optional

# 리트코드에서 기본으로 제공하는 이진 트리 노드 클래스
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. Base Case: 노드가 없으면 깊이는 0
        if root is None:
            return 0
        
        # 2. 왼쪽 자식과 오른쪽 자식의 최대 깊이를 각각 DFS(재귀)로 구하기
        left_depth, right_depth = self.maxDepth(root.left), self.maxDepth(root.right)
        
        # 3. 둘 중 더 큰 값에 1(현재 노드)을 더해서 반환하기
        return 1 + max(left_depth, right_depth)







if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: [3, 9, 20, null, null, 15, 7] 조립하기
    # 트리를 아래에서 위로(Bottom-up) 조립하는 과정
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20 = TreeNode(20, node15, node7)
    node9 = TreeNode(9)
    root1 = TreeNode(3, node9, node20)
    
    print("TC 1:", sol.maxDepth(root1)) # 예상 결과: 3
    
    # Test Case 2: [1, null, 2] 조립하기
    root2 = TreeNode(1, None, TreeNode(2))
    print("TC 2:", sol.maxDepth(root2)) # 예상 결과: 2
    
    # Test Case 3: 빈 트리
    print("TC 3:", sol.maxDepth(None)) # 예상 결과: 0