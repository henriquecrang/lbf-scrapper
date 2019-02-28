from decouple import config
from pymongo import MongoClient


def connect():
    return MongoClient(
        config('MONGO_ADDR'),
        config('MONGO_PORT', cast=int),
        username=config('MONGO_USER'),
        password=config('MONGO_PWD'),
        authSource=config('MONGO_AUTH_DB')
    )


def insert(data):
    pass
