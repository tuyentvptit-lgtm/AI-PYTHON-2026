# Bài 12: Dictionary đếm tần suất ký tự
s = input("Nhập một chuỗi: ")

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch, c in freq.items():
    print(f"'{ch}': {c}")
