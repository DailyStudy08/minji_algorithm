# 단어 수학
N = int(input())
alphabets = []
alpha_dict = {}

for _ in range(N):
    alphabets.append(input().rstrip())

for alphabet in alphabets:
    square_root = len(alphabet) - 1
    for char in alphabet:
        if char in alpha_dict:
            alpha_dict[char] += pow(10, square_root)
        else:
            alpha_dict[char] = pow(10, square_root)        
        square_root -= 1

alpha_dict = sorted(alpha_dict.values(), reverse=True)
result, _max = 0, 9
for i in alpha_dict:
    result += i * _max
    _max -= 1
print (result)
# 계속 시도했는데 안되스 구글링 했습니다.. 내일 다시 풀어보겠습니다 ㅠ