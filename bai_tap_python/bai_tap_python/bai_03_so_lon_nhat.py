# Bài 3: Tìm phần tử lớn nhất (không dùng max())
numbers = [4, 17, 9, 25, 3, 12]

largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n

print("List:", numbers)
print("Số lớn nhất:", largest)
