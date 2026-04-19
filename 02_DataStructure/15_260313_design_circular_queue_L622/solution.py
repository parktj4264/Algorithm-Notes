class MyCircularQueue:
    def __init__(self, k: int):
        # 최대 크기 k와 고정 배열을 초기화해.
        self.k = k
        self.q = [None] * k
        # 투 포인터(인덱스)와 현재 크기(size)를 추적할 변수들을 만들어봐.
        self.front = 0
        self.rear = -1 # (혹은 -1로 시작해도 됨, 본인 논리에 맞게 세팅)
        self.size = 0

    def enQueue(self, value: int) -> bool: #질문!! return이 bool인 이유!??
        # 꽉 찼으면 False 반환
        # 아니면 rear 위치에 값을 넣고, rear 인덱스를 1칸 전진(모듈로 연산!)
        
        if None not in self.q:
            return False
        
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value
        
        
        return True
    
    
    def deQueue(self) -> bool:
        # 비었으면 False 반환 -> 이거도 왜 bool로 return 굳이 하는거??
        # 아니면 front 위치의 값을 빼고(None 처리 등), front 인덱스를 1칸 전진(모듈로 연산!)
        
        if self.q == [None] * self.k: 
            return False
        
        self.q[self.front] = None
        self.front = (self.front + 1) % self.k
        
        return True
        

    def Front(self) -> int:
        # 비었으면 -1 반환, 아니면 front 위치의 값 반환
        
        if self.q[self.front] == None: 
            return -1
        
        return self.q[self.front] # ㅋㅋ 먼가 비효율적으로보이네
    
        

    def Rear(self) -> int:
        # 비었으면 -1 반환, 아니면 가장 최근에 삽입된 위치의 값 반환
        
        if self.q[self.rear] == None: 
            return -1
        
        return self.q[self.rear]
        
        
        

    def isEmpty(self) -> bool:
        # 현재 사이즈가 0인지 체크
        
        if self.q == [None] * self.k: 
            return True
        
        return False
    
    def isFull(self) -> bool:
        # 현재 사이즈가 k인지 체크
        
        if None not in self.q: 
            return True
        return False
    
    
    


if __name__ == "__main__":
    print("=== 원형 큐 테스트 시작 ===")
    cq = MyCircularQueue(3)  # 크기가 3인 원형 큐 생성
    
    print("enQueue 1:", cq.enQueue(1))  # Expected: True
    print("enQueue 2:", cq.enQueue(2))  # Expected: True
    print("enQueue 3:", cq.enQueue(3))  # Expected: True
    print("enQueue 4 (Full):", cq.enQueue(4))  # Expected: False (꽉 참)
    
    print("Rear element:", cq.Rear())  # Expected: 3
    print("isFull?:", cq.isFull())     # Expected: True
    
    print("deQueue:", cq.deQueue())    # Expected: True (1번 요소 빠짐, 공간 생김!)
    print("enQueue 4:", cq.enQueue(4))  # Expected: True (남은 공간에 4가 들어감)
    
    print("Rear element:", cq.Rear())  # Expected: 4