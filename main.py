from bs4 import BeautifulSoup
import requests
import lxml
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

URL="https://www.amazon.com/SLICE-RED-Android13-Smartphone-Fingerprint/dp/B0CJ77FJW1/ref=sr_1_1?crid=KUZDU1Y7Y93U&keywords=iphone%2B14%2Bpro%2Bmax&qid=1708230898"
responce= requests.get(URL,header)

soup=BeautifulSoup(responce.content,"lxml")
print(soup.title)