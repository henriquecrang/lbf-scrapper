import requests

from dao import insert

URL = 'http://lbf.com.br/ws/tempo_real_bybr/json/{id}_tempo_real.json'


def client(match_id):
    resp = requests.get(URL.format(id=match_id))
    return resp


def batch_download(id_range):
    jsons = []
    missed = []
    for id_ in range(id_range):
        resp = client(match_id=id_)
        if resp.status_code == 200:
            resp_json = resp.json()
            jsons.append(resp_json)
            insert(resp_json)
        else:
            missed.append(id_)

    return jsons, missed
