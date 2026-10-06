# Bài 13: Giao, hợp, hiệu của hai set
# Nhập các số cách nhau bởi dấu cách, ví dụ: 1 2 3 4
s1 = set(map(int, input("Nhập set 1: ").split()))
s2 = set(map(int, input("Nhập set 2: ").split()))

print("Giao (s1 & s2):", s1 & s2)
print("Hợp  (s1 | s2):", s1 | s2)
print("Hiệu (s1 - s2):", s1 - s2)
