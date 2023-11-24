import mysql.connector as ms

class DBConnect2:
    def __init__(self):
        self.con=ms.connect(host='localhost',user='root',password='*#123Nitesh*#',\
                            database='party_info')
        self.cur=self.con.cursor()

    def insert(self,query,values):
        self.cur.execute(query,values)
        self.con.commit()

    def fetching(self, query):
        self.cur.execute(query)
        records = self.cur.fetchall()
        self.con.commit()
        return records

    def fetch(self, query):
        self.cur.execute(query)
        self.rows = self.cur.fetchall()
        self.con.commit()

    def update(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def delete(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def search_code(self, query, values):
        self.cur.execute(query, values)
        records = self.cur.fetchall()
        self.con.commit()
        return records

