a = int(input("정수를 입력하세요[가로] : "))
b = int(input("정수를 입력하세요[세로] : "))

i = j = 1

# 기본형 ( 가로 입력받고, 세로 입력받은 뒤 사각형 출력하기 )
for i in range(b):
    for j in range(a):
        print("*", end="")
        j += 1

    print("")
    i += 1
