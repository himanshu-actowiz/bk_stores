import mysql.connector


def make_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='actowiz',
        database='bk_stores'
    )
    return conn

def create_table(table_name: str):

    create_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name}(
        id INT AUTO_INCREMENT PRIMARY KEY,
        store_id VARCHAR(200),
        brand_name VARCHAR(200),
        address TEXT,
        locality VARCHAR(200),
        city VARCHAR(100),
        pincode VARCHAR(20),
        phone_number VARCHAR(50),
        timing VARCHAR(100),
        store_url TEXT,
        map_url TEXT
    )
    '''

    conn = make_connection()
    cursor = conn.cursor()

    cursor.execute(create_query)

    conn.commit()
    conn.close()

def insert_into_db(table_name: str, data: dict):
    cols = ",".join(list(data.keys()))
    vals = "".join([len(data.keys()) * '%s,']).strip(',')
    q = f"""INSERT INTO {table_name} ({cols}) VALUES ({vals})"""
    conn = make_connection()
    cursor = conn.cursor()
    cursor.execute(q, tuple(data.values()))
    conn.commit()
