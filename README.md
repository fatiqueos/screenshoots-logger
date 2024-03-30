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

python screnshoots.py komut satırı üzerinde çalışır:

Bu durumda, screnshoots.py adlı Python dosyası doğrudan komut satırından çalıştırılabilir. Örneğin, terminal veya komut istemcisinde şu komutu kullanarak çalıştırabilirsiniz:

python screnshoots.py

Bu komut, screnshoots.py dosyasını çalıştırır ve ekran görüntüsü alma işlemini başlatır. Program, belirli aralıklarla ekran görüntüsü alacak ve Discord'a gönderecektir.
python undercover-screnshoots.py görünmez bir komut satırı üzerinde çalışır:

Bu durumda, undercover-screnshoots.py adlı Python dosyası, kullanıcıya görünmez şekilde (arka planda) çalışır. Bu tür bir işlem genellikle bir arka plan görevi veya bir betik tarafından gerçekleştirilir. Örneğin, bu tür bir betiği bir işletim sistemi zamanlayıcısı veya başka bir otomasyon aracılığıyla planlanabilir.

python undercover-screnshoots.py

Bu komut, undercover-screnshoots.py dosyasını çalıştırır. Bu dosya, genellikle kullanıcıya herhangi bir çıktı veya görsel sunmaz, yani "görünmez" olarak çalışır. Bu dosyanın hangi senaryoda kullanılacağına bağlı olarak, gerekli planlamayı veya çağrıyı yapmanız gerekecektir.
