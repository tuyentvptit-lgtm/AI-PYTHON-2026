# Bài 14: Trung bình cộng x và y trong list tuple (x, y)
points = [(1, 2), (3, 4), (5, 6)]

sum_x = 0
sum_y = 0
for x, y in points:
    sum_x += x
    sum_y += y

n = len(points)
print("Trung bình x:", sum_x / n)
print("Trung bình y:", sum_y / n)
