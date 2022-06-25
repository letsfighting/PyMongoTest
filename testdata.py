import pymongoarrow as pma
from pymongoarrow.monkey import patch_all
patch_all()

from datetime import datetime
from pymongo import MongoClient
client = MongoClient()
client.db.data.insert_many([
    {'_id': 5, 'amount': 21, 'last_updated': datetime(2020, 12, 10, 1, 3, 1)},
    {'_id': 6, 'amount': 16, 'last_updated': datetime(2020, 7, 23, 6, 7, 11)},
    {'_id': 7, 'amount': 3, 'last_updated': datetime(2021, 3, 10, 18, 43, 9)},
    {'_id': 8, 'amount': 0, 'last_updated': datetime(2021, 2, 25, 3, 50, 31)}])