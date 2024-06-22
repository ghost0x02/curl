import requests
import os
from colorama import Fore, Style
from requests.exceptions import RequestException

os.system("pip3 install requests")
os.system("clear")

print(Fore.RED + """

        .---.
       /    _\ 
      /    (={)
     /     /_/
    (      |(_
    /\_.--'// \ 
   /L.|`--'(   \    BUM BUM BUM
  /  /\_____`).J\____'==HH===HH
  \ \  \ `  |  \__..--."'
   \ \._) `  \       (
    \_/(`-..-'L       )
      / `\_(   L\,--.'
      > --'`--   \ 
      |   | \    Y
      |__/|  \---'\ 
      |   |   `.  _)
      \   ;     )  |
       )`)|     |  |  curl 1.0v
       |  |     |  |
       |  |     |(o) coded by enesxsec and ghost0x02
       |(o)     /  \ 
       /  |     \(\_"> 
       \(\_)   

  THIS SOFTWARE IS FOR TESTING!!!

producer  〔coded by enesxsec〕
instagram 〔xsecit〕
github    〔https://github.com/ghost0x02〕


""")

print(Style.RESET_ALL)
print(Fore.CYAN + "")

def baslik_(url):
    try:
        response = requests.get(url)
        headers = response.headers

        print(f"{url} için başlıklar kontrol ediliyor\n")


        if 'Access-Control-Allow-Origin' in headers:
            print("CORS Politikası: Mevcut")
        else:
            print("CORS Politikası: Mevcut Değil")

        guvenlik_basliklari = {
            'X-Frame-Options': 'Clickjacking saldırılarına karşı koruma sağlar',
            'X-Content-Type-Options': 'MIME türü karıştırma saldırılarını önler',
            'Strict-Transport-Security': 'Güvenli (SSL/TLS üzerinden HTTP) bağlantıları zorunlu kılar',
            'Content-Security-Policy': 'XSS saldırılarını önlemeye yardımcı olur',
            'Referrer-Policy': 'İsteklerle gönderilen referrer bilgilerini kontrol eder',
            'Permissions-Policy': 'Sitenin bağlamında hangi tarayıcı özelliklerinin kullanılabileceğini belirtir',
            'X-XSS-Protection': 'XSS filtreleme',
            'Expect-CT': 'Belirli SSL/TLS yanlış yapılandırmalarını tespit eder ve önler',
            'Feature-Policy': 'Web geliştiricilerin çeşitli tarayıcı özelliklerini ve API\'leri seçici olarak etkinleştirmesine ve devre dışı bırakmasına izin verir',
            'Server': 'Bilgi sızdırma riski',
            'X-Powered-By': 'Bilgi sızdırma riski'
        }

        for header, description in guvenlik_basliklari.items():
            if header in headers:
                print(f"{header}: Mevcut ({description})")
            else:
                print(f"{header}: Mevcut Değil ({description})")

    except RequestException as e:
        print(f"Başlıkları kontrol ederken bir hata oluştu: {e}")

def metodlar_(url):
    try:
        metodlar = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH']
        print(f"\n{url} için HTTP metodları kontrol ediliyor\n")
        for method in metodlar:
            try:
                response = requests.request(method, url)
                print(f"{method}: {response.status_code}")
            except RequestException as e:
                print(f"{method}: Bir hata oluştu: {e}")
    except RequestException as e:
        print(f"Metodları kontrol ederken bir hata oluştu: {e}")

def yanit_(url, anahtar_kelimeler):
    try:
        response = requests.get(url)
        body = response.text

        print(f"\n{url} için yanıt gövdesi kontrol ediliyor\n")

        for keyword in anahtar_kelimeler:
            if keyword.lower() in body.lower():
                print(f"Yanıt gövdesinde '{keyword}' anahtar kelimesi bulundu")
            else:
                print(f"Yanıt gövdesinde '{keyword}' anahtar kelimesi bulunamadı")

    except RequestException as e:
        print(f"Yanıt gövdesini kontrol ederken bir hata oluştu: {e}")

def ssl_(url):
    try:
        response = requests.get(url)
        if response.url.startswith("https://"):
            print("SSL/TLS doğru yapılandırılmış.")
        else:
            print("Uyarı: SSL/TLS yapılandırılmamış.")
    except RequestException as e:
        print(f"SSL yapılandırmasını kontrol ederken bir hata oluştu: {e}")

def guvenlik_kontrolu(url):
    print(f"{url} için gelişmiş güvenlik kontrolü başlatılıyor\n")

    ssl_(url)
    baslik_(url)
    metodlar_(url)
    yanit_(url, ["error", "not found", "exception", "warning", "fail", "invalid", "unauthorized", "forbidden", "access denied"])

if __name__ == "__main__":
    site_url = input("Site URL'sini girin: ")
    guvenlik_kontrolu(site_url)
