import mysql.connector as ms

class DBConnect:
    def __init__(self):
        self.con=ms.connect(host='localhost',user='root',password='*#123Nitesh*#',\
                            database='database_login')
        self.cur=self.con.cursor()

    def insert(self,query,values):
        self.cur.execute(query,values)
        self.con.commit()
    def select(self,query,values):
        self.cur.execute(query,values)
        records=self.cur.fetchall()
        return records



