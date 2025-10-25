# Döngüde i değerlerini yazdırma

i = 0
while i < 10:
    print("i değeri", i)
    i += 1

# Kullanıcıdan alınan sayıdan 1'e kadar geriye sayma

sayı = int(input("Bir sayı girin:"))
while sayı >= 1:
    print(sayı)
    sayı -= 1

print("Geri sayım tamamlandı!")

# Kullanıcıdan alınan sayıların çarpımının hesaplanması

prduct = 1
count = 0
while count < 5:
    sayı = int(input("Bir sayı girin:"))
    prduct *= sayı
    count += 1
print("Çarpım:", prduct)

# Şifre doğrulama

şifre = "4321"
giriş = ""
while giriş != şifre:
    giriş = input("Şifrenizi girin:")
print("Şifre doğru, giriş yapıldı!")
