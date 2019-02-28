import requests

URL = 'http://lbf.com.br/ws/tempo_real_bybr/json/{id}_tempo_real.json'


def client(match_id):
    resp = requests.get(URL.format(id=match_id))
    return resp


def download(match_id):
    resp = client(match_id)
    status = resp.status_code
    if status == 200:
        result = resp.json()
    elif status == 404:
        result = match_id

    return result, status
