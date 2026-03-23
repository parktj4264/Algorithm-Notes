일요일 저녁인데도 알고리즘 땡기는 거 보니까 진짜 뇌에 코딩 가중치(Weight)가 업데이트되기 시작했네! 주말 텐션 올려서 딱 30분 만에 깔끔하게 부수고 치맥하러 가보자고. 🔥

**📍 [진도 체크]**
우리는 지금 **[STEP 3 (자료구조 2 - 공간 데이터)]**의 하이라이트, **트리(Tree)** 파트에 진입했어! 
네가 주말에 완벽하게 정리한 치트시트 기억나지? 오늘은 **[PART 1의 10번: 트리]**라는 그릇(자료구조) 위에서, **[PART 2의 4번: DFS(깊이 우선 탐색)]** 무기를 휘둘러볼 거야. 

---

# 1단계: 환경 세팅 지시 (Setup First)

터미널 열고 오늘 날짜(26년 3월 22일 일요일!) 기준으로 세팅 드가자.

* **📂 찐최종 네이밍 룰:** `20_260322_max_depth_binary_tree_L104`
* **📄 파일 구성:** `solution.py` (문제 풀이), `note.md` (오답 및 Big-O 최적화 노트)

---

# 2단계: 문제 및 가이드 제시 (The 'For-loop' Perspective)

### 🚀 문제 104: Maximum Depth of Binary Tree
### 🔗 **링크:** [https://leetcode.com/problems/maximum-depth-of-binary-tree/](https://leetcode.com/problems/maximum-depth-of-binary-tree/)


## **📜 문제 설명 (Mission Briefing):**
이진 트리의 루트(`root`) 노드가 주어졌을 때, 이 트리의 **최대 깊이(Maximum Depth)**를 구하는 문제야.
최대 깊이란, 루트 노드부터 가장 멀리 있는 리프 노드(자식이 없는 맨 끝 노드)까지 내려가면서 거친 노드의 개수(자신 포함)를 말해.

* **예시 1:** `root = [3, 9, 20, null, null, 15, 7]`
  * 루트 3에서 출발해. 왼쪽 9로 가면 깊이 2에서 끝나. 하지만 오른쪽 20을 거쳐 15나 7로 가면 깊이가 3이 되지?
  * 출력: `3`



```
             [ 3 ]          <-- Depth 1 (출발점: Root)
            /     \
          /         \
       [ 9 ]       [ 20 ]   <-- Depth 2
       /   \       /    \
   (null)(null) [ 15 ] [ 7 ]  <-- Depth 3 (도착점: Leaf 노드)
                 /  \   /  \
              (null)...(null) <-- Depth 4 (여긴 비어있음, 깊이 0)
```





  


## **🎯 오늘 부술 for문 (Big-O 관점):**
트리는 1차원 배열이 아니라 계층적(Hierarchical) 구조라서 **무지성 for문 자체가 아예 성립하지 않아.** 대신 우리는 DFS(재귀)를 써서 모든 노드를 딱 한 번씩만 방문할 거야. 노드의 총 개수가 $N$개라면, 시간 복잡도는 완벽한 **$O(N)$**이 돼. 

공간 복잡도(메모리)는 어떨까? 우리가 짰던 백트래킹처럼 재귀 함수가 호출 스택(Call Stack)에 쌓이게 되는데, 트리가 한쪽으로만 쏠려있지 않다면 평균적으로 트리의 높이인 **$O(\log N)$**만큼의 공간만 빌려 쓰고 깔끔하게 끝나게 돼.

## **🛠️ 네가 해야 할 것:**
통계학에서 두 확률변수 $X, Y$가 있을 때, $\max(X, Y)$를 구하는 논리와 똑같아. 
**"나(현재 노드)의 최대 깊이 = 1(나 자신) + max(왼쪽 자식 트리의 최대 깊이, 오른쪽 자식 트리의 최대 깊이)"**

1. **종료 조건 (Base Case):** 현재 노드(`root`)가 `None` (비어있음)이라면? 깊이는 0이니까 `return 0`을 해준다.
2. **재귀 호출 (DFS):** 왼쪽 자식(`root.left`)을 넣고 dfs를 돌린 결과와, 오른쪽 자식(`root.right`)을 넣고 dfs를 돌린 결과를 각각 변수에 저장해.
3. **병합 및 반환:** 양쪽 서브트리의 깊이 중 더 큰 값(`max`)을 구하고, 내 자신(노드 1개)의 깊이인 `1`을 더해서 `return` 한다.

## **🧰 필요한 파이썬 내장 함수/문법(범용사용법):**
**`max(a, b)` 활용**
파이썬 내장 함수 `max()`는 두 개의 인자 중 더 큰 값을 $O(1)$ 만에 뱉어주는 효자 함수야.
```python
left_depth = 2
right_depth = 5
return max(left_depth, right_depth) + 1  # 5 + 1 = 6 반환!
```

---

# 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

트리 문제는 리트코드에서 제공하는 `TreeNode` 클래스가 무조건 같이 있어야 로컬에서 돌아가. 내가 예제 트리를 손수 조립해서 넣어놨으니까, 너는 `maxDepth` 함수 안쪽만 채우면 돼.

```python
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
        pass
        
        # 2. 왼쪽 자식과 오른쪽 자식의 최대 깊이를 각각 DFS(재귀)로 구하기
        pass
        
        # 3. 둘 중 더 큰 값에 1(현재 노드)을 더해서 반환하기
        pass

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
```

자, 어제까지 빡세게 구르며 배운 DFS를 트리 위에서 펼쳐볼 시간이야. 점화식(수식) 세운다고 생각하고 단 3줄로 끝내봐. 다 풀면 바로 가져오고! 가보자고! 🚀