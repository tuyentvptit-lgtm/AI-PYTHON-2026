# Bài 10: Tìm phần tử xuất hiện nhiều nhất
numbers = [1, 3, 2, 3, 4, 3, 2, 1, 2, 3]

count = {}
for n in numbers:
    count[n] = count.get(n, 0) + 1

best = numbers[0]
for k in count:
    if count[k] > count[best]:
        best = k

print("Phần tử xuất hiện nhiều nhất:", best, f"({count[best]} lần)")
