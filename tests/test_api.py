from unittest import TestCase, mock

import responses

from api import client, batch_download


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
    def test_download_all_matches(self, _client):
        resp_mock_1 = mock.MagicMock()
        resp_mock_2 = mock.MagicMock()
        resp_mock_3 = mock.MagicMock()
        resp_mock_1.status_code = 200
        resp_mock_1.json.return_value = {'id': 0}
        resp_mock_2.status_code = 404
        resp_mock_3.status_code = 200
        resp_mock_3.json.return_value = {'id': 2}

        _client.side_effect = [resp_mock_1, resp_mock_2, resp_mock_3]

        id_range = 3
        resp, missed = batch_download(id_range=id_range)

        client_calls = [
                mock.call(match_id=i) for i in range(id_range)
        ]
        _client.assert_has_calls(client_calls)
        self.assertIsInstance(resp, list)
        self.assertEqual(resp, [{'id': 0}, {'id': 2}])

        self.assertEqual(missed, [1])
