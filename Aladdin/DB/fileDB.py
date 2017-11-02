import json
from sys import argv

import gridfs
import os
from bson import ObjectId
from pymongo import MongoClient


def get_db_fs():
    conn_props={}
    with(open(os.path.dirname(os.path.abspath(__file__)) + '\\conn.json', 'r', encoding="UTF-8")) as conn_file:
        conn_props=json.load(conn_file)
    client = MongoClient(conn_props["ip"],conn_props["port"] )
    db = client[conn_props["db"]]
    return gridfs.GridFS(db)

def downloadFile(file_id=None):
    fs = get_db_fs()
    f_data = fs.get(ObjectId(file_id))

    fn = f_data.file_name
    if fn is None:
        fn = "file_from_db"
    fn = os.path.dirname(os.path.abspath(__file__)) + '\\'+fn
    with(open(fn, 'wb')) as f:
        f.write(f_data.read())

    return fn

if __name__=="__main__":
    print(downloadFile(argv[1]))