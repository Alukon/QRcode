# pip install django-qrcode
import qrcode
# Куда поведет картинка кода
data = "https://alukon27.ru"
# Куда сохраняем картинку кода
filename = "site.png"
# Создаем картинку кода
img = qrcode.make(data)
# Сохраняем картинку кода
img.save(filename)