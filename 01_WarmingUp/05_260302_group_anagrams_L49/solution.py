import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. 빈 리스트를 기본값으로 갖는 defaultdict 생성
        
        # 2. strs를 for문으로 하나씩 돌면서:
        #    - 단어를 알파벳 순으로 정렬해서 Key로 만듦 ("".join(sorted(...)))
        #    - 딕셔너리의 해당 Key에 원래 단어를 append
        
        # 3. 딕셔너리의 value들만 리스트로 묶어서 반환 (dict.values() 활용)

        key_dict = collections.defaultdict(list)

        for str in strs:
            key_str = "".join(sorted(str))
            key_dict[key_str].append(str)

        results_list = key_dict.values()

        return results_list

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    print("Test 1:", sol.groupAnagrams(strs1))
    # 예상 출력: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] (순서는 달라도 됨)

    # Test Case 2
    strs2 = [""]
    print("Test 2:", sol.groupAnagrams(strs2))
    # 예상 출력: [[""]]

    # Test Case 3
    strs3 = ["a"]
    print("Test 3:", sol.groupAnagrams(strs3))
    # 예상 출력: [["a"]]