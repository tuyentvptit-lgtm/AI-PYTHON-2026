# Bài 18: Gộp quantity của các SKU trùng nhau
items = [("A01", 5), ("B02", 3), ("A01", 2), ("C03", 7), ("B02", 4)]

totals = {}
for sku, qty in items:
    totals[sku] = totals.get(sku, 0) + qty

result = list(totals.items())
print(result)
