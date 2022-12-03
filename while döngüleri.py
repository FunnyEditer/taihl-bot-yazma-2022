#0 dan yüze kadar olan sayıları yazdıralım
# sayi = 0
# while sayi < 100:
#
#     if sayi % 2 == 0:
#         print(f"{sayi} çift sayı")
#     else:
#         print(f"{sayi} tek sayıdır")
#
#     sayi += 1

# excel okuma modülünü içeri aktaralım
import xlrd

# excel dosyasını açalım
ck = xlrd.open_workbook("veriler/WorldCupPlayers.xls")

#excel çalışma sayfasını alalım
cs = ck.sheet_by_index(0)

# toplam satır ve sütun sayılarını alalım
satir_sayisi = cs.nrows
sutun_sayisi = cs.ncols
print(f"Satır sayısı: {satir_sayisi}")
print(f"Sütun sayısı: {sutun_sayisi}")

#ilk başlık satırını okuyalım
a1 = cs.cell(0,0)
print(a1)

# tüm futbolcuların ismini yazdıralım
satir = 1 #1. indeksten başlıyoruz
while satir < satir_sayisi:
    futbolcu = cs.cell_value(satir,6)
# if futbolcu.startswith("R"):  # R harfi ile başlayan futbolcular
    #     print(f"Futbolcu: {futbolcu}")

    # Bir olaya yaşamış futbolcular yazdıralım
    olay = cs.cell_value(satir, 8)
    if olay != "":
        print(f"Futbolcu: {futbolcu} - Olay: {olay}")

    satir += 1


