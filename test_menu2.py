import requests, json, re
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

url = 'https://www.dankook.ac.kr/web/kor/-555'  # API의 URL을 여기에 입력하세요.

response = requests.post(url)
ymd = pytz.timezone('Asia/Seoul')
day_code = datetime.now(ymd).weekday()

result = []
flag = 0

if response.status_code == 200:
    print("Successfully posted data to the server.")
    soup = BeautifulSoup(response.text, 'html.parser')
    target_table = soup.find('table', summary="요일, 식단메뉴").find('tbody')
    if target_table:
        tr_tags = target_table.find_all('tr')
        td_tags = tr_tags[day_code].find_all('td') #여기까지 하면 td_tags[1]로 오늘의 식단 HTML부분 추출 가능

    # [A코스], [B코스], [C코스] 정보 추출
    for br in td_tags[1].find_all('br'):
        info = br.next_sibling
        if info and isinstance(info, str) and ('코스' in info):
            course_info = ["중식" if flag == 0 else "석식"]
            flag = 1
            while True:
                br = br.next_sibling
                if (str(br)[0] == '('): continue # 괄호시작은 무시
                if not br or br.name == 'b' or '코스' in br.next_sibling:
                    break
                elif br.name != 'br' and len(br) > 1:
                    course_info.append(re.sub(r'[\'"\\$￦]', '', str(br).strip()).replace('  ', ' '))
            if (len(course_info) > 2):
                result.append(course_info)

    # 토요일저녁, 일요일, 공휴일 예외처리(len(result) == 0) -> status 필드를 false로
            
else:
    print("Failed to receive a valid response. Status Code:", response.status_code)
    print("Response:", response.text)

for i in result:
    print(i)
