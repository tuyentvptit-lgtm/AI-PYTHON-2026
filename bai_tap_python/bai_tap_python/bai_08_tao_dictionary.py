# Bài 8: Nhập tên và tuổi 3 người, lưu vào dict {name: age}
people = {}
for i in range(3):
    name = input(f"Nhập tên người thứ {i + 1}: ")
    age = int(input(f"Nhập tuổi của {name}: "))
    people[name] = age

print(people)
