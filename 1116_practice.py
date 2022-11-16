#### Exceptions ####
try:
    sum = "123" + 4
    print(sum)  # TypeError 발생
    div = 5/0  
    print(div)  # zero division error
# except TypeError:
#     print("str과 int는 + 연산을 할 수 없습니다.")
except Exception as e:  # 어떤 에러든 처리
    print(f"뭔가 에러가 남...{e}")

a, b = 52, 1
if b== 1:
    raise Exception("1로도 나누지 마세요")  # 파이썬에서 사전 정의된 에러 외에도 직접 exception 발생 가능
print(a/b)


# assert
a, b = 52, 2

assert b != 1, ("1로도 나누지 마세요")  # b가 1이면 에러
print(a/b)