import requests, json
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

url = 'https://www.dankook.ac.kr/web/kor/-2014-'  # API의 URL을 여기에 입력하세요.

response = requests.post(url)
ymd = pytz.timezone('Asia/Seoul')
ymd = str(datetime.now(ymd))
ymd = datetime(int(ymd[:4]), int(ymd[5:7]), int(ymd[8:10]))

result = []
def date_val_check(s): # 기간 유효성 검사
    start_ymd = datetime(int(s[:4]), int(s[5:7]), int(s[8:10]))
    end_ymd = datetime(int(s[13:17]), int(s[18:20]), int(s[21:23]))
    if (start_ymd <= ymd <= end_ymd): return True
    else: return False


if response.status_code == 200:
    print("Successfully posted data to the server.")
    soup = BeautifulSoup(response.text, 'html.parser')
    target_div = soup.find('div', id="_Event_WAR_eventportlet_week_3")
    if target_div:
        # "detail" 클래스를 가진 태그 내부의 모든 'ul' 태그를 찾습니다.
        ul_tags = target_div.find('div', class_='detail').find('ul')
        li_tags = ul_tags.find_all('li')
        for li in li_tags:
            span_text = li.find('span').text.strip()
            a_text = li.find('a').text.strip()
            if (date_val_check(span_text) == True):
                result.append([span_text, a_text])

else:
    print("Failed to receive a valid response. Status Code:", response.status_code)
    print("Response:", response.text)

for i in result:
    print(i)
