import urllib.parse

#graphql api POST 요청 request url decoding -> query로 넘어가는 variable field 확인
encoded_str = "%7B%22filterBy%22%3A%7B%22types%22%3A%5B%22ALL%22%5D%2C%22status%22%3A%22PUBLISHED%22%7D%2C%22orderBy%22%3A%7B%22field%22%3A%22PASSED_AT%22%2C%22direction%22%3A%22DESC%22%7D%2C%22pagination%22%3A%7B%22page%22%3A1%2C%22pageSize%22%3A20%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%229de3e00d7c080f21a562200ff07a8f380c724477caa7d564d356f47d8c84eb5b%22%7D%7D"
decoded_str = urllib.parse.unquote(encoded_str) # -> variable

# print(decoded_str)

json_str = '{"filterBy":{"types":["ALL"],"status":"PUBLISHED"},"orderBy":{"field":"PASSED_AT","direction":"DESC"},"pagination":{"page":1,"pageSize":20}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"9de3e00d7c080f21a562200ff07a8f380c724477caa7d564d356f47d8c84eb5b"}}'

# URL 쿼리 문자열로 인코딩, '&'와 '='는 인코딩하지 않음
encoded_str = urllib.parse.quote(json_str, safe='&=')

# print(encoded_str)

# safe option을 적용하지 않으면, 첫번째 문자열처럼 변환되어 &와 =까지 인코딩되어버린다. (하단 참고)
"%7B%22filterBy%22%3A%7B%22types%22%3A%5B%22ALL%22%5D%2C%22status%22%3A%22PUBLISHED%22%7D%2C%22orderBy%22%3A%7B%22field%22%3A%22PASSED_AT%22%2C%22direction%22%3A%22DESC%22%7D%2C%22pagination%22%3A%7B%22page%22%3A1%2C%22pageSize%22%3A20%7D%7D%26extensions%3D%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%229de3e00d7c080f21a562200ff07a8f380c724477caa7d564d356f47d8c84eb5b%22%7D%7D"
"%7B%22filterBy%22%3A%7B%22types%22%3A%5B%22ALL%22%5D%2C%22status%22%3A%22PUBLISHED%22%7D%2C%22orderBy%22%3A%7B%22field%22%3A%22PASSED_AT%22%2C%22direction%22%3A%22DESC%22%7D%2C%22pagination%22%3A%7B%22page%22%3A1%2C%22pageSize%22%3A20%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%229de3e00d7c080f21a562200ff07a8f380c724477caa7d564d356f47d8c84eb5b%22%7D%7D"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# 크롤링 실제 테스트
import requests

json_variable = '{"filterBy":{"types":["ALL"],"status":"PUBLISHED"},"orderBy":{"field":"PASSED_AT","direction":"DESC"},"pagination":{"page":1,"pageSize":20}}&extensions={"persistedQuery":{"version":1,"sha256Hash":"9de3e00d7c080f21a562200ff07a8f380c724477caa7d564d356f47d8c84eb5b"}}'
encoded_str = urllib.parse.quote(json_variable, safe='&=')

# url = f'https://api.linkareer.com/graphql?operationName=CoverLetterList&variables={encoded_str}' # json_variable을 직접 전달해도 문제는 생기지 않음.
url = "https://www.jobplanet.co.kr/api/v1/job/postings/1271027"
response = requests.get(url)
html = response.text
print(html)