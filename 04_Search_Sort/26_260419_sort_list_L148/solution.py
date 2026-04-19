from typing import Optional

# LeetCode에서 제공하는 연결 리스트 노드 클래스
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Base condition: 노드가 없거나 1개면 이미 정렬된 상태이므로 반환
        if not head or not head.next:
            return head
        
        # 2. 런너 기법으로 중간 노드 찾기 (리스트 반갈죽)
        # TODO: half, slow, fast 포인터를 이용해 리스트를 두 동강 내기
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        half = slow.next
        slow.next = None

        # 3. 분할된 리스트를 재귀적으로 정렬
        # TODO: left = self.sortList(head), right = self.sortList(half)
        left = self.sortList(head)
        right = self.sortList(half)

        
        # 4. 정렬된 두 리스트를 병합 (Merge)
        # TODO: 별도의 merge 함수를 만들거나 안에서 병합하여 반환
        
        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next    
            
            curr = curr.next

        curr.next = left or right

        return dummy.next





# -------------------------------------------------------------
# 로컬 테스트용 헬퍼 함수들 (LeetCode 환경 모방)
# -------------------------------------------------------------
def build_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def print_linked_list(head):
    res = []
    curr = head
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(res) if res else "Empty")




if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: 기본 정렬 안 된 케이스
    head1 = build_linked_list([4, 2, 1, 3])
    print("Input 1:")
    print_linked_list(head1)
    print("Output 1:")
    print_linked_list(sol.sortList(head1))
    print("-" * 30)
    
    # Test Case 2: 음수 포함 및 홀수 개수
    head2 = build_linked_list([-1, 5, 3, 4, 0])
    print("Input 2:")
    print_linked_list(head2)
    print("Output 2:")
    print_linked_list(sol.sortList(head2))
    print("-" * 30)
    
    # Test Case 3: 엣지 케이스 (빈 리스트)
    head3 = build_linked_list([])
    print("Input 3:")
    print_linked_list(head3)
    print("Output 3:")
    print_linked_list(sol.sortList(head3))
    print("-" * 30)
    
    # Test Case 4: 엣지 케이스 (이미 정렬된 리스트)
    head4 = build_linked_list([1, 2, 3, 4, 5])
    print("Input 4:")
    print_linked_list(head4)
    print("Output 4:")
    print_linked_list(sol.sortList(head4))