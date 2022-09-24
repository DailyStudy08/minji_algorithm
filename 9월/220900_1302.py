# 베스트 셀러
N = int(input())
st ={}
lst = []
for _ in range(N):
    book = input()
    lst.append(book)
    st.setdefault(book,0)
print(lst)
print(st)