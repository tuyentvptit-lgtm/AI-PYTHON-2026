# Bài 15: Lọc các số lớn hơn 10 và là số chẵn
numbers = [5, 12, 7, 14, 20, 9, 11, 30]

result = [n for n in numbers if n > 10 and n % 2 == 0]
print(result)
