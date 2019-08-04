"{}".format(10)
"{} {}".format(10,20)
"{} {} {} {}".format(10,20, 30, 40)

string_a = "{}".format(10)
int(string_a)
print(string_a)
print(type(string_a))

format_a = "{}만 원".format(5000)
print(format_a)

#정수를 특정 칸에 출력하기
output_a = "{:d}".format(52)

#특정 칸에 출력
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_e)



# 기호와 함께 출력
output_f = 