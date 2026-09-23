import random

so_bi_mat = random.randint(1, 10)
while True:
    doan = int(input("Đoán số (1-10): "))
    if doan == so_bi_mat:
        print("Chính xác!")
        break
    elif doan < so_bi_mat:
        print("Lớn hơn")
    else:
        print("Nhỏ hơn")
