import heapq
from typing import List, Optional

# 리트코드에서 제공하는 단일 연결 리스트 클래스
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        
        # 질문! 여기서 O(K*N_K) 만큼 쓰네? ㄴㄴ O(K)

        # 1. 각 리스트의 '첫 번째 노드(대표)'들을 힙에 넣기
        for i, node in enumerate(lists):
            if node:
                # 🚨 에러 방지용 치트키: (노드의 값, 리스트 번호 i, 노드 객체) 튜플로 넣음!
                heapq.heappush(hq, (node.val, i, node))
                
        # 정답을 이어 붙일 가짜(Dummy) 헤드 노드 하나 생성
        dummy = ListNode(0)
        curr = dummy
        
        # 2. VIP 대기실이 텅 빌 때까지 무한 반복
        while hq:
            # 2-1. 대기실에서 제일 작은 놈을 뽑기 (val, i, node 추출)
            smallest_vip = heapq.heappop(hq)
            
            # 2-2. 정답 리스트(curr)의 다음에 방금 뽑은 node를 연결하고, curr 전진시키기
            curr.next = ListNode(smallest_vip[2].val)
            curr = curr.next
            
            # 2-3. 방금 뽑힌 node에게 '다음 노드(node.next)'가 있다면?
            # 그놈을 다시 대기실(hq)에 넣어주기! (주의: 리스트 번호 i도 같이 넣어야 함)
            if smallest_vip[2].next: 
                smallest_vip_node_next = smallest_vip[2].next
                heapq.heappush(hq, (smallest_vip_node_next.val, smallest_vip[1],smallest_vip_node_next))
            
        return dummy.next




# 🎁 연결 리스트를 예쁘게 출력/생성하는 헬퍼 함수 (디버깅용)
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))



if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: [[1,4,5], [1,3,4], [2,6]]
    l1 = create_linked_list([1, 4, 5])
    l2 = create_linked_list([1, 3, 4])
    l3 = create_linked_list([2, 6])
    lists1 = [l1, l2, l3]
    
    print("TC 1 결과:")
    ans1 = sol.mergeKLists(lists1)
    print_linked_list(ans1) 
    # 예상 결과: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6