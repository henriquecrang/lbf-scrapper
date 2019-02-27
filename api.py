import requests


def client(match_id):
    url = f'http://lbf.com.br/ws/tempo_real_bybr/json/{match_id}'\
            '_tempo_real.json'
    resp = requests.get(url)
    return resp
