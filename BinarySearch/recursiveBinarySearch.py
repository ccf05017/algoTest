def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.
    # 중간 포인터 계산
    middle_idx = (start_index + end_index) // 2

    # 예외 케이스
    if (start_index == end_index):
        if (element == some_list[middle_idx]):
            return middle_idx
        else:
            return None
    
    # 실제 recursive logic
    # base case
    if (element == some_list[middle_idx]):
        return middle_idx

    # recursive case
    elif (element < some_list[middle_idx]):
        return binary_search(element=element,
            some_list=some_list,
            start_index = 0,
            end_index = middle_idx)

    elif (element > some_list[middle_idx]):
        return binary_search(element=element,
            some_list=some_list,
            start_index = middle_idx + 1)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))