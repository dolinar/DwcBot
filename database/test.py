import database.connection as conn


def test():
    connection = conn.get_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE test
                 (bla text)''')
    cursor.execute("INSERT INTO test VALUES ('enrfi')")
    connection.commit()
    connection.close()


def test_select():
    connection = conn.get_connection()
    cursor = connection.cursor()

    for row in cursor.execute('''SELECT * FROM test'''):
        print(row)
    connection.close()


def test_drop():
    connection = conn.get_connection()
    cursor = connection.cursor()
    cursor.execute('''DROP TABLE test''')
    connection.commit()
    connection.close()

