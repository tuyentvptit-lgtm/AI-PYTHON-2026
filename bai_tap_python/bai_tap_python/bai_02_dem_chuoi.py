# Bài 2: Đếm số lần xuất hiện của một chuỗi
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
target = input("Nhập chuỗi cần đếm: ")

count = 0
for w in words:
    if w == target:
        count += 1

print(f"'{target}' xuất hiện {count} lần")
