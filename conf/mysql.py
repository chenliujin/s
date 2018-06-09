import pymysql

mysql = {}

mysql['host'] = "192.168.1.102"
mysql['port'] = 3306
mysql['user'] = "root"
mysql['passwd'] = "@liujin"
mysql['db'] = "stock"

conn = pymysql.connect(host=mysql['host'], port=mysql['port'], user=mysql['user'], passwd=mysql['passwd'], db=mysql['db'], charset="utf8")
cursor = conn.cursor()


