from typing import Optional

# 리트코드에서 기본으로 제공하는 이진 트리 노드 클래스
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # 가장 긴 직경을 기록할 인스턴스 변수 (장부)
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_diameter = 0
        
        # 어제 짰던 그 깊이 탐색 함수 (로컬 함수로 만들어도 되고 클래스 메서드로 해도 무방!)
        def dfs(node: Optional[TreeNode]) -> int:
            # 1. Base Case: 바닥을 치면 깊이 0 반환
            if node is None:
                return 0
            
            # 2. 왼쪽, 오른쪽 자식의 깊이를 각각 재귀로 구하기
            left_depth, right_depth = dfs(node.left), dfs(node.right)
            
            # 3. 🎯 [오늘의 핵심] 현재 노드를 꺾이는 지점(루트)으로 삼았을 때의 직경 계산
            # 그 직경이 self.max_diameter보다 크면 장부 업데이트!
            diameter = left_depth + right_depth
            # if node.left is not None: diameter += 1
            # if node.right is not None: diameter += 1 # 추가해야할거같은데... 복잡도 높아지려나 # 아! 이건 실수였다!! ㅋㅋㅋ
            
            # 디버깅해서 알았다
            # print("==========")
            # print("node.val: ", node.val)
            # print("node.val: ", node.left)
            # print("node.val: ", node.right)
            # print("diameter: ", diameter)
            
            # print("before self.max_diameter: ", self.max_diameter)

            self.max_diameter = max(self.max_diameter, diameter)

            # print("after self.max_diameter: ", self.max_diameter)

            # print("==========")

            # 4. 내 부모 노드를 위해 '나의 최대 깊이'를 반환 (어제랑 동일)
            return 1 + max(left_depth, right_depth)
        
        # 트리의 루트부터 DFS 순회 시작
        dfs(root)
        
        # 순회가 끝나면 장부에 적힌 최댓값이 정답!
        return self.max_diameter
    


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: [1, 2, 3, 4, 5] 조립
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3)
    root1 = TreeNode(1, node2, node3)
    
    print("TC 1:", sol.diameterOfBinaryTree(root1)) 
    # 예상 결과: 3 (경로: 4->2->1->3 또는 5->2->1->3)
    
    # Test Case 2: [1, 2]
    root2 = TreeNode(1, TreeNode(2), None)
    print("TC 2:", sol.diameterOfBinaryTree(root2)) #엥 왜 max_diameter = 3, 이게 이어지는거지??
    # 예상 결과: 1 (경로: 2->1)