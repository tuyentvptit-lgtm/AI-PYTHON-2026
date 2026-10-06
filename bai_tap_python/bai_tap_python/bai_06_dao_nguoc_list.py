# Bài 6: Đảo ngược list thủ công (không dùng reverse() hay [::-1])
a = [1, 2, 3, 4, 5]
print("Trước:", a)

left, right = 0, len(a) - 1
while left < right:
    a[left], a[right] = a[right], a[left]  # hoán đổi
    left += 1
    right -= 1

print("Sau:  ", a)
