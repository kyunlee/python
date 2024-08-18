from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
from datetime import datetime

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

#Beautiful
soup = BeautifulSoup(res, "html.parser")

currency = soup.select("div.head_info > span.value")

#print(currency)

#for price  in currency:
#    print(price.string)


today = datetime.today().strftime("%Y%M%d")
#print(today) 

df = pd.DataFrame([currency[0], currency[1], currency[2],
                   currency[3], currency[4], currency[5],
                   currency[6], currency[7], currency[8],
                   currency[9], currency[10], currency[11]],
                   index=['미국USD', '일본JPY(100엔)','유럽연합EUR',
                         '중국CNY','달러/일본 엔', '유로/달러',
                         '영국파운드/달러', '달러인덱스', 'WTI',
                         '휘발유','국제 금','국내 금'],
                   columns=[today]
                  )
print(df) 

df.to_excel('D:/Autocoder/Naver_Currency.xlsx', sheet_name='finance' )