from unittest import TestCase

import responses

from api import client


class TestApi(TestCase):
    @responses.activate
    def test_correct_response(self):
        url = 'http://lbf.com.br/ws/tempo_real_bybr/json/123_tempo_real.json'
        responses.add(
                responses.GET,
                url,
                json={'id': '123'},
                status=200
        )
        resp = client(match_id='123')
        expected = {
                'id': '123',
        }

        self.assertEqual(resp.json(), expected)
