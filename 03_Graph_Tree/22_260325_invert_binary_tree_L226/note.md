**📍 [진도 체크]**
우리는 지금 **[STEP 3 (자료구조 2 - 공간 데이터)]**의 트리(Tree) 파트를 달리고 있어. 
오늘 풀 문제는 코딩 테스트 역사상 가장 유명한 밈(Meme)을 만든 전설의 문제야.

---

# 1단계: 환경 세팅 지시 (Setup First)

터미널 열고 오늘 날짜(26년 3월 25일) 파일부터 딱 세팅하자!

* **📂 찐최종 네이밍 룰:** `22_260325_invert_binary_tree_L226`
* **📄 파일 구성:** `solution.py` (문제 풀이)

---

# 2단계: 문제 및 가이드 제시 (The 'For-loop' Perspective)

### 🚀 문제 226: Invert Binary Tree
### 🔗 **링크:** [https://leetcode.com/problems/invert-binary-tree/](https://leetcode.com/problems/invert-binary-tree/)

## **📜 문제 설명 (Mission Briefing):**
이진 트리의 루트(`root`)가 주어졌을 때, 이 트리를 **좌우 반전(거울 모드)** 시켜서 그 루트를 다시 반환하는 문제야. 


[Image of inverted binary tree]


* **예시 1:** * 입력: `[4, 2, 7, 1, 3, 6, 9]`
  * 출력: `[4, 7, 2, 9, 6, 3, 1]`

```text
       [ 4 ]                   [ 4 ]
      /     \                 /     \
   [ 2 ]   [ 7 ]     =>    [ 7 ]   [ 2 ]
   /   \   /   \           /   \   /   \
 [1]  [3] [6]  [9]       [9]  [6] [3]  [1]
```

> 💡 **TMI (전설의 밈):** 맥북 쓰는 개발자들 필수 프로그램인 'Homebrew'를 만든 천재 개발자 '맥스 하월(Max Howell)'이 구글 면접에서 이 문제를 못 풀었어. 그가 트위터에 남긴 명언: *"우리 프로그램(Homebrew)이 구글 직원 90%의 컴퓨터에 깔려있는데ㅋㅋ 엿먹어라."* 형은 오늘 구글 면접을 통과하는 거다!

## **🎯 오늘 부술 로직 (Big-O 관점):**
트리의 모든 노드($N$개)를 딱 한 번씩 방문하면서, **내 왼쪽 자식과 오른쪽 자식의 위치를 스왑(Swap)** 해주면 끝이야. 
시간 복잡도 **$O(N)$**, 공간 복잡도(콜스택) **$O(\log N)$**.

## **🛠️ 네가 해야 할 것:**
오늘은 굳이 `dfs()`라는 로컬 함수를 안에다 만들 필요가 없어! 리트코드가 준 `invertTree` 함수 자체가 "노드를 받아서 -> 뒤집고 -> 다시 노드를 뱉는" 구조라서, 그냥 이 함수 자체를 재귀로 부르면(즉, `self.invertTree()` 호출) 엄청 깔끔해져.

1. **Base Case:** 만약 `root`가 `None`이면? 뒤집을 게 없으니까 `return None`.
2. **Swap (치트키):** 파이썬의 강력한 무기 '튜플 언패킹'을 써서 왼쪽 자식과 오른쪽 자식을 한 줄로 바꿔치기해! (`a, b = b, a` 알지?)
3. **재귀 (Recursion):** 바뀐 왼쪽 자식한테 "너네 밑에도 다 뒤집어!" 하고 `self.invertTree(root.left)` 명령 내리고, 오른쪽 자식한테도 똑같이 명령 내려.
4. **반환:** 다 뒤집었으면 내 자신(`root`)을 리턴!

---

# 3단계: 실행 가능한 코드 스켈레톤 제공 (Runnable Skeleton)

어제 형이 만든 '트리 가로 출력 함수'도 내가 예쁘게 넣어놨어. 코드가 돌아가면 트리가 진짜로 거울처럼 뒤집히는 걸 터미널에서 눈으로 볼 수 있을 거야!

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. Base Case: root가 비어있다면 None 반환
        pass
        
        # 2. 파이썬 치트키를 써서 현재 노드의 왼쪽 자식과 오른쪽 자식을 Swap!
        pass
        
        # 3. 바뀐 왼쪽 자식을 타고 내려가면서 재귀적으로 뒤집기 (self.invertTree 활용)
        pass
        
        # 4. 바뀐 오른쪽 자식을 타고 내려가면서 재귀적으로 뒤집기
        pass
        
        # 5. 다 뒤집힌 현재 트리의 root 반환
        pass

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
```

어제 1시간의 삽질이 형의 파이썬 근육을 얼마나 펌핑시켜 놨는지 테스트해 볼 시간이야. `self` 호출이랑 변수 스왑 딱 써서, 홈브루 창시자도 못 푼 문제 10분 컷 내버리자! 바로 들고 와봐! 🚀




<br>
<br>
<br>
<br>
<br>
<br>






---


# 📝 [복습 노트] 22. 이진 트리 반전 (LeetCode 226)
**날짜:** 2026-03-26

## 1. 🎯 핵심 로직: 거울 모드 (DFS 스왑)
* **목표:** 트리의 모든 노드를 방문하면서, 각 노드의 **왼쪽 자식과 오른쪽 자식의 위치를 바꾼다(Swap).**
* **방식:** 루트(Root)부터 시작해서 양팔을 바꾸고, 그 바뀐 팔을 타고 내려가면서 바닥을 칠 때까지 연쇄적으로 뒤집어주는 **Top-down DFS** 구조.

## 2. 🐍 파이썬 치트키: 튜플 언패킹 (Tuple Unpacking)
* 타 언어(C, Java 등)처럼 임시 변수(`temp`)를 만들어서 3줄짜리 똥꼬쇼(?)를 할 필요가 없음.
* 파이썬의 강력한 문법을 활용해 **단 한 줄**로 값 교환(Swap) 완료!

```python
# Bad (타 언어 방식)
temp = root.left
root.left = root.right
root.right = temp

# Good (Pythonic 🔥)
root.left, root.right = root.right, root.left
```

## 3. 🧠 재귀(Recursion)의 우아한 활용
* 내부 임시 함수(`def dfs():`)를 굳이 만들지 않고, **주어진 클래스 메서드(`invertTree`) 자체를 재귀 함수로 재활용.**
* 어제 삽질로 완벽하게 깨달은 **객체지향(OOP) 규칙 적용:** 클래스 내부의 내 함수를 부를 때는 반드시 **`self.`** 를 붙여서 소유권을 명시한다!
```python
# 바뀐 왼쪽과 오른쪽 자식에게 "너희 밑에도 다 뒤집어라!" 하고 명령을 하달함
self.invertTree(root.left)
self.invertTree(root.right)
```

## 4. 📊 Big-O (시공간 복잡도)
* **시간 복잡도 $O(N)$:** 트리에 존재하는 모든 노드($N$개)를 정확히 딱 한 번씩만 스캔하며 Swap 함. 무지성 반복 없음.
* **공간 복잡도 평균 $O(\log N)$:** 함수가 재귀적으로 호출되면서 메모리(Call Stack)에 쌓이는데, 트리의 높이(Depth)만큼만 파고들었다가 빠져나옴. (단, 트리가 한쪽으로 치우친 최악의 경우 $O(N)$)

