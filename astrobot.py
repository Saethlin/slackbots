from multiprocessing import Process
import requests
import json
from flask import Flask, request

from isitup import check_is_up
from brightstars import find_bright_stars

app = Flask(__name__)


@app.route('/isitup', methods=['GET', 'POST'])
def isitup():
    p = Process(target=isitup_async, args=(request.form['response_url'], request.form['text']))
    p.start()

    return 'Working...'


def isitup_async(response_url, target):
    text = check_is_up(target)
    headers = {'content-type': 'application/json'}
    data = {'response_type': 'in_channel', 'text':text}

    requests.post(response_url, data=json.dumps(data), headers=headers)


@app.route('/brightstars', methods=['GET', 'POST'])
def brightstars():
    p = Process(target=brightstars_async, args=(request.form['response_url'],))
    p.start()

    return 'Working...'


def brightstars_async(response_url):
    text = find_bright_stars()
    headers = {'content-type': 'application/json'}
    data = {'response_type': 'in_channel', 'text':text}

    requests.post(response_url, data=json.dumps(data), headers=headers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)

