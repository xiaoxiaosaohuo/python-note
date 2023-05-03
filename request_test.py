import requests
url = 'https://www.baidu.com'
response = requests.get(url)
print('状态码:',response.status_code)
print('响应内容:',response.text)