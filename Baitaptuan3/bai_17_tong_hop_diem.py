# Bài 17: Tổng hợp điểm theo tên
data = [
    {"name": "A", "score": 7},
    {"name": "B", "score": 9},
    {"name": "A", "score": 8},
]

result = {}
for item in data:
    name = item["name"]
    if name not in result:
        result[name] = []
    result[name].append(item["score"])

for name, scores in result.items():
    print(f"{name}: {scores}")
