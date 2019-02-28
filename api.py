import requests

URL = 'http://lbf.com.br/ws/tempo_real_bybr/json/{id}_tempo_real.json'


def client(match_id):
    resp = requests.get(URL.format(id=match_id))
    return resp


def download(match_id):
    resp = client(match_id)
    if resp.status_code == 200:
        resp_json = resp.json()
        status = resp.status_code

    return resp_json, status
