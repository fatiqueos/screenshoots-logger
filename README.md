# Otomatik Ekran Görüntüsü Gönderici

Bu Python betiği, belirli aralıklarla cihazınızın ekran görüntüsünü alır ve Discord üzerinden belirtilen bir kanala gönderir. Kullanıcı, internet bağlantısını kontrol edebilir ve ekran görüntüsünü Discord'a gönderebilir. Ekran görüntüsü alma işlemi `pyscreenshot` kütüphanesi kullanılarak gerçekleştirilir ve Discord'a gönderme işlemi için `discord_webhook` kütüphanesi kullanılır.

## Özellikler

- Belirli aralıklarla ekran görüntüsü alma ve Discord'a gönderme
- İnternet bağlantısını kontrol etme ve bağlantı varsa anında gönderme
- Ekran görüntüsü alırken ve Discord'a gönderirken hata yönetimi
- Cihaz adını Discord mesajında belirtme özelliği

## Kullanım

1. Discord Webhook URL'sini belirtin.
2. Kodu çalıştırın ve ekran görüntüsünün Discord'a düzenli olarak gönderilmesini izleyin.

## Kurulum

Projenin ana dizininde şu komutu kullanarak gerekli kütüphaneleri yükleyin:

pip install -r requirements.txt

markdown


## Kullanılan Kütüphaneler

- `discord_webhook`: Discord'a mesaj göndermek için kullanılır.
- `pyscreenshot`: Ekran görüntüsü alma işlemi için kullanılır.
- `requests`: İnternet bağlantısını kontrol etmek için kullanılır.

## Örnek Kullanım

### Komut Satırı Üzerinde Çalışma

Komut satırında aşağıdaki komutu kullanarak programı başlatın:

python screnshoots.py

css


Bu komut, `screnshoots.py` dosyasını çalıştırır ve ekran görüntüsü alma işlemini başlatır. Program, belirli aralıklarla ekran görüntüsü alacak ve Discord'a gönderecektir.

### Görünmez Komut Satırı Üzerinde Çalışma

Aşağıdaki komutu kullanarak programı arka planda (görünmez şekilde) çalıştırın:

python undercover-screnshoots.py

markdown


Bu komut, `undercover-screnshoots.py` dosyasını çalıştırır. Bu dosya, genellikle kullanıcıya herhangi bir çıktı veya görsel sunmaz, yani "görünmez" olarak çalışır. Bu dosyanın hangi senaryoda kullanılacağına bağlı olarak, gerekli planlamayı veya çağrıyı yapmanız gerekecektir.

## İletişim Bilgileri

- Discord: fatiqueos#0
- Telegram: [t.me/fatiqueos](https://t.me/fatiqueos)
