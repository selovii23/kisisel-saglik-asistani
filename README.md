# Kişisel Sağlık Asistanı Projesi

Bu proje, kullanıcıların kişisel sağlık bilgilerini girerek günlük kalori ihtiyacını, makro besin dağılımını ve egzersiz önerilerini hesaplayabilmesini sağlayan bir masaüstü uygulamasıdır. Uygulama, kullanıcı dostu bir arayüz ile sağlıklı yaşam hedeflerine ulaşmalarına yardımcı olur.

## Projenin Amacı

Bu projenin amacı:
- Kullanıcıların günlük kalori ihtiyacını ve makro besin dağılımını hesaplamak,
- Kullanıcılara kişisel sağlık bilgilerine göre diyet planı önerileri sunmak,
- Kullanıcılara egzersiz hareketleri ve tekrar sayıları hakkında önerilerde bulunmak.

## Kurulum Talimatları

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### Gereksinimler

- Python 3.x
- `tkinter` kütüphanesi (Python ile birlikte gelir)
- `random` kütüphanesi (Python ile birlikte gelir)

### Adımlar

1. **Python'u İndirin ve Kurun**:
   - [Python resmi web sitesinden](https://www.python.org/) Python'u indirin ve kurun.

2. **Proje Dosyalarını İndirin**:
   - Bu proje dosyalarını bilgisayarınıza indirin.

3. **Proje Dosyalarını Çalıştırın**:
   - Terminal veya Komut İstemi'ni açın.
   - Proje dosyasının bulunduğu klasöre gidin.
   - Aşağıdaki komutu çalıştırın:
     ```sh
     python main.py
     ```

## Kullanım Detayları

Uygulama açıldığında, kullanıcı bilgilerini girerek günlük kalori ihtiyacını ve makro besin dağılımını hesaplayabilir. Ayrıca, diyet planı ve egzersiz önerileri de sunulmaktadır.

### Ana Menü

- **Kullanıcı Bilgiler Formu**: Kullanıcı bilgilerini girerek sonuçları hesaplayabileceğiniz form.
- **Egzersiz Hareketleri**: Mevcut egzersiz hareketlerini ve tekrar sayılarını görebileceğiniz liste.
- **Diyet Listesi**: Farklı diyet türlerini ve içeriklerini görebileceğiniz liste.

### Kullanıcı Bilgileri Formu

Kullanıcı, aşağıdaki bilgileri girerek hesaplamaları yapabilir:
- İsim
- Yaş
- Cinsiyet (Kadın veya Erkek)
- Boy (cm)
- Kilo (kg)
- Hareketlilik Seviyesi (Az Hareketli, Orta Hareketli, Çok Hareketli)
- Hedef (Kilo Vermek, Kilo Almak, Formu Korumak)
- Beslenme Tercihi (Normal, Vegan, Vejetaryen)
- Alerji veya Tüketilmeyen Besinler

### Sonuçların Gösterimi

Hesapla butonuna tıkladıktan sonra, uygulama yeni bir sayfada aşağıdaki bilgileri gösterir:
- Günlük kalori ihtiyacı
- Protein, yağ ve karbonhidrat miktarları
- Diyet planı
- Egzersiz önerileri

### Egzersiz Hareketleri

Egzersiz hareketleri sayfasında, mevcut tüm egzersiz hareketlerini ve tekrar sayılarını görebilirsiniz.

### Diyet Listesi

Diyet listesi sayfasında, farklı diyet türlerini ve içeriklerini görebilirsiniz. 



Eğer projeye katkıda bulunmak isterseniz, lütfen bir pull request oluşturun veya bir issue açın.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasını inceleyebilirsiniz.
