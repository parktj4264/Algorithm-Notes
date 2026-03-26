from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # 🎯 node와 함께 이 노드가 지켜야 할 '하한선(low)'과 '상한선(high)'을 같이 들고 다님!
        def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
            # 1. Base Case: 바닥을 쳤다(None)는 건, 끝까지 규칙 위반이 없었다는 뜻!
            if node is None:
                return True
            
            # 2. 현재 노드의 값이 허용 구간 (low < node.val < high)을 벗어났다면?
            # 가차 없이 False 반환!
            if not (low < node.val < high):
                return False
            
            # 3. 왼쪽 자식 검사 & 오른쪽 자식 검사 (둘 다 True여야 전체가 True)
            # 힌트: 왼쪽으로 갈 때는 상한선(high)이 내 값(node.val)으로 좁혀짐!
            # 힌트: 오른쪽으로 갈 때는 하한선(low)이 내 값(node.val)으로 좁혀짐!
            left_return = dfs(node.left, low, float(node.val))
            right_return = dfs(node.right, float(node.val), high)

            if left_return and right_return:
                return True
            else:
                return False

        # 처음 꼭대기 노드는 아무런 제약이 없으므로 -무한대 ~ +무한대 구간을 줌
        return dfs(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: 올바른 BST [2, 1, 3]
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print("TC 1:", sol.isValidBST(root1)) # 예상 결과: True
    
    # Test Case 2: 아까 말한 '뉴비 낚시용' 함정 트리 [5, 1, 4, null, null, 3, 6]
    # 4의 왼쪽 자식이 3이라서 부분적으론 맞지만, 5의 오른쪽 가문에 3이 있으므로 False!
    node4 = TreeNode(4, TreeNode(3), TreeNode(6))
    root2 = TreeNode(5, TreeNode(1), node4)
    print("TC 2:", sol.isValidBST(root2)) # 예상 결과: False