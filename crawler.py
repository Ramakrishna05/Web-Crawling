import requests
import bs4

url = "https://www.andhrabank.in/Telugu/GenTheBankTelugu.aspx"
res = requests.get(url)
# print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')
partext = soup('p')

print(partext)
