# Bài 19: Tìm cặp phần tử có tổng gần N nhất
numbers = [1, 4, 7, 10, 15, 22]
N = int(input("Nhập N: "))

best_pair = None
best_diff = None

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        diff = abs(numbers[i] + numbers[j] - N)
        if best_diff is None or diff < best_diff:
            best_diff = diff
            best_pair = (numbers[i], numbers[j])

print("Cặp gần nhất:", best_pair, "- tổng =", sum(best_pair))
