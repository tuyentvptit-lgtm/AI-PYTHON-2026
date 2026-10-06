# Bài 9: Loại phần tử trùng nhưng giữ thứ tự (không dùng set)
a = [1, 2, 2, 3, 1]

result = []
for x in a:
    if x not in result:
        result.append(x)

print(a, "->", result)
