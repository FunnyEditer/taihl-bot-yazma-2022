okul =  "sancaktepe TEKNO"

#tum karakteleri buyuk yapalım
print(okul.upper())

#her kelimenin ilk harfini buyuk yapalım lower()
print(okul.lower())

#her kelimenin ilk harfini buyuk yapalım title()
print(okul.title())

#ilk harf buyuk digerleri kucuk capitalize()
print(okul.capitalize())

#bir ifadenin kac tane yer aldıgını bulalım count()
makale = "hep birlikte olmak ister"
print(makale.lower().count("e"))

#soldaki ve sagdaki bosluk karakterlerini temizlemeye yarar strip()
ad = input("Adınız: ")
print(ad + "|")
print(ad.strip() + "|" )

#soldakı ve sagdakı karakterlerini siler strip(ifade)
urun_kodu = "HEP20221022"
print(urun_kodu.strip("HEP"))

#soladaki boşluk veya belirli ifadeyi temizleyelim lstrip()
print(ad +"|" )
print(ad.lstrip()+ "|")
print(urun_kodu.lstrip("HEP"))

#sagdaki boslugu veya karakteri silmemizi saglar rstrip()
print(ad+"|") # adı boslukla gonderelim
print(ad.rstrip()+"|")
print(urun_kodu.rstrip("HEP"))

# Karakter dizisini bölelim: split()
print(makale.split("."))
print(okul.split())

# Böldüğümüz ve listeye dönüşen ifadeleri birleştirelim: join()
kelimeler = okul.split()
print(kelimeler)
print("---".join(kelimeler))

# Ortalayıp çıktı verme: center()
print("Eren".center(25, "-"))