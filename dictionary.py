numaralar = [66,75]
isimler = ["Ahmed","Mehmed"]
numara = int(input("Öğrenci numarasını yazınız:"))
konum = numaralar.index(numara)
print(isimler[konum])

#numarayı bulma işlemini dictinoary ile yapalım
ogrenciler = {66: "Ahmed", 75: "Mehmed"}
# print(ogrenciler[numara])

kisiler = {
    19: {
        "ad":"eren",
        "yas":"14",
        "cinsiyet": True,
        "dersler": ["hayat bilgisi","matematik"]
    }
}
