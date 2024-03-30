Otomatik Ekran Görüntüsü Gönderici

Bu Python betiği, belirli aralıklarla cihazınızın ekran görüntüsünü alır ve Discord üzerinden belirtilen bir kanala gönderir. Kullanıcı, internet bağlantısını kontrol edebilir ve ekran görüntüsünü Discord'a gönderebilir. Ekran görüntüsü alma işlemi pyscreenshot kütüphanesi kullanılarak gerçekleştirilir ve Discord'a gönderme işlemi için discord_webhook kütüphanesi kullanılır.
Özellikler

    Belirli aralıklarla ekran görüntüsü alma ve Discord'a gönderme
    İnternet bağlantısını kontrol etme ve bağlantı varsa anında gönderme
    Ekran görüntüsü alırken ve Discord'a gönderirken hata yönetimi
    Cihaz adını Discord mesajında belirtme özelliği

Kullanım

    Discord Webhook URL'sini belirtin.
    Kodu çalıştırın ve ekran görüntüsünün Discord'a düzenli olarak gönderilmesini izleyin.

Kurulum

Projenin ana dizininde şu komutu kullanarak gerekli kütüphaneleri yükleyin:

pip install -r requirements.txt

Kullanılan Kütüphaneler

    discord_webhook: Discord'a mesaj göndermek için kullanılır.
    pyscreenshot: Ekran görüntüsü alma işlemi için kullanılır.
    requests: İnternet bağlantısını kontrol etmek için kullanılır.

Örnek Kullanım

Terminal veya komut istemcisinde aşağıdaki komutu çalıştırarak programı başlatın:


python screnshoots.py
