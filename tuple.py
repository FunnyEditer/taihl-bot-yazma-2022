liste = [1,2,3]
tuple = ("bir","iki","üç")

#tuple'ı ekrana yazıralım
print(liste)
print(type(liste))
print(tuple)
print(type(tuple))

#beleirli bir elemanı ekrana yazdıralım
print(tuple[0])

#listenin ve tuple'ın bir elemanın değiştirelim
liste[0] = 7
print(liste)
# 👇 TypeError: 'tuple' object does not support item assignment
# tuple[0] = "yedi"  hata verdi
# print(tuple)

#tuple içindeki beirli bir elemanının indexini bulalım index()
print(tuple.index("iki"))

#tuple'ı birleştirelim
tuple1 = (1,2,3)
tuple2 = "bir","iki","üç"
print(tuple1+tuple2)