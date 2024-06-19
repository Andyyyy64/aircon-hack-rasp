import requests
import json

url = 'http://ntfy.sh/aircon/json'

def get_stream():
    while(1):
        with requests.get(url, stream=True) as res:
            for line in res.iter_lines():
                if line:
                    data = json.loads(line.decode('utf-8'))
                    print(data)
get_stream()
