# 1 ile 10 arasındaki sayılarsdan olusan liste
liste = list(range(1,10))
print(liste)

#ekrana 50 defa python yazdıralım
for sayi in range(50):
    print(f"{sayi+1}.Python"),

# metot :enumerate()
#ingilizcede enumerate numaralandırmak anlamına gelir
#Fonksiyonun görevi nesne elemanlarını numaralandırarak döndürmek

#python kelimesinin karakterlerini enumerate
#ile yazdıralım
kelime = "Python"
kelime_enum = list(enumerate(kelime))
print(kelime_enum)

for index,harf in enumerate(kelime):
    print(index,harf)

# metot :zip()
#zip listeleri birleştirme işlemi yapar

#sayılardan ve o sayıların okunuşlarından oluşan 2 liste oluşturalım
sayilar = [1,2,3]
okunuslari = ["bir","iki","üç"]

#bu listeleri zipile birlestirelim
sayilar_zip = list(zip(sayilar,okunuslari))
print(sayilar_zip)