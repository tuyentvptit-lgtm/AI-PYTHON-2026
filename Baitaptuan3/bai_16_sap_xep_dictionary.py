# Bài 16: Sắp xếp dict theo điểm giảm dần
scores = {"An": 8.5, "Bình": 9.0, "Chi": 7.0, "Dũng": 9.5}

sorted_items = sorted(scores.items(), key=lambda item: item[1], reverse=True)

for name, score in sorted_items:
    print(f"{name}: {score}")
