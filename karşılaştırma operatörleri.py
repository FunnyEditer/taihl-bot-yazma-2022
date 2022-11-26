"""
KARŞILAŞTIRMA OPERATÖRLERİ
//////////////////////////////////////////////////////////////////////////////
Python'da değişkenlerin içindeki verileri karşılaştırmak için kullanırız
+----------+----------------+-----------+
| Operatör | Açıklama       | Kullanımı |
+----------+----------------+-----------+
|    ==    | eşit mi?       |   x == y  |
+----------+----------------+-----------+
|    !=    | eşit değil mi? |   x != y  |
+----------+----------------+-----------+
|     >    | büyük mü?      |   x > y   |
+----------+----------------+-----------+
|     <    | küçük mü?      |   x < y   |
+----------+----------------+-----------+
|    >=    | büyük eşit mi? |   x >= y  |
+----------+----------------+-----------+
|    <=    | küçük eşit mi? |   x <= y  |
+----------+----------------+-----------+
"""

#VERİTABANI
kullanici_adi = 'ahmed'
sifre = '2143'

#kullanıcıdan bilgilerini alalım ve veritabanını temsil eden değişkenlerin eşitliğini kontrol edelim
k_kadi = input("Kullanıcı adınızı yazınız")
k_sifre = input("şifrenizi yazınız")

print(f"kullanıcı adı doğru mu : {kullanici_adi == k_kadi}")
print(f"şifre doğru mu :{sifre == k_sifre}")

#
sayi1 = int(input("1. sayı :"))
sayi2 = int(input("2. sayı :"))
print(f"Eşit değilmi : {sayi1 != sayi2}")

#iki kişinin yaşını karşılaştıralım
yas1 = 34
yas2 = 23
print("Büyük mü : " + str(yas1 > yas2))
print("Küçük mü : {}".format(yas1 < yas2))
