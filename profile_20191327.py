import contextlib
import time
import random


class Profile(contextlib.ContextDecorator):
    def __init__(self, t=0.0):
        self.t = t
        self.each_t = []

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, type, value, traceback):
        self.dt = time.time() - self.start  # delta-time
        self.t += self.dt  # accumulate dt
        ### BLANK ###
        self.each_t.append(self.dt) # 각각의 실행 시간 저장


def random_string_generator(n: int):
    if n < 1:
        raise Exception('n cannot be less than 1')

    random_strs = []
    alpha_with_space = ' ' + 'abcdefghijklmnopqrstuvwxyz'
    
    for _ in range(n):
        ### 각 문장의 길이는 200~1000 사이의 임의의 값
        ### *Hint: random.randint(start, end) -> start에서 end 사이의 임의의 값을 반환
        ### BLANK ###
        str_len = random.randint(200, 1000)
        str_tem = ""
        for c in range(str_len):
            str_tem += alpha_with_space[random.randint(0, 26)]
        random_strs.append(str_tem)
        
    return random_strs


if __name__ == '__main__':
    num_of_line = 1000
    writing = Profile()

    rstrs = random_string_generator(num_of_line)

	### BLANK ###
    f = open('./write.txt', 'w', encoding='utf-8')
    for s in rstrs:
        with writing:
            f.write(s)
    f.close()
    
    avg_time = round(writing.t / num_of_line * 1E6, 4)
    wcet = round(max(writing.each_t) * 1E6, 4)

    print(f'Average execution time: {avg_time} micro second')
    print(f'Worst case execution time: {wcet} micro second')