# 뭐지...?
#  왜지...?
#   스스로 풀었지만 왜 어쩌다 이런 생각이 난건지 모르겠다.

def sum_digits(n):
    if (n / 10) < 1:
        # 1자리 수
        return int(n % 10)

    if (n / 10) > 1:
        return int(n % 10) + sum_digits(n / 10)

print(sum_digits(1))
print(sum_digits(41))
print(sum_digits(22541))