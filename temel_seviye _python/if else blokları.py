"""
if ve else blokları ile mantıksal operatörler kullanılarak
programın akışı değiştirilebilir
"""
#kullanıcıdan iki sayı alalım
sayi1 = int(input("1. sayıyı girin:"))
sayi2 = int(input("2. sayıyı girin:"))
#hangidinin büyk olduğunu yazdıralım
if sayi1 > sayi2:
    print(f"1.sayı: ({sayi1}), 2.sayıdan ({sayi2}) büyüktür.")

else:
    print(f"2.sayı ({sayi2}),1.sayıdan ({sayi1})büyüktür.")