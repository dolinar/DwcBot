import config.dbconfig as cfg
import sqlite3 as sql


def get_connection():
    db_name = cfg.db['db-name']
    return sql.connect(db_name)

