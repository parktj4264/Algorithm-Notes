from collections import deque

class MyStack:
    def __init__(self):
        # 큐를 하나 초기화한다.
        self.q = deque()

    def push(self, x: int) -> None:
        # x를 큐에 넣고, x가 맨 앞으로 오도록 기존 요소들을 회전(Rotate)시킨다.
        # 1. 일단 내 주머니(self)의 q 맨 뒤에 새로 들어온 x를 밀어 넣는다.
        self.q.append(x)
        
        # 2. 방금 넣은 x를 맨 앞으로 보내기 위해, 
        #    기존에 있던 놈들(현재 길이 - 1)을 앞에서 뽑아서 다시 뒤로 넣는다.

        for _ in range(len(self.q) - 1):
            # 출구(앞)에서 뽑는다: self.q.popleft()
            # 뽑은 걸 입구(뒤)로 넣는다: self.q.append(...)
            # 이 두 동작을 한 줄로 합쳐서 구현해 봐!            
            self.q.append( self.q.popleft() )


    def pop(self) -> int:
        # 스택의 pop(LIFO)처럼 큐의 맨 앞 요소를 뽑아 반환한다.
        return self.q.popleft()

    def top(self) -> int:
        # 스택의 top처럼 큐의 맨 앞 요소를 확인만 하고 반환한다.
        return self.q[0]

    def empty(self) -> bool:
        # 큐가 비어있는지 여부를 반환한다.
        if len(self.q) > 0 : return False
        else: return True



if __name__ == "__main__":
    # Test Case 실행
    myStack = MyStack()
    
    print("Push 1")
    myStack.push(1)
    
    print("Push 2")
    myStack.push(2)
    
    print("Top element:", myStack.top())    # Expected: 2 (나중에 들어온 2가 맨 위에 있어야 함)
    
    print("Pop element:", myStack.pop())    # Expected: 2 (나중에 들어온 2가 먼저 나감)
    
    print("Is empty?:", myStack.empty())    # Expected: False (1이 남아있음)
    
    print("Pop element:", myStack.pop())    # Expected: 1 (마지막 남은 1 나감)
    
    print("Is empty?:", myStack.empty())    # Expected: True (다 비었음)