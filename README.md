# Müzik Uygulaması

Python ve Kivy ile geliştirilmiş mobil müzik çalıcı uygulaması.

## Özellikler

- ✅ Müzik çalma/durdurma
- ✅ Playlist oluşturma ve yönetme
- ✅ Yerel dosyalardan müzik okuma
- ✅ Deezer API ile streaming entegrasyonu (ücretsiz)
- ✅ Müzik arama ve önizleme
- ✅ Alt navigasyon menüsü
- ✅ Karanlık tema

## Kurulum

```bash
pip install -r requirements.txt
```

## Çalıştırma

```bash
python main.py
```

## Mobil Derleme

### Android için:

1. Buildozer'ı yükle:
```bash
pip install buildozer
```

2. Android SDK ve NDK'yı yükle (buildozer otomatik yapabilir)

3. APK oluştur:
```bash
buildozer -v android debug
```

4. APK dosyası `bin/` klasöründe olacak

### iOS için:
Xcode ve kivy-ios gereklidir (sadece macOS'ta çalışır).

## Yapı

- `main.py` - Ana uygulama
- `screens/` - Uygulama ekranları
  - `home_screen.py` - Ana müzik çalıcı ekranı
  - `playlist_screen.py` - Playlist yönetimi
  - `search_screen.py` - Müzik arama
- `services/` - Servisler
  - `music_player.py` - Müzik çalma motoru
  - `playlist_manager.py` - Playlist yönetimi
  - `streaming_service.py` - Streaming API entegrasyonu
