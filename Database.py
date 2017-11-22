import psycopg2
import psycopg2.extras


class Database():
    conn = None
    cursor = None

    def __init__(self, url):
        self.conn = psycopg2.connect(url)
        self.cursor = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    def get_addresses(self):
        sql = '''
            SELECT 
                a.address_id "address_id", 
                a.hash "hash", 
                c.name "coin" 
            FROM 
                address a 
            NATURAL JOIN 
                coin c
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_address_users(self, id, type):
        sql = '''
            SELECT 
                w.type "type", 
                w.name "name", 
                w.notify "notify", 
                u.user_id "user_id", 
                u.email "email",
                u.email_template "template"
            FROM 
                watchlist w 
            JOIN 
                users u
            ON u.user_id = w.user_id
            WHERE w.address_id = %s AND w.type = %s
        '''
        self.cursor.execute(sql, (id, type))
        return self.cursor.fetchall()

    def get_last_block_number(self, coin):
        sql = '''
            SELECT 
                last_block 
            FROM 
                coin 
            WHERE 
                name = %s
        '''
        self.cursor.execute(sql, (str(coin),))
        result = self.cursor.fetchone()

        return result['last_block']

    def set_last_block_number(self, coin, number):
        sql = '''
            UPDATE 
                coin 
            SET 
                last_block = %s  
            WHERE 
                name = %s
        '''
        self.cursor.execute(sql, (number, str(coin),))
        self.conn.commit()
        