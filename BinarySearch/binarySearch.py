def binary_search(element, some_list):
    # 코드를 작성하세요.
    first_idx = 0
    last_idx = len(some_list) - 1
    middle_idx = int((first_idx + last_idx) / 2)
    
    while(first_idx != last_idx):
        if (element < some_list[middle_idx]):
            last_idx = middle_idx
            middle_idx = int((first_idx + last_idx) / 2)
            
        if (element > some_list[middle_idx]):
            # 왜 얘만 +1을 해줘야 하는가?
            # 파이썬의 int 형변환이 버림이기 때문이다.
            # 이따우로 하면 맨 아래 케이스는 죽었다 깨나도 루프가 안풀린다.
            first_idx = middle_idx + 1
            middle_idx = int((first_idx + last_idx) / 2)

        if (element == some_list[middle_idx]):
            return middle_idx

    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))