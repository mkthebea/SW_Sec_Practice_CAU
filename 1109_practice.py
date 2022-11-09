##### File Read & Write #####

# 코드 실행할 때는 위치 중요
# 현재 경로를 다룰 수 있게 해주는 라이브러리 pathlib
from pathlib import Path

FILE = Path(__file__).resolve()  # 이 파일에 대한 path 정보 (절대 경로)
print(FILE) 
ROOT = FILE.parent  # 이 파일을 소유하고 있는 폴더
print(ROOT)

if __name__ == '__main__':
    # f = open(ROOT / 'hello.txt', 'r', encoding='utf-8')   # ROOT에 있는 hello.txt 가져오기
    # f = open(ROOT / 'hello.txt', 'w', encoding='utf-8') <- 오류 나고 hello.txt 내용 다 지워짐(읽을 수 없음, 덮어쓰기니까)
    f = open(ROOT / 'hello.txt', 'r+', encoding='utf-8')    # 그래서 write 대신 r+ 많이 씀

    print(f.writable())     # 쓸 수 있는지 (현재 r+이므로 True)

    # print(f.tell())     # 현재 커서 위치를 반환 (현재 0)
    # f.seek(5, 0)        # 커서의 위치를 시작점으로부터 5칸 옮김
    # print(f.read())     # -> hello 빼고 출력됨
    # print(f.tell())     # 커서가 맨 뒤로 이동함

    # f.seek(0, 2)    # 커서 위치 맨 뒤로 보냄
    # f.write("Write new line")   # 커서가 맨 뒤에 가 있으므로 append와 같이 동작함 (그냥 쓰면 파일 덮어씌워짐)

    # f.seek(0, 2)
    # f.write("Write new line again\n")
    # print(f.read())     # 출력 안됨 -> 쓰고 나서 커서가 맨 뒤로 이동했기 때문

    f.seek(0, 2)
    save_point = f.tell()   # 현재 커서 위치 저장
    f.write("Write new line again\n")
    f.seek(save_point, 0)   # 방금 쓴 내용 확인 가능, save_point 대신 0 쓰면 전체 출력
    print(f.read())     

    # print(f.readline())     # 한 줄씩
    # print(f.readline())
    # print(f.readline())

    # print(f.readlines())    # 한 줄씩 읽어서 리스트로

    # f.write("Write this line\n")
    # f.writelines(["Write this line\n", "Second new line\n"])


    f.close()

# with 구문
# 해당 함수의 실행 시간을 측정할 때 많이 사용: 시작시 time, 마지막 time