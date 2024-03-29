def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # start_index가 end_index보다 크면 some_list안에 element는 없다
    if start_index > end_index:
        return None
      
    # 범위의 중간 인덱스를 찾는다
    mid = (start_index + end_index) // 2
  
    # 이 인덱스의 값이 찾는 값인지 확인을 해준다
    if some_list[mid] == element:
        return mid

    # start, end로 직접 리스트에 접근하는 것이 아님
    # 그렇기 때문에 -1, +1이 꼭 있어야 한다.
    # 지금 계산하는 건 index를 계산하는거지 리스트 요소 내의 값을 계산하는 게 아니다
    # 찾는 항목이 중간 값보다 작으면 리스트 왼쪽을 탐색해준다
    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)

    # 찾는 항목이 중간 값보다 크면 리스트 오른쪽을 탐색해준다
    else:
        return binary_search(element, some_list, mid + 1, end_index)        

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))