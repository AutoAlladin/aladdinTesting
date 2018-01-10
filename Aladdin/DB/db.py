import pyodbc
import sys
import os

import struct
from datetime import datetime, timezone, timedelta

def_args={
    '_server': '192.168.80.90',
    '_database': 'ApsMarketWork',
    '_username': 'web_actini_user',
    '_password': '18E2B855EB29411D9548FD8CA4E49DA7',
    '_driver': '{ODBC Driver 13 for SQL Server}'
}

def handle_datetimeoffset(dto_value):
    # ref: https://github.com/mkleehammer/pyodbc/issues/134#issuecomment-281739794
    tup = struct.unpack("<6hI2h", dto_value)  # e.g., (2017, 3, 16, 10, 35, 18, 0, -6, 0)
    tweaked = [tup[i] // 100 if i == 6 else tup[i] for i in range(len(tup))]
    #return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}.{:07d} {:+03d}:{:02d}".format(*tweaked)
    return datetime(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6] // 1000,
                    timezone(timedelta(hours=tup[7], minutes=tup[8])))


def get_connection(_server,_database,_username,_password,_driver):
    costr="DRIVER={driver};SERVER={server};PORT=1443;DATABASE={database};UID={username};PWD={password}"\
                          .format(driver=_driver,
                                  server=_server,
                                  database=_database,
                                  username=_username,
                                  password=_password
                                  )
    conn = pyodbc.connect(costr)
    conn.add_output_converter(-155, handle_datetimeoffset)
    return conn


#cursor = get_connection(**def_args).cursor()


cursor = get_connection(**def_args).cursor()






