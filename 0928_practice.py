import copy
#-------------------------------------------------------------------------------------------------------------------- 
# 저번 시간 복습

# sample_list = [2,4,8]
# sample_list = list([2,4,8])도 같음

# Delete: del sample_list[index]

# list는 변경 가능한 특성(mutable) -> 문제 발생 가능
sample_list = [2,4,8,16]
other_list = sample_list
other_list[0] = 0
print(sample_list)
# => [0,4,8,16]이 출력됨!
# 배열을 변수에 할당할 경우 값이 할당되는게 아니라 해당 위치를 가리키게 됨 (포인터 개념)

# 해결법
other_list_1 = copy.deepcopy(sample_list)   # slowest
other_list_2 = list(sample_list)
other_list_3 = sample_list[:]   # fastest

# tuple: 변경 불가능
sample_tuple = (2,4,8)

# set: 중복이 없는 배열, 단 순서를 보장하지 않음
# 특정 인덱스의 값에 접근 X
sample_set = {2,4,8,2,10}
print(sample_set)   # {8, 2, 10, 4}
sample_set.add(5)
sample_set.remove(10)
#-------------------------------------------------------------------------------------------------------------------- 
