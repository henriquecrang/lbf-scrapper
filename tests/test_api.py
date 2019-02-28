from unittest import TestCase, mock

import responses

from api import client, download


class TestApi(TestCase):
    url_base = 'http://lbf.com.br/ws/tempo_real_bybr/json/{id}_tempo_real.json'

    @responses.activate
    def test_correct_response(self):
        url = self.url_base.format(id='123')
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

    @mock.patch('api.client')
    def test_download_match(self, _client):
        resp_mock = mock.MagicMock()
        resp_mock.status_code = 200
        resp_mock.json.return_value = {'id': 0}

        _client.return_value = resp_mock

        resp, status = download(match_id='0')

        _client.assert_called_once_with('0')
        self.assertEqual(resp, {'id': 0})
        self.assertEqual(status, 200)

    @mock.patch('api.client')
    def test_download_match_not_found(self, _client):
        resp_mock = mock.MagicMock()
        resp_mock.status_code = 404

        _client.return_value = resp_mock

        resp, status = download(match_id='1')

        _client.assert_called_once_with('1')
        self.assertEqual(resp, '1')
        self.assertEqual(status, 404)
