@echo off
echo Android APK olusturuluyor...
echo.
echo NOT: Bu islem icin python-for-android gereklidir
echo.

pip install python-for-android

p4a create --requirements=python3,kivy,kivymd,pygame,mutagen,requests --private . --package=org.muzikapp --name "Muzik App" --version 0.1 --bootstrap=sdl2 --permission INTERNET --permission READ_EXTERNAL_STORAGE --permission WRITE_EXTERNAL_STORAGE

p4a apk --private . --package=org.muzikapp --name "Muzik App" --version 0.1 --bootstrap=sdl2 --requirements=python3,kivy,kivymd,pygame,mutagen,requests --permission INTERNET

echo.
echo APK olusturuldu!
pause
