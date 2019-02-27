import requests

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
            jsons.append(resp.json())
        else:
            missed.append(id_)

    return jsons, missed
