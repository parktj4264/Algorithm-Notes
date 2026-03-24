**📍 [진도 체크]**

우리는 지금 [STEP 3 (자료구조 2 - 공간 데이터)]의 꽃, 트리(Tree) 파트를 달리고 있어. 
어제 20번 문제에서 DFS로 트리 바닥까지 찍고 올라오면서 **'트리의 최대 깊이'** 구하는 점화식을 완벽하게 짰지? 
오늘은 그 코드에서 **딱 한 줄, 아니 정확히는 변수 하나만 추가**하면 날로 먹을 수 있는 **'21. 이진 트리의 직경 (LeetCode 543)'**이야. 어제 짠 깊이(Depth) 구하는 함수가 오늘 문제의 핵심 부품(모듈)이 될 테니까 유기적인 연결고리를 잘 느껴봐!

---

# 1단계: 환경 세팅 지시 (Setup First)

터미널 열고 오늘 날짜(26년 3월 24일) 기준으로 폴더랑 파일 딱 세팅하자.

* **📂 찐최종 네이밍 룰:** `21_260324_diameter_of_binary_tree_L543`
* **📄 파일 구성:** `solution.py` (문제 풀이), `note.md` (오답 및 Big-O 최적화 노트)

---

# 2단계: 문제 및 가이드 제시 (The 'For-loop' Perspective)

### 🚀 문제 543: Diameter of Binary Tree
### 🔗 **링크:** [https://leetcode.com/problems/diameter-of-binary-tree/](https://leetcode.com/problems/diameter-of-binary-tree/)

## **📜 문제 설명 (Mission Briefing):**
이진 트리의 루트(`root`)가 주어질 때, 트리의 **직경(Diameter)**을 구하는 문제야. 
직경이란, 트리 안에 있는 **임의의 두 노드 사이의 가장 긴 경로(간선의 개수)**를 말해. 
여기서 함정! 이 가장 긴 경로가 **반드시 꼭대기(Root)를 통과할 필요는 없어.** 트리 어딘가에 치우쳐진 엄청 긴 팔 두 개가 있다면, 그 두 팔을 더한 게 전체 트리의 직경이 될 수도 있거든.

* **예시 1:** `root = [1, 2, 3, 4, 5]`
  * 4 -> 2 -> 1 -> 3 이나 5 -> 2 -> 1 -> 3 경로가 제일 길어. (간선 3개)
  * 출력: `3`

```
              [ 1 ]  <-- Root (꼭대기)
             🟢  🔵
           🟢     🔵   <-- (간선 2, 3)
         [ 2 ]   [ 3 ]
         🟢  \
       🟢     \        <-- (간선 1)
     [ 4 ]   [ 5 ]
```



## **🎯 오늘 부술 for문 (Big-O 관점):**
무지성으로 푼다면 "모든 노드에 대해 각각 왼쪽 깊이와 오른쪽 깊이를 구해서 더해보자!" 하면서 이중 탐색($O(N^2)$)을 하려고 하겠지. 
하지만 우린 통계학도잖아? 데이터를 한 번 스캔($O(N)$)하면서 필요한 통계량(최댓값)을 동시에 업데이트해 나갈 거야. 

어제 짰던 DFS 깊이 탐색 함수가 바닥에서부터 깊이를 계산하며 위로 올라올(Bottom-up) 때, **"아, 방금 내 왼쪽 깊이랑 오른쪽 깊이를 더해봤는데, 이게 지금까지 발견한 직경 중 제일 큰데?"** 싶으면 전역 최댓값 장부(`self.max_diameter`)에 스윽 기록만 해두면 끝이야. 시간 복잡도 $O(N)$, 공간 복잡도 $O(\log N)$(재귀 콜스택)으로 이중 for문을 완벽하게 찢어버리자.

## **🛠️ 네가 해야 할 것:**
어제 짠 `maxDepth` 논리를 그대로 쓸 거야. 
1. **상태 기록 장부:** 깊이를 리턴하는 재귀 함수와 별개로, '지금까지 찾은 가장 큰 직경'을 기억할 변수 `self.max_diameter`를 `__init__`이나 함수 도입부에 만들어 둬. (어제 배운 `self` 개념 바로 써먹기!)
2. **점화식 1 (직경 업데이트):** 현재 노드에서 뻗어나갈 수 있는 가장 긴 경로는? **`왼쪽 자식의 최대 깊이 + 오른쪽 자식의 최대 깊이`**야. 이 값이 `self.max_diameter`보다 크면 갱신해.
3. **점화식 2 (깊이 반환):** 내 부모 노드한테는 어제처럼 **`max(왼쪽 깊이, 오른쪽 깊이) + 1`**을 똑같이 리턴해줘서 깊이 계산이 계속 위로 이어지게 해.

## **🧰 필요한 파이썬 내장 함수/문법(범용사용법):**
**클래스 인스턴스 변수(`self.variable`) 활용**
재귀 함수는 자꾸 위로 값을 `return` 해버리기 때문에, 재귀 사이클 밖에서 '최댓값'을 계속 누적해서 기억하려면 클래스 소속의 변수(`self`)를 쓰는 게 제일 깔끔해.

```python
class Solution:
    def __init__(self):
        self.best_score = 0  # 클래스가 태어날 때 장부를 하나 펼침

    def dfs(self, node):
        # ... 깊이 계산 ...
        # 현재 노드에서 계산한 점수가 역대급이면 장부 업데이트!
        self.best_score = max(self.best_score, current_score)
        return depth
```

---

# 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

어제 배운 `self` 개념과, 어제 짰던 깊이 탐색 코드를 머릿속에 띄워놓고 빈칸을 채워봐!

```python
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
        
        # 어제 짰던 그 깊이 탐색 함수 (로컬 함수로 만들어도 되고 클래스 메서드로 해도 무방!)
        def dfs(node: Optional[TreeNode]) -> int:
            # 1. Base Case: 바닥을 치면 깊이 0 반환
            pass
            
            # 2. 왼쪽, 오른쪽 자식의 깊이를 각각 재귀로 구하기
            pass
            
            # 3. 🎯 [오늘의 핵심] 현재 노드를 꺾이는 지점(루트)으로 삼았을 때의 직경 계산
            # 그 직경이 self.max_diameter보다 크면 장부 업데이트!
            pass
            
            # 4. 내 부모 노드를 위해 '나의 최대 깊이'를 반환 (어제랑 동일)
            pass
        
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
    print("TC 2:", sol.diameterOfBinaryTree(root2)) 
    # 예상 결과: 1 (경로: 2->1)
```

어제 코드에서 정말 딱 한 꼬집만 얹으면 풀리는 문제야. 재귀가 돌면서 깊이를 구하는 동시에, 몰래 직경 장부(`self.max_diameter`)를 업데이트하고 오는 그 짜릿함을 느껴봐. 다 짜면 바로 들고 와! 🔥