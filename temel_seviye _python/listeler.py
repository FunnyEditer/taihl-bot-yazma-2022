#Bos bir liste tanımlayalım
liste = []
print(liste)
print(type(liste))

okul = "Sancaktepe aihl"
kelimeler = okul.split()
print(kelimeler)

#Belirli sıradaki kelimleri yazdıralım
print(kelimeler[0])#ilk kelime
print(kelimeler[1])
print(kelimeler[-1]) #son kelime
ad = "Eren Mustafa Özdal"
print(ad[0])  # E
print(ad[5:12])  # Mustafa
print(ad[5:12:2])  # Msaa
print(ad[-7:-14:-1])  # afatsuM
print(ad[::-1])  # ladzÖ afatsuM nerE


#listeler içerisinde farklı elemanlar olabir
liste = [1,12.3,"Python",True,[1,2,3]]
print(liste[-1][-1])
print(liste[4][-1])

# İki listeyi birleştirme
liste2 = [1, 2, 3]
liste3 = [4, 5, 6]
liste4 = liste2 + liste3
liste5 = liste3 + liste2
print(liste4)
print(liste5)