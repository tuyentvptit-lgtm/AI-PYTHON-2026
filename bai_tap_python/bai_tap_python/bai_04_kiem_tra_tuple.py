# Bài 4: Kiểm tra giá trị có nằm trong tuple không
data = (1, 5, 9, 12, 20)
x = int(input("Nhập giá trị cần kiểm tra: "))

if x in data:
    print(f"{x} CÓ trong tuple {data}")
else:
    print(f"{x} KHÔNG có trong tuple {data}")
