import requests
import json
import time
import subprocess

url = 'http://ntfy.sh/andy64/json' # ntfy stream url

aircon = 0 # aircon's state(0 is off, 1 is on)

#use irr.py lib(lib for recive and send infrared)
cmd = "python3 irr.py -p -g20 -f aircon on"

try:
    while True:
        with requests.get(url, stream=True) as res:
            for line in res.iter_lines():
                if line:
                    res = json.loads(line.decode('utf-8'))
                    if aircon == 0 and res["event"] == "message":
                        if res["message"] == "on":
                            subprocess.run([cmd], shell=True)
                            aircon = 1
                            
                time.sleep(3)
                
except KeyboardInterrupt:
    if aircon == 1:
        subprocess.run([cmd], shell=True)





