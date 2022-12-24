#selenium ve diğer paketler içeri aktarılır




from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
tarayici = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#tarayıcıda gezinme
tarayici.get("https://teknolojiaihl.meb.k12.tr")
print(tarayici.current_url)
sleep(1)

tarayici.get("ttps://teknolojiaihl.meb.k12.tr/34/40/766892/teskilat_semasi.html")
sleep(1)

#geri dönelim
tarayici.back()
print(tarayici.title)
sleep(1)

#ileri gidelim
tarayici.forward()
print(tarayici.title)
sleep(1)

#pencere boyutunu yazdıralım
print(tarayici.get_window_size())

#pencere boyutunu ayarlayalım
tarayici.set_window_size(1024,728)
sleep(3)
#pencerenin pozisyonunu yazdıralım
print(tarayici.get_window_position())

# pencerenin pozisyonunu ayarlayalım
tarayici.set_window_position(100, 500)
sleep(2)