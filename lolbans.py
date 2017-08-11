from multiprocessing import Process
import requests
import json
from flask import Flask, request

from bestbans import find_best_bans

app = Flask(__name__)


def lolbans_async(response_url):
    text = find_best_bans()
    headers = {'content-type': 'application/json'}
    data = {'response_type': 'in_channel', 'text':text}

    requests.post(response_url, data=json.dumps(data), headers=headers)


@app.route('/lolbans', methods=['GET', 'POST'])
def lolbans():
    p = Process(target=lolbans_async, args=(request.form['response_url'],))
    p.start()

    return 'Working...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
