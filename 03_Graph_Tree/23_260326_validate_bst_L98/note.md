**📍 [진도 체크]**
우리는 지금 **[STEP 3 (자료구조 2 - 공간 데이터)]**의 트리 파트 마지막 보스를 만나러 왔어. 
지금까지는 그냥 이진 트리(Binary Tree)였다면, 오늘은 조건이 하나 더 붙은 **'이진 탐색 트리(BST: Binary Search Tree)'**야. 어제 그저께 배운 DFS 재귀 함수에다가 통계학의 **'신뢰구간(Confidence Interval)'** 개념을 살짝 얹으면 끝나는 문제야.

---

# 1단계: 환경 세팅 지시 (Setup First)

터미널 열고 오늘 날짜(26년 3월 26일) 파일부터 세팅하자! 풋살 후니까 손가락 속도 올려!

* **📂 찐최종 네이밍 룰:** `23_260326_validate_bst_L98`
* **📄 파일 구성:** `solution.py` 

---

# 2단계: 문제 및 가이드 제시 (The 'For-loop' Perspective)

### 🚀 문제 98: Validate Binary Search Tree
### 🔗 **링크:** [https://leetcode.com/problems/validate-binary-search-tree/](https://leetcode.com/problems/validate-binary-search-tree/)

## **📜 문제 설명 (Mission Briefing):**
이진 트리의 루트(`root`)가 주어졌을 때, 이 트리가 **올바른 '이진 탐색 트리(BST)'인지 검증(True/False)** 하는 문제야.
BST의 절대 규칙 3가지는 다음과 같아:
1. 노드의 **왼쪽 서브트리(가문 전체)**에는 노드의 값보다 **작은** 값들만 있어야 한다.
2. 노드의 **오른쪽 서브트리(가문 전체)**에는 노드의 값보다 **큰** 값들만 있어야 한다.
3. 양쪽 서브트리 모두 다 BST여야 한다. (즉, 중복 값은 허용 안 됨!)



## **🎯 오늘 부술 로직 (Big-O 관점 & 통계학 비유):**
뉴비들이 제일 많이 하는 1차원적인 실수가 뭔지 알아? 
"오! 내 왼쪽 자식이 나보다 작고, 오른쪽 자식이 나보다 크면 True네?" 하고 바로 아래 자식만 검사하는 거야. 

**🚨 함정 트리 (부분은 맞지만 전체가 틀림)**
```text
          [ 5 ]
         /     \
       [4]     [ 6 ]
               /   \
             [3]   [7]  <-- 3은 6의 왼쪽이라 맞지만, 루트 5의 오른쪽 가문인데 5보다 작아서 ❌
```

이걸 해결하려면 통계에서 **상한선(Upper Bound)**과 **하한선(Lower Bound)**을 주고 데이터를 필터링하듯, DFS가 밑으로 파고들 때마다 허용 구간 `(low, high)`을 좁혀가면서 내려가야 해.

1. 처음 꼭대기 `[5]`는 아무 제한이 없으니까 `(-∞, ∞)` 구간을 부여받아.
2. `[5]`에서 **왼쪽**으로 내려가면? **"너는 무조건 5보다는 작아야 해!"** ➔ 구간이 `(-∞, 5)`로 좁혀짐. (상한선 갱신)
3. `[5]`에서 **오른쪽**으로 내려가면? **"너는 무조건 5보다는 커야 해!"** ➔ 구간이 `(5, ∞)`로 좁혀짐. (하한선 갱신)
4. 만약 내려갔는데 자기한테 주어진 구간 `(low, high)`를 벗어난 숫자가 있다? 바로 `False` 때리고 백트래킹!

## **🛠️ 네가 해야 할 것:**
어제 배운 대로 로컬 함수 `dfs(node, low, high)`를 만들어서 파라미터를 3개 넘기자.
파이썬에서 무한대는 `float('-inf')`, `float('inf')`로 쓸 수 있어.

---

# 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

풋살의 열기 그대로, 어제 마스터한 재귀를 써서 이 BST를 검증해 보자!

```python
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
            pass
            
            # 2. 현재 노드의 값이 허용 구간 (low < node.val < high)을 벗어났다면?
            # 가차 없이 False 반환!
            pass
            
            # 3. 왼쪽 자식 검사 & 오른쪽 자식 검사 (둘 다 True여야 전체가 True)
            # 힌트: 왼쪽으로 갈 때는 상한선(high)이 내 값(node.val)으로 좁혀짐!
            # 힌트: 오른쪽으로 갈 때는 하한선(low)이 내 값(node.val)으로 좁혀짐!
            pass
            
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
```

어제 삽질하면서 `node` 파라미터 들고 다니는 건 완벽하게 체화했지? 
오늘은 거기에 `low`, `high`라는 구간 통계량(?)만 추가해서 갱신해 주면 돼. 딱 10분 컷 내고 샤워하러 가자! 다 짜면 바로 들고 와! 🚿🏃‍♂️💨






<br><br><br><br><br><br>





---

### 💡 PT쌤의 Pythonic 꿀팁 (안 고쳐도 무방함!)

형 코드가 논리적으로 너무 완벽해서 굳이 손댈 필요는 없지만, 나중에 실무가서 파이썬 고인물 소리 듣게 1%만 더 깎아볼게.

**1. `float(node.val)` ➔ 그냥 `node.val`**
C나 Java는 정수형이랑 실수형(float) 섞어 쓰면 에러 뿜는데, 파이썬은 진짜 똑똑해서 알아서 실수/정수 호환해서 비교해 줘. 그래서 굳이 `float()`로 안 감싸줘도 `node.val < float('inf')`가 완벽하게 돌아가!

**2. `if / else` 문 한 줄로 압축하기**
```python
            # 형이 짠 코드 (직관성 100점!)
            if left_return and right_return:
                return True
            else:
                return False
            
            # 🐍 파이썬 썩은물들의 방식
            # "어차피 and 연산의 결과가 True/False니까 그냥 그 결과를 리턴하면 되잖아?!"
            return left_return and right_return
```
결국 3번 스텝을 이렇게 단 한 줄로 줄일 수 있어.
`return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)`

---

### 📝 [복습 노트] 바로 복붙하고 샤워하러 가자!


# 📝 [복습 노트] 23. 이진 탐색 트리 검증 (LeetCode 98)
**날짜:** 2026-03-26
**소요 시간:** 10분 컷 (풋살 직후 아드레날린 버프 🔥)

## 1. 🎯 핵심 로직: 신뢰구간(Boundary) 업데이트
* **문제점:** 현재 노드의 바로 아래 자식만 크기 비교를 하면, 후손 노드가 할아버지 노드의 범위를 침범하는 '함정'을 잡을 수 없다.
* **해결책 (Top-down DFS):** 위에서 아래로 내려갈 때, 해당 가문이 지켜야 할 **하한선(low)과 상한선(high)**을 계속 물려주면서 검증한다.

## 2. 🧮 점화식 (구간 좁히기)
* **초기 상태 (루트):** `(-∞, ∞)` 아무 제약 없음.
* **왼쪽 자식으로 갈 때:** 최대 상한선이 **현재 노드의 값**으로 좁혀짐! `dfs(node.left, low, node.val)`
* **오른쪽 자식으로 갈 때:** 최소 하한선이 **현재 노드의 값**으로 좁혀짐! `dfs(node.right, node.val, high)`

## 3. 🐍 Pythonic Code (조건문 최적화)
```python
# 현재 노드가 허용 구간을 벗어나면 즉각 처단
if not (low < node.val < high): 
    return False

# 왼쪽 가문과 오른쪽 가문이 모두 참(True)이어야만 나도 참(True)이다.
return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
```

## 4. 📊 Big-O (시공간 복잡도)
* **시간 복잡도 $O(N)$:** 모든 노드($N$개)를 정확히 딱 한 번씩만 방문함.
* **공간 복잡도 평균 $O(\log N)$:** DFS 재귀 호출로 인한 콜스택 깊이. (최악의 경우 트리가 한쪽으로 쏠리면 $O(N)$)


