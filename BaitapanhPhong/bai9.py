kwh = float(input("Nhập số kWh tiêu thụ: "))
if kwh <= 50:
    tien = kwh * 1800
elif kwh <= 100:
    tien = 50 * 1800 + (kwh - 50) * 2000
else:
    tien = 50 * 1800 + 50 * 2000 + (kwh - 100) * 2500
print(f"Tổng tiền điện: {tien} đ")
