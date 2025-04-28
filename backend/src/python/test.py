import requests

url = "http://127.0.0.1:5000/optimize"
data = {"prompt": "你是谁？"}
resp = requests.post(url, json=data, stream=True)
for chunk in resp.iter_content(chunk_size=None, decode_unicode=True):
    print(chunk, end="")