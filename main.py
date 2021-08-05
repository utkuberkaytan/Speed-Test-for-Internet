'''

Speed Test for Internet - v1.0

Apache Lisance 2.0

Created by Utku Berkay TAN

'''

import speedtest

s = speedtest.Speedtest()

def durum(ping):
    durum = "Hata - Ölçülemedi"
    if(ping <= 10):
        durum = "Çok İyi!"
    elif(ping > 10 and ping <= 50):
        durum = "İyi!"
    elif(ping > 40 and ping <= 100):
        durum = "Kötü!"
    elif(ping > 100):
        durum = "Çok Kötü!"
    return durum
def oneri(downloadspeed, uploadspeed, situation):
    oneri = "Hata"
    if(downloadspeed <= 10 and uploadspeed <= 5):
        oneri = "İnternet Tarifenizi Veya İnternet Sağlayıcınızı Değiştirmeyi Deneyin."
    elif(downloadspeed > 10 and uploadspeed <= 5 or uploadspeed > 5):
        if(situation == "Kötü!" or situation == "Çok Kötü!"):
            oneri = "Fiziksel Konumunuzu Değiştirmeyi Deneyin."
        else:
            oneri = "Sorun Yok Gibi Görünüyor :)"
    return oneri



print("Test Yapılıyor...")
print(" ")

indirmehızı = s.download() / 1048576
yuklemehızı = s.upload() / 1048576
ping = round(s.results.ping)

internetdurumu = durum(ping=ping)
internetonerisi = oneri(downloadspeed=indirmehızı, uploadspeed=yuklemehızı, situation=internetdurumu)

print(f"İndirme Hızı: {indirmehızı:.2f} Mbps")
print(f"Yükleme Hızı: {yuklemehızı:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")
print(" ")
print(f"İnternet Durumu: {internetdurumu}")
print("Not: İnternet durumu pinge göre hesaplanır.")
print(" ")
print(f"Önerimiz(Beta): {internetonerisi}")

input()
