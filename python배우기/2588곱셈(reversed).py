first_num = int(input())
second_num = list(map(int, input()))
reverse_second_num = second_num[::-1]
# print(reverse_second_num)
result = 0
squ_ = 0

for i in reverse_second_num:
    print(first_num * i)
    result = result + first_num * i * 10**squ_
    # print(squ_, result, 10**squ_)
    squ_ += 1

print(result)