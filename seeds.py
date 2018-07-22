import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='the captain speaks spanish',
    charset='utf8')
c = db.cursor()
c.execute('use Populations')

with open('cities.txt') as f:
    for line in f:
        data = line.split('\t')
        data[-1] = data[-1][:-1]
        c.execute('insert into Cities values (%s, %s, %s, %s, %s, %s, %s)', \
                (int(data[0]), data[1], data[2], float(data[3]), float(data[4]), data[5], int(data[6]),))

db.commit()
db.close()