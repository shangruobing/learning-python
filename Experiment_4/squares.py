squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
# 列表解析
square = [value ** 2 for value in range(1, 11)]
print(square)
