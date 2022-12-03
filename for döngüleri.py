#öğrenci isimlerinden oluşan bir liste oluşturalım
ogrenciler = ["mahmud","semih","ayşe"]

#her öğrencinin adını ekrana yazdıralım
for ogrenci in ogrenciler:
    print(f"Öğrencinin adı: {ogrenci}")

# içinde ikili sayı olan tuple yapalım
sayilar = [(1,2),(2,3),(3,4)]
for a,b in sayilar:
    print(f"1.sayı: {a},2.sayı: {b}")
# okulumuzn yer aldığı değişkeni kelimelere bölüp her kerlimeyi döngü içinde yazdıralım
okul = "Sancaktepe TAİHL"
for kelime in okul.split():
    print(kelime)
# öğrencilerin yer aldığı dict oluşturalım
ogrenciler= {
    1: {
        "ad": "Eren",
        "soyad": "Özdal",
        "cinsiyet": True,
        "dersler": ["Türkçe", "Matematik", "Hayat Bilgisi"]
    },
    45: {
        "ad": "Zeynep",
        "soyad": "Özdal",
        "cinsiyet": False,
        "dersler": ["Görsel Sanatlar", "Matematik", "Fen Bilimleri"]
    }
}

for no, ogrenci in ogrenciler.items():
    print(f"{no} numaralı öğrenci: {ogrenci['ad']}")