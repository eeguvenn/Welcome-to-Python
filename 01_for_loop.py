# Range fonksiyonu ile 0'dan 10'a kadar sayıları yazdırma

for i in range(11):
    print("Sayı: {}" .format(i))

# Liste elemanlarını tek tek yazdırma

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like {}".format(fruit))

# Listedeki sayıların toplamını hesaplama

toplam = 0
liste = [1, 2, 3, 4, 5, 6, 7, 8]
for sayı in liste:
    toplam += sayı
print("Toplam: {}".format(toplam))

# Listedeki sayıların ve elemanlarının yazdırılması

toplam = 0
liste = [1, 2, 3, 4, 5, 6, 7, 8]
for sayı in liste:
    toplam += toplam + sayı
    print("toplam: {} sayı {} ".format(toplam, sayı))
print(toplam)


# Çift ve tek sayıları ayırma

liste = [2, 5, 13, 23, 12, 17, 65, 77, 80, 72]
for eleman in liste:
    if eleman % 2 == 0:
        print("{} sayısı çifttir".format(eleman))
    else:
        print("{} sayısı tektir".format(eleman))

# Her bir karakterği çarpılarak yazdırma

s = "deneme"
for karakter in s:
    print(karakter*2)

# Matris içindeki elemanların çarpımı

liste = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for (i, j, k) in liste:
    print(i*j*k)
