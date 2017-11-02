import json
from sys import argv

import gridfs
import os
from bson import ObjectId
from pymongo import MongoClient


def get_db_fs():
    conn_props={}
    with(open(os.path.dirname(os.path.abspath(__file__)) + '\\conn.json', 'w', encoding="UTF-8")) as conn_file:
        json.dump(conn_props, conn_file)
    client = MongoClient(conn_props["ip"],conn_props["port"] )
    db = client[conn_props["db"]]
    fs = gridfs.GridFS(db)

def downloadFile(file_id=None):
    fs = get_db_fs()
    f_data = fs.get(ObjectId(file_id))

    fn = os.path.dirname(os.path.abspath(__file__)) + '\\'+f_data.filename
    with(open(fn, 'wb')) as f:
        f.write(f_data.read())

    return fn

if __name__=="__main__":
    print(downloadFile(argv[1]))