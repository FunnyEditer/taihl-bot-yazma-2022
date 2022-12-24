"""
break döngüyü solandırır
continue turu sonlandırır
"""
# 0 dan 10 kadar olan sayıları beş hariç ekrana yazdıralım

for sayi in range(10):
    if sayi == 5:
        continue
    print(sayi)

# 0 dan 10 kadar sayışları ekrana yazdıralım ama 5 e gelince döngü bitsin
for sayi in range(10):
    if sayi == 5:
        break
    print(sayi)
# 1 den 100e kadar olan tek saıyalrı ekrana yazdır
for sayi in range(1,100):
    if sayi %2 == 0:
        continue
    print(sayi)

