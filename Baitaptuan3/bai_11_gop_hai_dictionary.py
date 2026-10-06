# Bài 11: Gộp 2 dict, trùng key thì cộng giá trị
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 10, "c": 20, "d": 30}

result = dict(d1)
for k, v in d2.items():
    if k in result:
        result[k] += v
    else:
        result[k] = v

print(result)
