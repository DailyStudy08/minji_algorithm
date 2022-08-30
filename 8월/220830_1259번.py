# 팰린드롬수
# 앞뒤가 똑같은 숫자인지 아닌지 구분하는 문제!
num =input()
while num != '0':
    if num == 0:
        break

    if num == num[::-1]:
        print('yes')
    else:
        print('no')
    num = input()
