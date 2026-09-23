n = int(input("Nhập số lượng số: "))
dem = 0
for i in range(n):
    so = int(input(f"Nhập số thứ {i + 1}: "))
    if so % 2 == 0:
        dem += 1
print(f"Có {dem} số chẵn")
