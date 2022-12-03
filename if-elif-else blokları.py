"""
Python'da bazen birden fazla koşul ifadeleri yazmak isteyebiliriz.
Bu koşulları ilk "if" bloğundan sonra istenilen kadar "elif" ifadeleri
ile yeni bloklar oluşturarak ekleleyebiliriz.
Her bloktan dönen "False" sonucu, alttaki "elif" bloğunu tetikler.
"""
#kullanıcıdan iki sayı alalım
sayi1 = int(input("1. sayıyı girin:"))
sayi2 = int(input("2. sayıyı girin:"))
#hangidinin büyük veya eşit olduğunu yazdıralım
#ör 1. sayı 2.sayıya eşittir
if sayi1 > sayi2:
    print(f"1.sayı: ({sayi1}), 2.sayıdan ({sayi2}) büyüktür.")

elif sayi2 > sayi1:
    print(f"2.sayı: ({sayi2}), 1.sayıdan ({sayi1}) büyüktür.")

else:
    print(f"1.sayı: ({sayi1}), 2.sayıya ({sayi2}) eşittir.")

