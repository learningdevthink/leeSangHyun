pi = 3.14159
pi
pi + 2
pi - 2
pi * pi

# 변수 선언
pi = 3.14159265
r = 10

# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2*pi*r)
print("원의 넓이 =", pi*r*r)

# 사용자 입력 받기
input("인사말 입력해라 >")

string = input("인사말 써봐 >")
print(string)


# 인풋으로 받은 데이터는 무조건 데이터타입이 str
# str을 int로 변환해야만 하고  그건 int()처리 하믄 된다
string_a = input("입력 A > ")
int_a = int(string_a)

string_b = input("입력 B >")
int_b = int(string_b)

print("문자열 자료 : ", string_a + string_b)
print("숫자열 자료 : ", int_a + int_b)

input_a = float(input("첫 번째 숫자"))
input_b = float(input("두 번째 숫자"))

# 연습문제
str_input = input("원의 반지름 입력 >")
num_input = float(str_input)
type(num_input)
print()
print("반지름 =", num_input)
print("둘레 : ", 2 * 3.14 * num_input)

# 연습문제 6번
a = input("문자열 입력 >")
b = input("문자열 입력 > ")

print(a, b)
c = b
d = a
print (c,d)


