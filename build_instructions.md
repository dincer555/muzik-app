# Android APK Oluşturma Talimatları

## Windows Kullanıcıları İçin

Windows'ta doğrudan APK oluşturamazsınız. 3 seçeneğiniz var:

### Seçenek 1: WSL (Windows Subsystem for Linux) Kullan

1. WSL2 yükle:
```powershell
wsl --install
```

2. Ubuntu'yu başlat ve projeyi kopyala

3. WSL içinde:
```bash
sudo apt update
sudo apt install -y python3-pip git zip unzip openjdk-17-jdk
pip3 install buildozer cython
buildozer -v android debug
```

### Seçenek 2: GitHub Actions (Otomatik, Ücretsiz)

1. Projeyi GitHub'a yükle
2. `.github/workflows/build.yml` dosyası oluştur (aşağıda)
3. GitHub'da Actions sekmesinden build'i başlat
4. APK'yı indir

### Seçenek 3: Online Servisler

- **Replit** - Online Python IDE, mobil build desteği var
- **Google Colab** - Ücretsiz, buildozer çalıştırabilirsin

## Linux/Mac Kullanıcıları İçin

```bash
pip install buildozer
buildozer -v android debug
```

APK: `bin/muzikapp-0.1-arm64-v8a_armeabi-v7a-debug.apk`

## Test Etme

Masaüstünde test et:
```bash
pip install -r requirements.txt
python main.py
```
