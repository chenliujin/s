from flask import jsonify

import pymysql

host = "192.168.0.12"
port = 3306
user = "appuser_gm"
passwd = "123456"
db = "geomagnetism"
conn = None
cursor = None

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset="utf8")
cursor = conn.cursor()


class price_distribute:

  @staticmethod
  def index():
    sql="SELECT host_id, count(if(status=0, status, null)) as b, count(if(status=1, status, null)) as c FROM berth GROUP BY host_id";
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) == 0:
      return {}
    else:
      data = []

      for (host_id, s0, s1) in result: 
        price = {}
        price["price"] = host_id
        price["buy"] = s0 
        price["sale"] = s1 

        data.append(price)

      return data
