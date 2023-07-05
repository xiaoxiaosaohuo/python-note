import requests
url = 'https://httpbin.org/get'
response = requests.get(url)
print('状态码:',response.status_code)
print('响应内容:',response.text)
print('cookie:',response.cookies)
print('headers:',response.headers)
