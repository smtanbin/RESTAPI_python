import re

import cx_Oracle

# import mysql.connector

auth = re.split('[=\n]', open("auth.txt").read())

# config = {
#     'host': auth[1],
#     'database': auth[3],
#     'user': auth[5],
#     'password': auth[7],
#     'raise_on_warnings': True
# }


def execute(query):
    cnx = cx_Oracle.connect(user='TANBIN', password='@urA774234', dsn='10.130.102.103:1525/SBLABS')
    # cnx = mysql.connector.connect(**config)

    try:
        cursor = cnx.cursor()  # --> Oracle
        # cursor = cnx.cursor(dictionary=True)  # --> Mysql Connector
        cursor.execute(query)

        result = list()
        for data in cursor:
            result.append(data)

        cnx.commit()
        cursor.close()
        cnx.close()
        return result

    except Exception:
        cnx.rollback()
        return {'error': Exception}
