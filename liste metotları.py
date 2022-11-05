sayilar = [1,2,6,8,6]
harfler = ["t","f","d","g","h","k","u","s","a"]

#listelerin eleman sayısını bulalım len(liste)
print(len(sayilar))
print(len(harfler))

#listenin içindeki en küçük değeri yazdır min()
print(min(sayilar))
print(min(harfler))

#listenin en büyük elemanını bulalım
print(max(sayilar))
print(max(harfler))

#sayılardan olan listeleri birleştirelim en büyüğünü bulalım
birlesmis = sayilar + harfler
#TypeError hatası verdi int ile str karşılaştıralamaz

#listenin sonuna eleman ekleyelim append()
sayilar.append(95)
#print(sayilar)

#listenin istediğimiz konumuna yeni eleman ekleyelim insert()
harfler.insert(3,"b")
print(harfler)

#listenin sonundaki elemanı silelim pop()
harfler.pop()
print(harfler)
harfler.pop(3) #belirli bir konumu sil
print(harfler)

#listede belirli elemanları silelim remove("deger")
harfler.append("a")
print(harfler)
harfler.remove("a")
print(harfler)

#listedeki elemanları sıralayalım sort()
print(sayilar)
sayilar.sort() #artan sıralama yapar
# print(sayilar)
sayilar.sort(reverse=True)  # azalan sıralama yapar
# print(sayilar)
# print("-"*50)  # ayıraç
# print(harfler)
harfler.sort()  # artan sıralama yapar
# print(harfler)
harfler.sort(reverse=True)  # azalan sıralama yapar
# print(harfler)


#listedeki ismleri alfabetik sıraya
isimler = ["Eren", "Ersin", "Ahmet", "Kaan", "Kemal", "Hüseyin"]
isimler.sort()
# print(isimler)

# listeyi temizleyelim: clear()
isimler.clear()
print(isimler)