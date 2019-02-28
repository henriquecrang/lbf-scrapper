from unittest import TestCase, mock

from decouple import config
from pymongo import MongoClient

import dao


class TestDao(TestCase):
    @mock.patch('dao.MongoClient', spec=MongoClient)
    def test_create_db_client(self, _mongo):
        client = dao.connect()

        _mongo.assert_called_with(
            config('MONGO_ADDR'),
            config('MONGO_PORT', cast=int),
            username=config('MONGO_USER'),
            password=config('MONGO_PWD'),
            authSource=config('MONGO_AUTH_DB')
        )

        self.assertIsInstance(client, MongoClient)
