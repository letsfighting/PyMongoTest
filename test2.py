import pymongoarrow as pma
from pymongoarrow.monkey import patch_all
patch_all()
from pymongoarrow.api import Schema
from datetime import datetime
from pymongo import MongoClient
client = MongoClient()


schema = Schema({'_id': int, 'amount': float, 'last_updated': datetime})
df = client.db.data.find_pandas_all({'amount': {'$gt': 0}}, schema=schema)


# pandas
# df = client.db.data.aggregate_pandas_all([{'$match': {'amount': {'$lte': 10}}}], schema=schema)
# arrow
# arrow_table = client.db.data.aggregate_arrow_all([{'$match': {'amount': {'$lte': 10}}}], schema=schema)
# numpy
# ndarrays = client.db.data.aggregate_numpy_all([{'$match': {'amount': {'$lte': 10}}}], schema=schema)

df.to_csv('out.csv', index=False)